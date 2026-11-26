import csv
import os

CSV_FILE = "medicines.csv"
FIELDNAMES = ["ID", "Name", "Quantity", "Price"]


def load_medicines():
    """Load medicines from medicines.csv into a list of dictionaries."""
    medicines = []
    if not os.path.exists(CSV_FILE):
        return medicines

    with open(CSV_FILE, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if not row or not row.get("ID"):
                continue
            medicines.append({
                "ID": row["ID"].strip(),
                "Name": row["Name"].strip(),
                "Quantity": int(row["Quantity"]),
                "Price": float(row["Price"])
            })
    return medicines


def save_medicines(medicines):
    """Write the list of medicine dictionaries back to medicines.csv."""
    with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        for med in medicines:
            writer.writerow({
                "ID": med["ID"],
                "Name": med["Name"],
                "Quantity": med["Quantity"],
                "Price": f"{med['Price']:.2f}"
            })


def generate_next_id(medicines):
    """Generate the next sequential Medicine ID starting from M1."""
    if not medicines:
        return "M1"
    nums = [int(med["ID"][1:]) for med in medicines if med["ID"].startswith("M") and med["ID"][1:].isdigit()]
    max_num = max(nums) if nums else 0
    return f"M{max_num + 1}"


def add_medicine(medicines):
    """Option 1: Add a new medicine to the inventory."""
    name = input("Enter Medicine Name: ").strip()
    if not name:
        print("Invalid input. Medicine name cannot be empty.")
        return

    try:
        quantity = int(input("Enter Quantity: "))
        price = float(input("Enter Price: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for quantity and price.")
        return

    if quantity < 0 or price < 0:
        print("Invalid input. Quantity and price cannot be negative.")
        return

    med_id = generate_next_id(medicines)
    new_med = {
        "ID": med_id,
        "Name": name,
        "Quantity": quantity,
        "Price": price
    }
    medicines.append(new_med)
    save_medicines(medicines)
    print(f"Medicine added. ID: {med_id} | {name} | Qty: {quantity} | Price: {price:.2f}")


def view_stock(medicines):
    """Option 2: Display all medicines currently in stock."""
    if not medicines:
        print("Inventory is empty.")
        return

    print("\n--- Current Pharmacy Stock ---")
    print(f"{'ID':<6} | {'Name':<20} | {'Qty':<6} | {'Price':<8} | Status")
    print("-" * 62)
    for med in medicines:
        if med["Quantity"] == 0:
            status = "Out of stock!"
        elif med["Quantity"] < 10:
            status = "Low stock"
        else:
            status = "In stock"
        print(f"{med['ID']:<6} | {med['Name']:<20} | {med['Quantity']:<6} | {med['Price']:<8.2f} | {status}")


def sell_medicine(medicines):
    """Option 3: Sell a medicine, calculate the bill, and update stock."""
    med_id = input("Enter Medicine ID to sell: ").strip().upper()
    med = next((m for m in medicines if m["ID"].upper() == med_id), None)

    if not med:
        print(f"Medicine {med_id} not found.")
        return

    try:
        sell_qty = int(input("Enter Quantity to sell: "))
    except ValueError:
        print("Invalid input. Quantity must be a whole number.")
        return

    if sell_qty <= 0:
        print("Invalid input. Quantity to sell must be greater than zero.")
        return

    if sell_qty > med["Quantity"]:
        print(f"Insufficient stock. Available: {med['Quantity']}")
        return

    bill = sell_qty * med["Price"]
    med["Quantity"] -= sell_qty
    save_medicines(medicines)

    print(f"Sold {sell_qty} units. Bill: {bill:.2f}")
    if med["Quantity"] == 0:
        print("Stock left: 0 | Out of stock!")
    elif med["Quantity"] < 10:
        print(f"Stock left: {med['Quantity']} | Low stock")
    else:
        print(f"Stock left: {med['Quantity']}")


def delete_medicine(medicines):
    """Option 4: Delete a medicine from the inventory by ID."""
    med_id = input("Enter Medicine ID to delete: ").strip().upper()
    for i, med in enumerate(medicines):
        if med["ID"].upper() == med_id:
            medicines.pop(i)
            save_medicines(medicines)
            print(f"Medicine {med['ID']} deleted.")
            return

    print(f"Medicine {med_id} not found.")


def low_stock_report(medicines):
    """Option 5: Display all medicines with quantity below 10."""
    low_stock_items = [med for med in medicines if med["Quantity"] < 10]
    if not low_stock_items:
        print("No low-stock medicines found.")
        return

    for med in low_stock_items:
        print(f"{med['ID']} | {med['Name']} | Qty: {med['Quantity']} (Low stock)")


def inventory_value(medicines):
    """Option 6: Calculate and display the total value of all stock."""
    total_value = sum(med["Quantity"] * med["Price"] for med in medicines)
    print(f"Total inventory value: {total_value:.2f}")


def main():
    medicines = load_medicines()

    while True:
        print("\n=== Pharmacy Inventory System ===")
        print("1. Add Medicine")
        print("2. View Stock")
        print("3. Sell Medicine")
        print("4. Delete Medicine")
        print("5. Low Stock Report")
        print("6. Inventory Value")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_medicine(medicines)
        elif choice == "2":
            view_stock(medicines)
        elif choice == "3":
            sell_medicine(medicines)
        elif choice == "4":
            delete_medicine(medicines)
        elif choice == "5":
            low_stock_report(medicines)
        elif choice == "6":
            inventory_value(medicines)
        elif choice == "7":
            print("Exiting Pharmacy Inventory System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select an option from 1 to 7.")


if __name__ == "__main__":
    main()