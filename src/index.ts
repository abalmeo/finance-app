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
    
    console.log('\n=== Manual Steps ===');
    console.log('1. Navigate to your financial folder');
    console.log('2. Create a new Google Sheet');
    console.log('3. Name your spreadsheet appropriately');
    console.log('\nThe browser will remain open for you to complete these steps.');
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