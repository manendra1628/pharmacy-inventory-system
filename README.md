# Pharmacy Inventory System (PS No. 69)

## Project Overview
A console-based Python application designed to manage a pharmacy's medicine stock efficiently. It handles adding medicines, viewing inventory, selling items, deleting records, checking low-stock reports, and calculating total inventory value using CSV file storage.

## Features
- **Add Medicine:** Add new medicines with automatic ID assignment (M1, M2, etc.).
- **View Stock:** View all available medicines with real-time low-stock indicators.
- **Sell Medicine:** Sell stock, automatically update quantities, and generate bills.
- **Delete Medicine:** Remove discontinued or unwanted medicine records.
- **Low Stock Report:** Filter and display medicines with a quantity below 10.
- **Inventory Value Calculation:** Calculate the total financial worth of the current stock.

## Technologies Used
- **Language:** Python 3
- **Data Storage:** CSV File (`medicines.csv`)
- **Concepts Applied:** Dictionaries, Lists, File Handling, CRUD Operations, Functions

## How to Run
1. Ensure Python 3 is installed on your system.
2. Place `pharmacy.py` and `medicines.csv` in the same folder.
3. Open a terminal in that folder and run:
   ```bash
   python pharmacy.py
