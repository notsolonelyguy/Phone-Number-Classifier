# Phone Number Classifier

A Python utility for classifying phone numbers from CSV data, specifically identifying Indian phone numbers and categorizing international numbers by country. I had created this tool to help my team in my previous internship to segreate leads from diffrent countries (based on their phone numbers) for cold calling and marketing campaigns. I saved almost 9 hours of manual tasks and made them quite a lot of money.

## 📋 Overview

This tool processes CSV files containing phone number data to:
- Identify and separate Indian phone numbers based on standard formats
- Categorize international phone numbers by country
- Generate detailed statistics about the distribution of numbers
- Export the separated data into distinct CSV files

## 🚀 Features

- **Robust Indian number detection** - recognizes multiple Indian phone number formats:
  - Numbers with +91 prefix
  - Numbers with 91 prefix (without plus)
  - 10-digit numbers starting with 6, 7, 8, or 9
- **International number classification** - identifies numbers from 13+ countries including UAE, USA/Canada, UK, Australia, etc.
- **Comprehensive reporting** - provides percentage breakdowns and country distribution statistics
- **Clean data handling** - properly processes various formats with spaces, hyphens, and parentheses

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/your-username/phone-number-classifier.git

# Navigate to the project directory
cd phone-number-classifier

# Install dependencies
pip install pandas
```

## 📊 Usage

1. Update the file paths in the script:
```python
input_file = "path/to/your/input.csv"
indian_output = "path/to/save/indian_numbers.csv"
international_output = "path/to/save/international_numbers.csv"
```

2. Run the script:
```bash
python phone_classifier.py
```

3. Check the console output for statistics and verify the generated CSV files.

## 📝 Example Output

The script provides detailed statistics in the console:

```
Total entries: 1000
Indian phone numbers: 750 (75.00%)
International phone numbers: 250 (25.00%)

Indian numbers saved to: /path/to/indian_numbers.csv
International numbers saved to: /path/to/international_numbers.csv

International numbers by country:
UAE: 50 (20.00%)
USA/Canada: 45 (18.00%)
UK: 35 (14.00%)
...
```

## 🔍 When to Use This Tool

This utility is particularly useful for:
- Marketing teams separating domestic and international leads
- Customer service departments routing calls based on region
- Data analysis teams preparing region-specific reports
- Cleaning and standardizing phone number data

## 📈 Future Improvements

Potential enhancements for future versions:
- Add support for more countries
- Implement phone number validation beyond classification
- Add GUI interface for easier usage
- Support additional input/output formats beyond CSV

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
