import { chromium } from 'playwright';
import dotenv from 'dotenv';
import path from 'path';
import os from 'os';

// Load environment variables
dotenv.config();

async function main() {
  // Get the user's Chrome profile path based on OS
  const userDataDir = process.env.CHROME_PROFILE_PATH || path.join(
    os.homedir(),
    'Library/Application Support/Google/Chrome/Default'
  );

  // Get Chrome executable path based on OS
  const chromeExecutablePath = process.env.CHROME_EXECUTABLE_PATH || 
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';

  console.log('Launching Chrome with your local profile...');
  console.log(`Profile path: ${userDataDir}`);
  
  const browser = await chromium.launchPersistentContext(userDataDir, {
    headless: false,
    executablePath: chromeExecutablePath,
    args: ['--start-maximized']
  });

  try {
    const page = await browser.newPage();
    
    // Navigate to Google Drive
    const targetUrl = 'https://drive.google.com/drive/my-drive';
    console.log(`Navigating to ${targetUrl}...`);
    await page.goto(targetUrl);
    
    // Wait for Drive to load
    await page.waitForSelector('div[role="main"]');
    
    // Click the "New" button
    console.log('Creating new Google Sheet...');
    await page.click('div[aria-label="New"]');
    
    // Click "Google Sheets" from the dropdown
    await page.click('div[aria-label="Google Sheets"]');
    
    // Wait for the new sheet to open in a new tab
    const newPagePromise = browser.waitForEvent('page');
    const newPage = await newPagePromise;
    await newPage.waitForLoadState();
    
    console.log('Setting up sheet structure...');
    
    // Wait for the sheet to be fully loaded
    await newPage.waitForSelector('div[role="grid"]');
    
    // Add column headers
    const headers = [
      'Date',
      'Description',
      'Category',
      'Amount',
      'Account',
      'Notes'
    ];
    
    // Click cell A1 and type the first header
    await newPage.click('div[role="gridcell"][aria-label="A1"]');
    await newPage.keyboard.type(headers[0]);
    
    // Type remaining headers
    for (let i = 1; i < headers.length; i++) {
      await newPage.keyboard.press('Tab');
      await newPage.keyboard.type(headers[i]);
    }
    
    // Format header row
    console.log('Formatting header row...');
    await newPage.click('div[role="gridcell"][aria-label="A1"]');
    await newPage.keyboard.down('Shift');
    for (let i = 1; i < headers.length; i++) {
      await newPage.keyboard.press('ArrowRight');
    }
    await newPage.keyboard.up('Shift');
    
    // Open formatting menu
    await newPage.click('div[aria-label="Format"]');
    await newPage.click('div[aria-label="Bold"]');
    
    // Freeze header row
    console.log('Freezing header row...');
    await newPage.click('div[role="gridcell"][aria-label="A1"]');
    await newPage.click('div[aria-label="View"]');
    await newPage.click('div[aria-label="Freeze"]');
    await newPage.click('div[aria-label="1 row"]');
    
    // Set column widths
    console.log('Setting column widths...');
    const columnWidths = {
      'A': 100, // Date
      'B': 300, // Description
      'C': 150, // Category
      'D': 100, // Amount
      'E': 150, // Account
      'F': 200  // Notes
    };
    
    for (const [col, width] of Object.entries(columnWidths)) {
      await newPage.click(`div[aria-label="${col}1"]`);
      await newPage.click('div[aria-label="Format"]');
      await newPage.click('div[aria-label="Column width"]');
      await newPage.keyboard.type(width.toString());
      await newPage.keyboard.press('Enter');
    }
    
    // Format Amount column as currency
    console.log('Formatting amount column...');
    await newPage.click('div[role="gridcell"][aria-label="D1"]');
    await newPage.click('div[aria-label="Format"]');
    await newPage.click('div[aria-label="Number"]');
    await newPage.click('div[aria-label="Currency"]');
    
    console.log('\n=== Sheet Setup Complete ===');
    console.log('The Google Sheet has been created and formatted with:');
    console.log('- Column headers: Date, Description, Category, Amount, Account, Notes');
    console.log('- Bold header row');
    console.log('- Frozen header row');
    console.log('- Appropriate column widths');
    console.log('- Currency formatting for Amount column');
    console.log('\nThe browser will remain open for you to review the sheet.');
    console.log('Press Ctrl+C in the terminal when you\'re done.');
    
    // Keep the browser open until the user manually closes it
    await new Promise(() => {});
    
  } catch (error) {
    console.error('An error occurred:', error);
  } finally {
    await browser.close();
  }
}

main().catch(console.error); 