#!/usr/bin/env python3
import pandas as pd
import re
import argparse
import os

def is_indian_phone_number(phone):
    """
    Identifies if a phone number is from India based on standard formats.
    
    Args:
        phone (str): The phone number to check
        
    Returns:
        bool: True if the number is identified as Indian, False otherwise
    """
    if not phone or not isinstance(phone, str):
        return False
    
    # Remove any whitespace, hyphens, or parentheses
    cleaned_phone = re.sub(r'[\s\-\(\)]', '', phone)
    
    # Check for +91 prefix
    if cleaned_phone.startswith('+91'):
        return True
    
    # Check for 91 prefix without plus
    if cleaned_phone.startswith('91') and (len(cleaned_phone) >= 12 and len(cleaned_phone) <= 13):
        return True
    
    # Check for 10-digit number starting with 9, 8, 7, or 6 (Indian mobile formats)
    if re.match(r'^[6-9]\d{9}$', cleaned_phone):
        return True
    
    # The numbers starting with 91 but belonging to other countries (like Germany 49-17...)
    # should not be classified as Indian
    if cleaned_phone.startswith('491') or cleaned_phone.startswith('4917'):
        return False
    
    return False

def get_country_from_phone(phone):
    """
    Identifies the country for international phone numbers.
    
    Args:
        phone (str): The phone number to check
        
    Returns:
        str: The country name or 'Unknown'/'Other' if not identified
    """
    if not phone or not isinstance(phone, str):
        return 'Unknown'
    
    cleaned_phone = re.sub(r'[\s\-\(\)]', '', phone)
    
    # Check common country codes
    country_codes = {
        '971': 'UAE',
        '61': 'Australia',
        '44': 'UK',
        '1': 'USA/Canada',
        '977': 'Nepal',
        '94': 'Sri Lanka',
        '60': 'Malaysia',
        '880': 'Bangladesh',
        '974': 'Qatar',
        '973': 'Bahrain',
        '49': 'Germany',
        '65': 'Singapore',
        '966': 'Saudi Arabia'
    }
    
    for code, country in country_codes.items():
        if cleaned_phone.startswith(code):
            return country
    
    return 'Other'

def process_phone_numbers(input_csv, indian_output_csv, international_output_csv, phone_column='Phone'):
    """
    Process a CSV file to separate Indian and international phone numbers.
    
    Args:
        input_csv (str): Path to the input CSV file
        indian_output_csv (str): Path to save Indian numbers CSV
        international_output_csv (str): Path to save international numbers CSV
        phone_column (str): Name of the column containing phone numbers
        
    Returns:
        tuple: Counts of (total, indian, international) entries
    """
    # Read the CSV file
    print(f"Reading file from: {input_csv}")
    df = pd.read_csv(input_csv)
    
    # Ensure the phone column exists
    if phone_column not in df.columns:
        print(f"Error: Column '{phone_column}' not found in CSV. Available columns: {', '.join(df.columns)}")
        print(f"Please specify the correct column name using the --phone-column parameter.")
        return (0, 0, 0)
    
    # Create a mask to filter Indian phone numbers
    indian_mask = df[phone_column].apply(is_indian_phone_number)
    
    # Separate into two DataFrames
    indian_df = df[indian_mask].copy()
    international_df = df[~indian_mask].copy()
    
    # Add country information to the international numbers
    international_df['Country'] = international_df[phone_column].apply(get_country_from_phone)
    
    # Create output directories if they don't exist
    for path in [indian_output_csv, international_output_csv]:
        os.makedirs(os.path.dirname(os.path.abspath(path)) or '.', exist_ok=True)
    
    # Save to separate CSV files
    indian_df.to_csv(indian_output_csv, index=False)
    international_df.to_csv(international_output_csv, index=False)
    
    # Print statistics
    total_entries = len(df)
    indian_entries = len(indian_df)
    international_entries = len(international_df)
    
    print(f"Total entries: {total_entries}")
    print(f"Indian phone numbers: {indian_entries} ({indian_entries/total_entries*100:.2f}% if total_entries > 0 else 0}%)")
    print(f"International phone numbers: {international_entries} ({international_entries/total_entries*100:.2f}% if total_entries > 0 else 0}%)")
    
    print(f"\nIndian numbers saved to: {indian_output_csv}")
    print(f"International numbers saved to: {international_output_csv}")
    
    # Optional: Print country distribution for international numbers
    if international_entries > 0:
        country_counts = international_df['Country'].value_counts()
        print("\nInternational numbers by country:")
        for country, count in country_counts.items():
            print(f"{country}: {count} ({count/international_entries*100:.2f}%)")
    
    return (total_entries, indian_entries, international_entries)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Process CSV files to separate Indian and international phone numbers.')
    parser.add_argument('input_file', help='Path to the input CSV file')
    parser.add_argument('--indian-output', default='indian_numbers.csv', 
                        help='Path to save the CSV with Indian numbers (default: indian_numbers.csv)')
    parser.add_argument('--international-output', default='international_numbers.csv',
                        help='Path to save the CSV with international numbers (default: international_numbers.csv)')
    parser.add_argument('--phone-column', default='Phone',
                        help='Name of the column containing phone numbers (default: Phone)')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Run the process
    process_phone_numbers(
        args.input_file, 
        args.indian_output, 
        args.international_output,
        args.phone_column
    )

if __name__ == "__main__":
    main()
