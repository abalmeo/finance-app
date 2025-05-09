pivot... too risky
# 🧾 Finance Automation Agent (MVP v0.3)

This version pivots away from full automation. Instead, it focuses on launching Chrome using your actual logged-in profile and recording your manual steps (e.g., creating a new Google Sheet in a financial folder). This hybrid model gives you full control of sensitive data while enabling future automation.

---

## 📌 Objective

Launch Chrome using your existing local profile so you stay logged into your accounts (e.g., Google Drive), and begin recording your interactions manually (e.g., creating a spreadsheet). This lays the foundation for future automation by identifying and recording consistent behaviors.

---

## 🛠 Scope (MVP v0.3)

- Launch Chrome using your default local profile
- Open a new tab to Google Drive
- Manually navigate to your financial folder (or root directory)
- Create a new Google Sheet manually
- Log or capture each action for future automation reference

---

## ✨ Features

| Feature                      | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| Launch with Chrome profile   | Opens a browser with your actual local user profile to stay signed in       |
| Google Drive entry point     | Automatically navigates to Google Drive homepage                            |
| Manual spreadsheet creation  | You manually create and name a new spreadsheet                              |
| Record actions (log format)  | Actions you take are optionally recorded or logged for future scripting      |
| Future folder enhancement    | (Planned) Navigate to or auto-create a folder for each month/year            |

---

## 🔐 Security Considerations

- Your credentials and tokens are never accessed by the script
- All sensitive navigation and actions are done manually in your secure browser context

---

## 🚫 Out of Scope (for this version)

- Automating creation of Google Sheets or Drive folders
- Manipulating spreadsheet contents
- API or database connections

---

## 🧑‍💻 Technical Requirements

- **Language:** Node.js (TypeScript preferred)
- **Framework:** Playwright
- **Chrome Executable Path:** Uses local Chrome installation
- **User Data Directory:** Your active Chrome profile path
- **Initial Navigation URL:** `https://drive.google.com/drive/my-drive`

```ts
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launchPersistentContext(
    '/Users/YOURNAME/Library/Application Support/Google/Chrome/Default',
    {
      headless: false,
      executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    }
  );
  const page = await browser.newPage();
  await page.goto('https://drive.google.com/drive/my-drive');
})();