# 🧾 Finance Automation Agent (MVP v0.1)

A simple automation script that uses [Playwright](https://playwright.dev/) to open a browser and navigate to a financial website. This is the first step toward automating manual finance tasks like downloading statements and organizing them.

---

## 📌 Objective

Use Playwright to automate launching a browser and navigating to a specific financial website. This MVP will validate basic browser automation capabilities.

---

## 🛠 Scope (MVP v0.1)

- Launch a Chromium browser instance using Playwright
- Navigate to a specified URL (e.g., `https://www.capitalone.com`)
- Log success or failure of page load

---

## ✨ Features

| Feature               | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| Launch browser        | Use Playwright to open a Chromium instance                                  |
| Navigate to URL       | Open a pre-defined website                                                  |
| Headless toggle       | Run headless or with UI (configurable via `.env` or CLI flags)              |
| Log page title        | Output the page title for visual confirmation                               |
| Error handling        | Gracefully log errors if navigation fails                                   |

---

## 🚫 Out of Scope (for this version)

- Logging into the website  
- Interacting with page elements  
- Downloading CSVs or categorizing financial data  
- Google Sheets or database integration  

These will be added in future versions.

---

## 🧑‍💻 Technical Requirements

- **Language:** Node.js (JavaScript or TypeScript)
- **Framework:** Playwright
- **Browser:** Chromium
- **Configuration:** URL can be set via `.env` or passed in as a command-line argument

---

## ✅ Success Criteria

- Browser successfully launches and navigates to the specified URL
- Page title is printed to the console
- No unhandled exceptions or crashes

---

## 🪜 Next Steps

- Add login automation
- Download CSVs from each bank site
- Clean and categorize data
- Push to Google Sheets or a database

---

> Created by Alvin Balmeo – May 2025 (riight...lol -> Open AI)