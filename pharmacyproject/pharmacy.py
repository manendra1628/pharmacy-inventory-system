import csv
import os

FILENAME = "medicines.csv"


# 1. CSV file se medicines load karne ka function
def load_medicines():
  medicines = []
  if not os.path.exists(FILENAME):
    return medicines
  with open(FILENAME, mode="r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
      medicines.append({
          "ID": row["ID"],
          "Name": row["Name"],
          "Quantity": int(row["Quantity"]),
          "Price": float(row["Price"]),
      })
  return medicines


# 2. Changes ko wapas CSV file me save karne ka function
def save_medicines(medicines):
  with open(FILENAME, mode="w", newline="") as file:
    fieldnames = ["ID", "Name", "Quantity", "Price"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for med in medicines:
      writer.writerow(med)


# 3. Nayi medicine add karne ka function
def add_medicine(medicines):
  med_id = f"M{len(medicines) + 1}"
  name = input("Enter Medicine Name: ").strip()

  try:
    qty = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))
    if qty < 0 or price < 0:
      print("Error: Quantity and Price cannot be negative!")
      return
  except ValueError:
    print("Error: Please enter valid numbers.")
    return

  medicines.append(
      {"ID": med_id, "Name": name, "Quantity": qty, "Price": price}
  )
  save_medicines(medicines)
  print(
      f"Medicine added. ID: {med_id} | {name} | Qty: {qty} | Price:"
      f" {price:.2f}"
  )


# 4. Stock dekhne ka function
def view_stock(medicines):
  print("\n--- Current Inventory ---")
  for med in medicines:
    status = " (Low stock)" if med["Quantity"] < 10 else ""
    print(
        f"ID: {med['ID']} | Name: {med['Name']} | Qty: {med['Quantity']} |"
        f" Price: {med['Price']:.2f}{status}"
    )


# 5. Medicine bechne (Sell) karne ka function
def sell_medicine(medicines):
  med_id = input("Enter Medicine ID to sell (e.g., M1): ").strip()
  target = None
  for med in medicines:
    if med["ID"] == med_id:
      target = med
      break

  if not target:
    print("Error: Medicine ID not found!")
    return

  try:
    qty_to_sell = int(input("Enter Quantity to sell: "))
    if qty_to_sell < 0:
      print("Error: Quantity cannot be negative!")
      return
  except ValueError:
    print("Error: Please enter a valid number.")
    return

  if qty_to_sell > target["Quantity"]:
    print(f"Insufficient stock. Available: {target['Quantity']}")
    return

  target["Quantity"] -= qty_to_sell
  bill = qty_to_sell * target["Price"]
  save_medicines(medicines)

  print(f"Sold {qty_to_sell} units. Bill: {bill:.2f}")
  print(f"Stock left: {target['Quantity']} | Out of stock!")


# 6. Medicine delete karne ka function
def delete_medicine(medicines):
  med_id = input("Enter Medicine ID to delete (e.g., M3): ").strip()
  found = False
  for med in medicines:
    if med["ID"] == med_id:
      medicines.remove(med)
      found = True
      break

  if found:
    save_medicines(medicines)
    print(f"Medicine {med_id} deleted.")
  else:
    print("Error: Medicine ID not found!")


# 7. Low stock report dikhane ka function
def low_stock_report(medicines):
  print("\n--- Low Stock Report (Qty < 10) ---")
  count = 0
  for med in medicines:
    if med["Quantity"] < 10:
      print(
          f"({chr(97 + count)}) {med['ID']} | {med['Name']} | Qty:"
          f" {med['Quantity']} (Low stock)"
      )
      count += 1
  if count == 0:
    print("No low stock medicines.")


# 8. Total inventory value nikalne ka function
def total_inventory_value(medicines):
  total = sum(med["Quantity"] * med["Price"] for med in medicines)
  print(f"(c) Total inventory value: {total:.2f}")


# Main Menu jo screen par dikhega
def main():
  medicines = load_medicines()
  while True:
    print("\n=== Pharmacy Inventory System ===")
    print("1. Add Medicine")
    print("2. View Stock")
    print("3. Sell Medicine")
    print("4. Delete Medicine")
    print("5. Low Stock Report")
    print("6. Total Inventory Value")
    print("7. Exit")

    choice = input("Enter your menu option (1-7): ").strip()

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
      total_inventory_value(medicines)
    elif choice == "7":
      print("Exiting program. Goodbye!")
      break
    else:
      print("Invalid option! Please choose between 1 to 7.")


if __name__ == "__main__":
  main()