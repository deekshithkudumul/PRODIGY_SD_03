import json
import tkinter as tk
from tkinter import ttk, messagebox

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
def get_phone_number(phone):
    if phone.isdigit():
        return True
    else:
        return False

# Add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get() or "N/A"
    
    if not name or not phone:
        messagebox.showerror("Error", "Name and phone number are required.")
        return
    
    if not get_phone_number(phone):
        messagebox.showerror("Error", "Invalid phone number. Please enter only numbers.")
        return
    
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    messagebox.showinfo("Success", "Contact added successfully!")
    refresh_contacts()

# View all contacts
def view_contacts():
    for row in tree.get_children():
        tree.delete(row)
    for contact in contacts:
        tree.insert('', 'end', values=(contact['name'], contact['phone'], contact['email']))

# Edit an existing contact
def edit_contact():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "Please select a contact to edit.")
        return
    
    for item in selected_item:
        contact = tree.item(item, 'values')
        name = contact[0]
        phone = contact[1]
        email = contact[2]
        
        name_entry.delete(0, tk.END)
        name_entry.insert(0, name)
        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, phone)
        email_entry.delete(0, tk.END)
        email_entry.insert(0, email)
    
    def save_edit():
        edited_name = name_entry.get()
        edited_phone = phone_entry.get()
        edited_email = email_entry.get() or "N/A"
        
        if not edited_name or not edited_phone:
            messagebox.showerror("Error", "Name and phone number are required.")
            return
        
        if not get_phone_number(edited_phone):
            messagebox.showerror("Error", "Invalid phone number. Please enter only numbers.")
            return
        
        for contact in contacts:
            if contact['name'] == name:
                contact['name'] = edited_name
                contact['phone'] = edited_phone
                contact['email'] = edited_email
                break
        
        save_contacts(contacts)
        messagebox.showinfo("Success", "Contact updated successfully!")
        refresh_contacts()
        save_button.destroy()
    
    save_button = tk.Button(root, text="Save Edit", command=save_edit)
    save_button.grid(row=5, column=0, columnspan=2, pady=5)

# Delete a contact
def delete_contact():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "Please select a contact to delete.")
        return
    
    for item in selected_item:
        contact = tree.item(item, 'values')
        name = contact[0]
        
        for contact in contacts:
            if contact['name'] == name:
                contacts.remove(contact)
                break
    
    save_contacts(contacts)
    messagebox.showinfo("Success", "Contact deleted successfully!")
    refresh_contacts()

# Refresh the contact list
def refresh_contacts():
    for row in tree.get_children():
        tree.delete(row)
    view_contacts()

# Load contacts
contacts = load_contacts()

# Create the main window
root = tk.Tk()
root.title("Contact Management System")

# Create and place the Name entry
name_label = ttk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry = ttk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

# Create and place the Phone entry
phone_label = ttk.Label(root, text="Phone:")
phone_label.grid(row=1, column=0, padx=10, pady=5)
phone_entry = ttk.Entry(root)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

# Create and place the Email entry
email_label = ttk.Label(root, text="Email (optional):")
email_label.grid(row=2, column=0, padx=10, pady=5)
email_entry = ttk.Entry(root)
email_entry.grid(row=2, column=1, padx=10, pady=5)

# Create and place the Add button
add_button = ttk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=3, column=0, columnspan=2, pady=5)

# Create and place the Edit button
edit_button = ttk.Button(root, text="Edit Contact", command=edit_contact)
edit_button.grid(row=4, column=0, pady=5)

# Create and place the Delete button
delete_button = ttk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.grid(row=4, column=1, pady=5)

# Create and place the Treeview
columns = ('Name', 'Phone', 'Email')
tree = ttk.Treeview(root, columns=columns, show='headings')
tree.heading('Name', text='Name')
tree.heading('Phone', text='Phone')
tree.heading('Email', text='Email')
tree.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# View contacts on startup
view_contacts()

# Run the application
root.mainloop()
