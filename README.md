# Finance Categorization App

A Python application that automatically categorizes financial transactions from CSV files and organizes them into an Excel workbook with separate sheets for each category.

## Features

- Load and parse CSV transaction files
- Automatically categorize transactions based on configurable rules
- Create Excel workbook with separate sheets for each category
- Easy-to-update categorization rules
- Offline-first operation (no cloud dependencies)

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Export your transactions as CSV from your bank/finance site
2. Place the CSV file(s) in the `input` directory
3. Run the script:
   ```bash
   python categorize.py
   ```
4. Find the categorized Excel file in the `output` directory

## Customizing Categories

Edit the `config/categories.py` file to customize how transactions are categorized. The file includes example rules for common categories like:
- Groceries
- Dining
- Transportation
- Entertainment
- Utilities
- Income
- Shopping

Each category can have multiple rules, and each rule can be of different types:
- `contains`: Matches if the column contains the specified value
- `exact`: Matches if the column exactly equals the specified value
- `amount_range`: Matches if the amount is within the specified range

Example rule:
```python
{
    'type': 'contains',
    'column': 'Description',
    'value': 'WHOLE FOODS'
}
```

## Directory Structure

```
finance-categorizer/
├── categorize.py          # Main script
├── input/                 # Place your CSV files here
├── output/                # Categorized Excel files will be saved here
├── config/
│   └── categories.py      # Categorization rules
└── requirements.txt       # Python dependencies
```

## License

ISC