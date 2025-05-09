Next Prompt:

Ok this works now, and this is where I want to take over to input the sign in details since this is risky stuff.  I don’t want to give playwright access to my secrets

I'll manually sign in, where it then takes you to the browser. I use secretbank, once i sign in manually. I want the next steps to be waiting until the browser refreshes, and I now want to select ui elements to navigate to the correct page where I can export a csv

# 🧾 Finance Automation Agent (MVP v0.2)

This version builds on the initial browser automation, allowing manual login and then resuming automation to download CSVs from Monarch Money.

---

## 📌 Objective

After you manually log into Monarch Money (for security reasons), the script will wait until you're authenticated, then continue automating browser actions to export your financial transaction CSV.

---

## 🛠 Scope (MVP v0.2)

- Pause until login is manually completed
- Detect when the browser has transitioned to the authenticated state
- Navigate to the transactions or export page
- Select UI elements required to access export functionality
- Trigger CSV export/download

---

## ✨ Features

| Feature                 | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| Wait for login          | Pause automation until post-login state is detected (e.g., specific URL or element) |
| DOM detection           | Detect specific elements to confirm successful login                        |
| Navigate to export page | Automate clicks to reach CSV export section                                 |
| Initiate export         | Click export/download button to retrieve CSV                                |
| Log status              | Output confirmation or errors for each step                                 |

---

## 🔐 Security Considerations

- **No credentials stored or used in automation**
- Manual login is required before automation resumes
- Secrets and login steps are completely handled by the user

---

## 🚫 Out of Scope (for this version)

- Logging in or handling 2FA
- Reading or transforming the CSV data
- Sending data to Google Sheets or any backend

---

## 🧑‍💻 Technical Requirements

- **Language:** Node.js (TypeScript preferred)
- **Framework:** Playwright
- **Browser:** Chromium
- **Login Detection:** Wait for a specific DOM element or URL
- **Navigation:** Use `page.locator()` and other Playwright APIs to click through
- **Download Handling:** Save CSV to a local `./exports` directory

---

## ✅ Success Criteria

- Script pauses until login is complete
- Navigates to the correct export section without manual clicks
- CSV downloads successfully to the local system
- Console output reflects success/failure of each step

---

## 🪜 Next Steps

- Parse and clean downloaded CSV
- Categorize by account or transaction type
- Push processed data to Google Sheets or a database

---

> Created by Alvin Balmeo – May 2025