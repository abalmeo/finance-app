# Finance Categorization App

A Python application that automatically categorizes financial transactions from CSV files and creates a formatted Google Sheet with the categorized data.

## Features

- Load and parse CSV transaction files
- Automatically categorize transactions based on configurable rules
- Create and format Google Sheets with proper structure
- Easy-to-update categorization rules
- Secure Google Sheets integration

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Google Cloud Platform account
- Google Sheets API enabled

## Installation

1. Clone the repository
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up Google Sheets API:
   - Go to the [Google Cloud Console](https://console.cloud.google.com)
   - Create a new project
   - Enable the Google Sheets API
   - Create OAuth 2.0 credentials
   - Download the credentials and save as `credentials.json` in the project directory

## Usage

1. Export your transactions as CSV from your bank/finance site
2. Place the CSV file(s) in the `input` directory
3. Run the script:
   ```bash
   python categorize.py
   ```
4. On first run, you'll be prompted to authorize the application
5. The script will create a new Google Sheet with your categorized transactions

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
├── config/
│   └── categories.py      # Categorization rules
├── credentials.json       # Google API credentials
├── token.pickle          # OAuth token (created on first run)
└── requirements.txt       # Python dependencies
```

## Security Note

- Your Google credentials are stored locally in `token.pickle`
- The script only requests access to Google Sheets
- No sensitive data is stored in the cloud

## License

ISC