import tkinter as tk
from tkinter import messagebox
class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("400x400")
        self.contacts = {}

        # Set up the GUI
        self.setup_ui()

    def setup_ui(self):
        # Define colors
        bg_color = "#f0f8ff"
        btn_color = "#ff6347"
        entry_color = "#fffacd"
        label_color = "#4682b4"

        # Set background color
        self.root.config(bg=bg_color)

        # Add Contact Section
        tk.Label(self.root, text="Add Contact", font=("Arial", 14), bg=bg_color, fg=label_color).pack(pady=10)
        tk.Label(self.root, text="Name:", bg=bg_color, fg=label_color).pack()
        self.name_entry = tk.Entry(self.root, bg=entry_color)
        self.name_entry.pack()
        tk.Label(self.root, text="Phone:", bg=bg_color, fg=label_color).pack()
        self.phone_entry = tk.Entry(self.root, bg=entry_color)
        self.phone_entry.pack()
        tk.Button(self.root, text="Add Contact", command=self.add_contact, bg=btn_color, fg="white").pack(pady=5)

        # View Contacts Section
        tk.Button(self.root, text="View Contacts", command=self.view_contacts, bg=btn_color, fg="white").pack(pady=5)

        # Search Contact Section
        tk.Label(self.root, text="Search Contact", font=("Arial", 14), bg=bg_color, fg=label_color).pack(pady=10)
        tk.Label(self.root, text="Name:", bg=bg_color, fg=label_color).pack()
        self.search_entry = tk.Entry(self.root, bg=entry_color)
        self.search_entry.pack()
        tk.Button(self.root, text="Search", command=self.search_contact, bg=btn_color, fg="white").pack(pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name and phone:
            self.contacts[name] = phone
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            messagebox.showinfo("Contact Book", "Contact added successfully!")
        else:
            messagebox.showwarning("Input Error", "Please enter both name and phone number.")

    def view_contacts(self):
        contacts_list = "\n".join([f"{name}: {phone}" for name, phone in self.contacts.items()])
        if contacts_list:
            messagebox.showinfo("Contact Book", contacts_list)
        else:
            messagebox.showinfo("Contact Book", "No contacts available.")

    def search_contact(self):
        name = self.search_entry.get()
        phone = self.contacts.get(name)
        if phone:
            messagebox.showinfo("Contact Book", f"{name}: {phone}")
        else:
            messagebox.showinfo("Contact Book", "Contact not found.")

# Create the main window
root = tk.Tk()
app = ContactBookApp(root)
root.mainloop()
