"""
Categorization rules for financial transactions.
Each category can have multiple rules, and each rule can be of different types:
- 'contains': Matches if the column contains the specified value
- 'exact': Matches if the column exactly equals the specified value
- 'amount_range': Matches if the amount is within the specified range
"""

CATEGORY_RULES = {
    'Groceries': [
        {
            'type': 'contains',
            'column': 'Description',
            'value': 'WHOLE FOODS'
        },
        {
            'type': 'contains',
            'column': 'Description',
            'value': 'TRADER JOE'
        },
        {
            'type': 'contains',
            'column': 'Description',
            'value': 'SAFEWAY'
        }
    ],
    
    'Dining': [
        {
            'type': 'contains',
            'column': 'Description',
            'value': 'RESTAURANT'
        },
        {
            'type': 'contains',
            'column': 'Description',
            'value': 'CAFE'
        }
    ],
    
    'Transportation': [
        {
            'type': 'contains',
            'column': 'Description',
            'value': 'UBER'
        },
        {
            'type': 'contains',
            'column': 'Description',
            'value': 'LYFT'
        },
        {
            'type': 'contains',
            'column': 'Description',
            'value': 'GAS'
        }
    ],
    
    'Entertainment': [
        {
            'type': 'contains',
            'column': 'Description',
            'value': 'NETFLIX'
        },
        {
            'type': 'contains',
            'column': 'Description',
            'value': 'SPOTIFY'
        }
    ],
    
    'Utilities': [
        {
            'type': 'contains',
            'column': 'Description',
            'value': 'ELECTRIC'
        },
        {
            'type': 'contains',
            'column': 'Description',
            'value': 'WATER'
        },
        {
            'type': 'contains',
            'column': 'Description',
            'value': 'INTERNET'
        }
    ],
    
    'Income': [
        {
            'type': 'amount_range',
            'column': 'Amount',
            'min': 0,
            'max': float('inf')
        }
    ],
    
    'Shopping': [
        {
            'type': 'contains',
            'column': 'Description',
            'value': 'AMAZON'
        },
        {
            'type': 'contains',
            'column': 'Description',
            'value': 'TARGET'
        }
    ]
}

# Add your custom rules below
# Example:
# CATEGORY_RULES['Your Category'] = [
#     {
#         'type': 'contains',
#         'column': 'Description',
#         'value': 'YOUR KEYWORD'
#     }
# ] 