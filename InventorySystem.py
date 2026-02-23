import sqlite3

# Connect to database
conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    location TEXT NOT NULL
)
""")
conn.commit()


def add_item():
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    location = input("Enter location: ")

    cursor.execute(
        "INSERT INTO inventory (item_name, quantity, location) VALUES (?, ?, ?)",
        (name, quantity, location)
    )
    conn.commit()
    print("Item added successfully.\n")


def view_items():
    cursor.execute("SELECT * FROM inventory")
    items = cursor.fetchall()

    if not items:
        print("No inventory records found.\n")
        return

    print("\nInventory Records:")
    for item in items:
        print(f"ID: {item[0]}, Name: {item[1]}, Quantity: {item[2]}, Location: {item[3]}")
    print()


def update_quantity():
    item_id = int(input("Enter item ID to update: "))
    new_quantity = int(input("Enter new quantity: "))

    cursor.execute(
        "UPDATE inventory SET quantity = ? WHERE id = ?",
        (new_quantity, item_id)
    )
    conn.commit()
    print("Quantity updated successfully.\n")


def delete_item():
    item_id = int(input("Enter item ID to delete: "))
    cursor.execute("DELETE FROM inventory WHERE id = ?", (item_id,))
    conn.commit()
    print("Item deleted successfully.\n")


def menu():
    while True:
        print("1. Add Item")
        print("2. View Items")
        print("3. Update Quantity")
        print("4. Delete Item")
        print("5. Exit")

        choice = input("Select option: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            view_items()
        elif choice == "3":
            update_quantity()
        elif choice == "4":
            delete_item()
        elif choice == "5":
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    menu()
    conn.close()