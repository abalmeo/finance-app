# Finance Automation Agent

A simple automation script that uses Playwright to open a browser and navigate to financial websites. This is the first step toward automating manual finance tasks like downloading statements and organizing them.

## Features

- Launch a Chromium browser instance using Playwright
- Navigate to a specified URL
- Configurable headless mode
- Error handling and logging

## Prerequisites

- Node.js (v14 or higher)
- npm

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   npm install
   ```
3. Create a `.env` file in the root directory with the following variables:
   ```
   TARGET_URL=https://www.capitalone.com
   HEADLESS=true
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

## Configuration

- `TARGET_URL`: The URL to navigate to (default: https://www.capitalone.com)
- `HEADLESS`: Set to 'true' to run in headless mode, 'false' to show the browser UI

## License

ISC