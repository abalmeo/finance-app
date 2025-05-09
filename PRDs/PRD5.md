Ok i'm moving back to the idea of a hybrid automated/manual app (is that even a thing or would it be considered manual still... lol?)|

Ok what I will do manually:
- Export a CSV

What I expect the app to do
- using something that can work with csv's.
- Categorize each financial transaction by the different account. I think this part I'll need to do some manual updating on. So can you create this in a way where I can easily update the code in case I need to update the categorizations
- After categorized, move this into different sheets. I want to work with excel since that seems like it doesn't require authentication

Is this possible?


# 🧾 Finance Categorization App (Hybrid Automation – MVP v0.5)

This version introduces a semi-automated app that starts with a manual CSV export. The app will automatically categorize financial transactions based on account type and organize them into separate Excel sheets — with easy-to-update categorization logic.

---

## 📌 Objective

Automate the categorization and organization of manually exported CSV transaction files, and output a formatted Excel file with each account’s transactions on separate sheets.

---

## 🛠 Scope (MVP v0.5)

### ✅ What You’ll Do Manually:
- Log in to your bank or finance site (e.g., Monarch, Amex, Chase)
- Export your financial data as a CSV file and place it in the `/input` directory

### ✅ What the App Will Do:
- Load the exported CSV
- Categorize each transaction by account or description
- Output an Excel `.xlsx` file with multiple sheets (one per account/category)
- Provide a config file or function where categorization rules can be easily updated

---

## ✨ Features

| Feature                       | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| CSV ingestion                 | Load and parse exported transaction CSVs                                    |
| Categorization logic          | Tag each row based on rules (e.g., account name, vendor keyword, amount)   |
| Easy-to-edit rules section    | Categorization logic stored in a separate file or function for quick edits |
| Excel export with sheets      | Write categorized data into multiple sheets within a single `.xlsx` file   |
| Offline-first                 | No cloud dependencies; runs locally with no auth required                  |

---

## 🧑‍💻 Technical Requirements

- **Language:** Python
- **Libraries:** `pandas`, `openpyxl`
- **Input Format:** `.csv`
- **Output Format:** `.xlsx`
- **Editable Config:** Categorization logic lives in `config/categories.py` or directly in `categorize.py`

---

## 📁 Example Directory Structure
---
finance-categorizer/
├── categorize.py
├── input/
│   └── transactions.csv
├── output/
│   └── categorized_finances.xlsx
├── config/
│   └── categories.py  # Editable mapping logic (e.g., account → filter rules)

## ✅ Success Criteria

- The app can load and parse the CSV file
- Each transaction is categorized correctly using flexible rules
- Output Excel file is generated with one sheet per category/account
- The categorization logic is easy to update as needed

---

## 🪜 Next Steps

- Enhance categorization with regex or NLP to group similar vendors
- Support merging multiple monthly CSVs for longer-term tracking
- Add charts/visuals (e.g., monthly spend by category)
- Build a GUI or CLI to select CSVs and run the process
- Add logic to detect duplicate transactions across files

---

> Created by Alvin Balmeo – May 2025