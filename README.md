# Finance Automation Agent

A simple automation script that uses Playwright to launch Chrome with your local profile and navigate to Google Drive. This allows you to work with your financial data while maintaining security and control.

## Features

- Launch Chrome using your local user profile
- Automatically navigate to Google Drive
- Manual spreadsheet creation and management
- Secure handling of credentials (using your existing Chrome profile)
- Maximized browser window for better visibility

## Prerequisites

- Node.js (v14 or higher)
- npm
- Google Chrome installed
- Google account with Drive access

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   npm install
   ```
3. Create a `.env` file in the root directory with the following variables (optional):
   ```
   CHROME_PROFILE_PATH=/path/to/your/chrome/profile
   CHROME_EXECUTABLE_PATH=/path/to/chrome/executable
   ```

## Usage

Development mode:
```bash
npm run dev
```

Production mode:
```bash
npm run build
npm start
```

## How it Works

1. The script launches Chrome using your local profile (staying logged into your accounts)
2. Automatically navigates to Google Drive
3. Provides instructions for manual steps:
   - Navigate to your financial folder
   - Create a new Google Sheet
   - Name your spreadsheet appropriately
4. Keeps the browser open until you manually close it (Ctrl+C in terminal)

## Configuration

- `CHROME_PROFILE_PATH`: Path to your Chrome profile directory (defaults to standard location)
- `CHROME_EXECUTABLE_PATH`: Path to Chrome executable (defaults to standard location)

## Security Note

This script uses your local Chrome profile, which means:
- Your existing login sessions are preserved
- No credentials are stored in the script
- All sensitive operations are performed manually in your secure browser context

## License

ISC