import tkinter as tk
from tkinter import messagebox
import csv

# Function to display the menu using Tkinter
def display_menu():
    root = tk.Tk()
    root.title("Sliderz Station Menu")

    menu_lst = [
        ['Sl', 'ItemName', 'ItemNo:', 'Price(INR)'],
        [1, "Delta X Fries", '010', 200.00],
        [2, "Smoked Turkish Beef", '020', 200.00],
        [3, "Chicken Delight Slider", "130", 100.00],
        [4, "Classic Chicken Slider", "213", 200.00]
    ]

    table = tk.Label(root, text="MENU", font=('Helvetica', 16, 'bold'))
    table.grid(row=0, column=0, columnspan=4)

    for i, header in enumerate(menu_lst[0]):
        label = tk.Label(root, text=header)
        label.grid(row=1, column=i)

    for i, row in enumerate(menu_lst[1:], start=2):
        for j, item in enumerate(row):
            label = tk.Label(root, text=item)
            label.grid(row=i, column=j)

    root.mainloop()

# Call the function to display the menu
display_menu()
# Function to create a customer account
import tkinter as tk
from tkinter import messagebox

# Simulated customer data
customer_data = []

# Simulated menu data
menu_items = {
    '010': "Delta X Fries",
    '020': "Smoked Turkish Beef",
    '130': "Chicken Delight Slider",
    '213': "Classic Chicken Slider"
}

# Function to create a customer account and save data to a CSV file
def create_account():
    root = tk.Tk()
    root.title("Create Customer Account")

    # Labels and Entry fields for user information
    labels = ['Customer ID:', 'First Name:', 'Last Name:', 'Address:', 'Item No:', 'Quantity:']
    entries = []
    
    for i, label_text in enumerate(labels):
        label = tk.Label(root, text=label_text)
        label.grid(row=i, column=0, sticky='w')
        
        entry = tk.Entry(root)
        entry.grid(row=i, column=1)
        entries.append(entry)
    
    def submit():
        user_data = [entry.get() for entry in entries]
        
        # Verify Item Number from menu_items
        item_no = user_data[4]
        if item_no not in menu_items:
            messagebox.showerror("Error", "Invalid Item Number. Please enter a valid Item No.")
            return

        # Here, you can process the user data and store it in your system
        # For example, print the collected data
        print("User Data:", user_data)
        
        # Save data to a CSV file
        with open('customer_data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(user_data)

        messagebox.showinfo("Success", "Account Created Successfully!")
        root.destroy()

    submit_button = tk.Button(root, text="Submit", command=submit)
    submit_button.grid(row=len(labels), columnspan=2)

    root.mainloop()

# Call the function to create a customer account
create_account()

# Function to search for a customer account

# Function to search for a customer account
def search_account():
    def display_result():
        id_to_search = entry.get()
        found = False
        result_text = ""
        with open('customer_data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == id_to_search:
                    result_text += f"Customer ID: {row[0]}\n"
                    result_text += f"First Name: {row[1]}\n"
                    result_text += f"Last Name: {row[2]}\n"
                    result_text += f"Address: {row[3]}\n"
                    result_text += f"Item No: {row[4]}\n"
                    result_text += f"Quantity: {row[5]}\n\n"
                    found = True
                    break

        if found:
            result_label.config(text=result_text)
        else:
            result_label.config(text="Customer not found.")

    root = tk.Tk()
    root.title("Search Customer Account")

    label = tk.Label(root, text="Enter Customer ID:")
    label.grid(row=0, column=0)

    entry = tk.Entry(root)
    entry.grid(row=0, column=1)

    search_button = tk.Button(root, text="Search", command=display_result)
    search_button.grid(row=0, column=2)

    result_label = tk.Label(root, text="")
    result_label.grid(row=1, columnspan=3)

    root.mainloop()

# Call the function to search for a customer account
search_account()
# Function to generate a bill for a customer
def generate_bill():
    def display_bill():
        id_to_generate = entry.get()
        bill_content = ""
        with open('customer_data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == id_to_generate:
                    bill_content += "--------------------------------------\n"
                    bill_content += "           SLIDERZ STATION\n"
                    bill_content += "--------------------------------------\n"
                    bill_content += f"Customer ID: {row[0]}\n"
                    bill_content += f"Name: {row[1]} {row[2]}\n"
                    bill_content += f"Address: {row[3]}\n"
                    bill_content += "--------------------------------------\n"
                    bill_content += "          BILLING INFORMATION\n"
                    bill_content += "--------------------------------------\n"
                    bill_content += f"Item No: {row[4]}\n"
                    bill_content += f"Quantity: {row[5]}\n"
                    bill_content += "--------------------------------------\n"
                    bill_content += "               THANK YOU!\n"
                    bill_content += "--------------------------------------\n"

                    display_window = tk.Toplevel(root)
                    display_window.title("Bill")
                    bill_label = tk.Label(display_window, text=bill_content, justify=tk.LEFT)
                    bill_label.pack()
                    messagebox.showinfo("Bill Generated", "Bill has been displayed in a new window.")
                    return

        messagebox.showwarning("Customer not found", "Customer ID not found.")

    root = tk.Tk()
    root.title("Generate Bill")

    label = tk.Label(root, text="Enter Customer ID:")
    label.grid(row=0, column=0)

    entry = tk.Entry(root)
    entry.grid(row=0, column=1)

    generate_button = tk.Button(root, text="Generate Bill", command=display_bill)
    generate_button.grid(row=0, column=2)

    root.mainloop()

# Call the function to generate a bill for a customer
generate_bill()
# Function to delete a customer account
def delete_customer_account(customer_id):
    confirmation = messagebox.askyesno("Confirmation", f"Do you want to delete Customer ID: {customer_id}?")
    if confirmation:
        rows_to_keep = []
        with open('customer_data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] != customer_id:
                    rows_to_keep.append(row)

        with open('customer_data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows_to_keep)

        messagebox.showinfo("Account Deleted", f"Customer ID {customer_id} deleted successfully.")
        display_customer_ids()

# Function to display all customer IDs and allow deletion
def display_customer_ids():
    root = tk.Tk()
    root.title("Delete Customer Account")

    with open('customer_data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            customer_id = row[0]
            delete_button = tk.Button(root, text=f"Delete ID: {customer_id}", command=lambda id=customer_id: delete_customer_account(id))
            delete_button.pack()

    root.mainloop()

# Call the function to display customer IDs for deletion
display_customer_ids()
def menu_choice(choice):
    if choice == 1:
        create_account()
    elif choice == 2:
        search_account()
    elif choice == 3:
        display_customer_ids()
    elif choice == 4:
        generate_bill()
    elif choice == 5:
        # Add your code to call other functions as needed
        pass
def main_menu():
    root = tk.Tk()
    root.title("Customer Management")

    label = tk.Label(root, text="Select an option:")
    label.pack()

    var = tk.IntVar()

    options = [
        ("Create Account", 1),
        ("Search Account", 2),
        ("Delete Account", 3),
        ("Generate Bill", 4),
        # Add more options as needed
    ]

    for text, value in options:
        tk.Radiobutton(root, text=text, variable=var, value=value).pack()

    submit_button = tk.Button(root, text="Submit", command=lambda: menu_choice(var.get()))
    submit_button.pack()

    root.mainloop()

main_menu()
