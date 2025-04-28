import pandas as pd
import re

# Function to identify Indian phone numbers
def is_indian_phone_number(phone):
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

# Function to identify country for international numbers
def get_country_from_phone(phone):
    if not phone or not isinstance(phone, str):
        return 'Unknown'
    
    cleaned_phone = re.sub(r'[\s\-\(\)]', '', phone)
    
    # Check common country codes
    if cleaned_phone.startswith('971'): return 'UAE'
    if cleaned_phone.startswith('61'): return 'Australia'
    if cleaned_phone.startswith('44'): return 'UK'
    if cleaned_phone.startswith('1'): return 'USA/Canada'
    if cleaned_phone.startswith('977'): return 'Nepal'
    if cleaned_phone.startswith('94'): return 'Sri Lanka'
    if cleaned_phone.startswith('60'): return 'Malaysia'
    if cleaned_phone.startswith('880'): return 'Bangladesh'
    if cleaned_phone.startswith('974'): return 'Qatar'
    if cleaned_phone.startswith('973'): return 'Bahrain'
    if cleaned_phone.startswith('49'): return 'Germany'
    if cleaned_phone.startswith('65'): return 'Singapore'
    if cleaned_phone.startswith('966'): return 'Saudi Arabia'
    
    return 'Other'

# Main function to process the CSV
def process_phone_numbers(input_csv, indian_output_csv, international_output_csv):
    # Read the CSV file
    print(f"Reading file from: {input_csv}")
    df = pd.read_csv(input_csv)
    
    # Create a mask to filter Indian phone numbers
    indian_mask = df['Phone'].apply(is_indian_phone_number)
    
    # Separate into two DataFrames
    indian_df = df[indian_mask].copy()
    international_df = df[~indian_mask].copy()
    
    # Add country information to the international numbers
    international_df['Country'] = international_df['Phone'].apply(get_country_from_phone)
    
    # Save to separate CSV files
    indian_df.to_csv(indian_output_csv, index=False)
    international_df.to_csv(international_output_csv, index=False)
    
    print(f"Total entries: {len(df)}")
    print(f"Indian phone numbers: {len(indian_df)} ({len(indian_df)/len(df)*100:.2f}%)")
    print(f"International phone numbers: {len(international_df)} ({len(international_df)/len(df)*100:.2f}%)")
    
    print(f"\nIndian numbers saved to: {indian_output_csv}")
    print(f"International numbers saved to: {international_output_csv}")
    
    # Optional: Print country distribution for international numbers
    if len(international_df) > 0:
        country_counts = international_df['Country'].value_counts()
        print("\nInternational numbers by country:")
        for country, count in country_counts.items():
            print(f"{country}: {count} ({count/len(international_df)*100:.2f}%)")

# Specify the file paths
input_file = "/Users/sohumdhar/Downloads/SBA App Launch Masterclass Apr 2025.csv"
indian_output = "/Users/sohumdhar/Downloads/indian_numbers.csv"
international_output = "/Users/sohumdhar/Downloads/international_numbers.csv"

# Run the process
process_phone_numbers(input_file, indian_output, international_output)
