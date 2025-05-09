import pandas as pd
import os
from datetime import datetime
from config.categories import CATEGORY_RULES
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import pickle

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def get_google_sheets_service():
    """Get or create Google Sheets API service."""
    creds = None
    # The file token.pickle stores the user's access and refresh tokens
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('sheets', 'v4', credentials=creds)

def create_google_sheet(service, title):
    """Create a new Google Sheet."""
    spreadsheet = {
        'properties': {
            'title': title
        }
    }
    spreadsheet = service.spreadsheets().create(body=spreadsheet).execute()
    return spreadsheet['spreadsheetId']

def format_google_sheet(service, spreadsheet_id, df):
    """Format the Google Sheet with proper structure and styling."""
    # Prepare the data
    headers = ['Date', 'Description', 'Category', 'Amount', 'Account', 'Notes']
    data = [headers] + df[headers].values.tolist()
    
    # Clear existing content
    range_name = 'A1:F1000'  # Adjust range as needed
    service.spreadsheets().values().clear(
        spreadsheetId=spreadsheet_id,
        range=range_name
    ).execute()
    
    # Update values
    body = {
        'values': data
    }
    service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range=range_name,
        valueInputOption='RAW',
        body=body
    ).execute()
    
    # Format header row
    requests = [
        {
            'repeatCell': {
                'range': {
                    'sheetId': 0,
                    'startRowIndex': 0,
                    'endRowIndex': 1
                },
                'cell': {
                    'userEnteredFormat': {
                        'backgroundColor': {
                            'red': 0.8,
                            'green': 0.8,
                            'blue': 0.8
                        },
                        'textFormat': {
                            'bold': True
                        }
                    }
                },
                'fields': 'userEnteredFormat(backgroundColor,textFormat)'
            }
        },
        {
            'updateSheetProperties': {
                'properties': {
                    'sheetId': 0,
                    'gridProperties': {
                        'frozenRowCount': 1
                    }
                },
                'fields': 'gridProperties.frozenRowCount'
            }
        },
        {
            'updateDimensionProperties': {
                'range': {
                    'sheetId': 0,
                    'dimension': 'COLUMNS',
                    'startIndex': 0,
                    'endIndex': 1
                },
                'properties': {
                    'pixelSize': 100
                },
                'fields': 'pixelSize'
            }
        },
        {
            'updateDimensionProperties': {
                'range': {
                    'sheetId': 0,
                    'dimension': 'COLUMNS',
                    'startIndex': 1,
                    'endIndex': 2
                },
                'properties': {
                    'pixelSize': 300
                },
                'fields': 'pixelSize'
            }
        },
        {
            'updateDimensionProperties': {
                'range': {
                    'sheetId': 0,
                    'dimension': 'COLUMNS',
                    'startIndex': 2,
                    'endIndex': 3
                },
                'properties': {
                    'pixelSize': 150
                },
                'fields': 'pixelSize'
            }
        },
        {
            'updateDimensionProperties': {
                'range': {
                    'sheetId': 0,
                    'dimension': 'COLUMNS',
                    'startIndex': 3,
                    'endIndex': 4
                },
                'properties': {
                    'pixelSize': 100
                },
                'fields': 'pixelSize'
            }
        },
        {
            'updateDimensionProperties': {
                'range': {
                    'sheetId': 0,
                    'dimension': 'COLUMNS',
                    'startIndex': 4,
                    'endIndex': 5
                },
                'properties': {
                    'pixelSize': 150
                },
                'fields': 'pixelSize'
            }
        },
        {
            'updateDimensionProperties': {
                'range': {
                    'sheetId': 0,
                    'dimension': 'COLUMNS',
                    'startIndex': 5,
                    'endIndex': 6
                },
                'properties': {
                    'pixelSize': 200
                },
                'fields': 'pixelSize'
            }
        }
    ]
    
    # Apply formatting
    service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body={'requests': requests}
    ).execute()

def load_transactions(file_path):
    """Load and parse the CSV file."""
    try:
        # Try to detect the delimiter
        with open(file_path, 'r') as f:
            first_line = f.readline()
            delimiter = ',' if ',' in first_line else '\t'
        
        # Read the CSV file
        df = pd.read_csv(file_path, delimiter=delimiter)
        print(f"Successfully loaded {len(df)} transactions")
        return df
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return None

def categorize_transactions(df):
    """Categorize transactions based on rules."""
    # Create a new column for categories
    df['Category'] = 'Uncategorized'
    
    # Apply categorization rules
    for category, rules in CATEGORY_RULES.items():
        for rule in rules:
            if rule['type'] == 'contains':
                mask = df[rule['column']].str.contains(rule['value'], case=False, na=False)
            elif rule['type'] == 'exact':
                mask = df[rule['column']] == rule['value']
            elif rule['type'] == 'amount_range':
                mask = (df[rule['column']] >= rule['min']) & (df[rule['column']] <= rule['max'])
            
            df.loc[mask, 'Category'] = category
    
    return df

def main():
    # Check if input directory exists
    if not os.path.exists('input'):
        os.makedirs('input')
        print("Created 'input' directory. Please place your CSV files there.")
        return
    
    # Get all CSV files from input directory
    csv_files = [f for f in os.listdir('input') if f.endswith('.csv')]
    
    if not csv_files:
        print("No CSV files found in the 'input' directory.")
        print("Please export your transactions as CSV and place them in the 'input' directory.")
        return
    
    # Initialize Google Sheets service
    try:
        service = get_google_sheets_service()
    except Exception as e:
        print(f"Error initializing Google Sheets service: {e}")
        print("Please make sure you have set up the Google Sheets API and have credentials.json in the project directory.")
        return
    
    # Process each CSV file
    for csv_file in csv_files:
        print(f"\nProcessing {csv_file}...")
        file_path = os.path.join('input', csv_file)
        
        # Load transactions
        df = load_transactions(file_path)
        if df is None:
            continue
        
        # Categorize transactions
        df = categorize_transactions(df)
        
        # Create Google Sheet
        timestamp = datetime.now().strftime('%Y-%m-%d')
        sheet_title = f'Financial Transactions {timestamp}'
        spreadsheet_id = create_google_sheet(service, sheet_title)
        
        # Format the sheet
        format_google_sheet(service, spreadsheet_id, df)
        
        print(f"Processing complete for {csv_file}")
        print(f"Google Sheet created: https://docs.google.com/spreadsheets/d/{spreadsheet_id}")

if __name__ == "__main__":
    main() 