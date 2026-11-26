# Pharmacy Inventory System (PS No. 69)

A console-based Python application to manage a pharmacy's medicine stock. It supports full CRUD operations, automated billing, low-stock alerts, and total inventory valuation using persistent CSV storage (`medicines.csv`).

## Features
- **Add Medicine:** Automatically generates sequential IDs starting from `M1` and validates against negative quantity or price.
- **View Stock:** Displays all medicines in a structured table with real-time stock status (`In stock`, `Low stock`, `Out of stock!`).
- **Sell Medicine:** Validates available stock, calculates the total bill (`Quantity × Price`), and updates `medicines.csv` immediately.
- **Delete Medicine:** Removes a medicine record by its ID.
- **Low Stock Report:** Lists all medicines with a quantity below `10`.
- **Inventory Value:** Calculates the total monetary value of all medicines currently in stock.

## Concepts Used
- Python 3
- Lists & Dictionaries
- CSV File Handling (`csv.DictReader`, `csv.DictWriter`)
- Modular Functions & CRUD Operations
- Input Validation & Error Handling

## Project Structure
```text
pharmacyproject/
├── medicines.csv
├── pharmacy.py
└── README.md
