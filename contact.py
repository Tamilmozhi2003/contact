contacts = {}
def show_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
def add_contact():
    name = input("Enter contact name: ")
    if name in contacts:
        print(f"Contact for {name} already exists!")
    else:
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        address = input("Enter contact address: ")
        
        contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print(f"Contact for {name} added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("\nContact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")

def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found = False
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term in details['phone']:
            print(f"Found: Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
            found = True
    if not found:
        print("No contact found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print(f"Current details for {name}: {contacts[name]}")
        phone = input("Enter new phone number: ")
        email = input("Enter new email address: ")
        address = input("Enter new address: ")
        
        contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print(f"Contact for {name} updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact for {name} deleted successfully!")
    else:
        print("Contact not found.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()