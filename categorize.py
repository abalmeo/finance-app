import pandas as pd
import os
from datetime import datetime
from config.categories import CATEGORY_RULES

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

def create_excel_report(df, output_path):
    """Create an Excel file with separate sheets for each category."""
    # Create Excel writer
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_file = os.path.join(output_path, f'categorized_finances_{timestamp}.xlsx')
    
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        # Write each category to a separate sheet
        for category in df['Category'].unique():
            # Filter transactions for this category
            category_df = df[df['Category'] == category]
            
            # Clean up the sheet name (Excel has a 31 character limit)
            sheet_name = str(category)[:31]
            
            # Write to Excel
            category_df.to_excel(writer, sheet_name=sheet_name, index=False)
            
            # Auto-adjust column widths
            worksheet = writer.sheets[sheet_name]
            for idx, col in enumerate(category_df.columns):
                max_length = max(
                    category_df[col].astype(str).apply(len).max(),
                    len(str(col))
                )
                worksheet.column_dimensions[chr(65 + idx)].width = min(max_length + 2, 50)
    
    print(f"Excel report created: {output_file}")
    return output_file

def main():
    # Check if input directory exists
    if not os.path.exists('input'):
        os.makedirs('input')
        print("Created 'input' directory. Please place your CSV files there.")
        return
    
    # Check if output directory exists
    if not os.path.exists('output'):
        os.makedirs('output')
    
    # Get all CSV files from input directory
    csv_files = [f for f in os.listdir('input') if f.endswith('.csv')]
    
    if not csv_files:
        print("No CSV files found in the 'input' directory.")
        print("Please export your transactions as CSV and place them in the 'input' directory.")
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
        
        # Create Excel report
        output_file = create_excel_report(df, 'output')
        
        print(f"Processing complete for {csv_file}")
        print(f"Output saved to: {output_file}")

if __name__ == "__main__":
    main() 