import { chromium } from 'playwright';
import dotenv from 'dotenv';

// Load environment variables
dotenv.config();

async function main() {
  const browser = await chromium.launch({
    headless: process.env.HEADLESS === 'true'
  });

  try {
    const context = await browser.newContext();
    const page = await context.newPage();

    // Navigate to the target URL
    const targetUrl = process.env.TARGET_URL || 'https://www.capitalone.com';
    console.log(`Navigating to ${targetUrl}...`);
    
    await page.goto(targetUrl);
    
    // Log the page title
    const title = await page.title();
    console.log(`Page title: ${title}`);
    
    // Wait a bit to see the page (if not headless)
    if (process.env.HEADLESS !== 'true') {
      await new Promise(resolve => setTimeout(resolve, 5000));
    }
  } catch (error) {
    console.error('An error occurred:', error);
  } finally {
    await browser.close();
  }
}

main().catch(console.error); 