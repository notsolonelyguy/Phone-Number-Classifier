# How to Use Phone Number Classifier

This guide explains how to use the Phone Number Classifier tool from the command line.

## Basic Usage

```bash
python phone_classifier.py input_file.csv
```

This will process `input_file.csv` and create two output files in the current directory:
- `indian_numbers.csv` - containing all Indian phone numbers
- `international_numbers.csv` - containing all international phone numbers with country information

## Command Line Options

### Specifying Output Files

```bash
python phone_classifier.py input_file.csv --indian-output path/to/indian.csv --international-output path/to/international.csv
```

### Custom Phone Column Name

If your CSV uses a column name other than "Phone" for phone numbers:

```bash
python phone_classifier.py input_file.csv --phone-column PhoneNumber
```

### Full Example

```bash
python phone_classifier.py customer_data.csv --indian-output output/indian_customers.csv --international-output output/international_customers.csv --phone-column ContactNumber
```

## Sample Run with Example Data

Try running the tool with the included sample data:

```bash
python phone_classifier.py examples/sample_data.csv
```

Expected output:
```
Reading file from: examples/sample_data.csv
Total entries: 10
Indian phone numbers: 5 (50.00%)
International phone numbers: 5 (50.00%)

Indian numbers saved to: indian_numbers.csv
International numbers saved to: international_numbers.csv

International numbers by country:
USA/Canada: 2 (40.00%)
UK: 1 (20.00%)
UAE: 1 (20.00%)
Singapore: 1 (20.00%)
```
