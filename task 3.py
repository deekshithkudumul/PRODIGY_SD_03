import json

# Load contacts from a file
def load_contacts(filename='contacts.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save contacts to a file
def save_contacts(contacts, filename='contacts.json'):
    with open(filename, 'w') as file:
        json.dump(contacts, file, indent=4)

# Validate phone number input
def get_phone_number():
    while True:
        phone = input("Enter phone number: ")
        if phone.isdigit():
            return phone
        else:
            print("Invalid input. Please enter only numbers.")

# Add a new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = get_phone_number()
    email = input("Enter email address (optional): ")
    contacts.append({"name": name, "phone": phone, "email": email if email else "N/A"})
    save_contacts(contacts)
    print("Contact added successfully!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

# Edit an existing contact
def edit_contact(contacts):
    name = input("Enter the name of the contact to edit: ")
    for contact in contacts:
        if contact['name'] == name:
            contact['phone'] = get_phone_number()
            email = input("Enter new email address (optional): ")
            contact['email'] = email if email else "N/A"
            save_contacts(contacts)
            print("Contact updated successfully!")
            return
    print("Contact not found.")

# Delete a contact
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

# Main menu
def main():
    contacts = load_contacts()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
