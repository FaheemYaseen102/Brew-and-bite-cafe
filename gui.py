import tkinter as tk
from tkinter import ttk, messagebox
from utils import (
    register_user, update_user, delete_user,
    record_expense, view_expenses,
    add_inventory_item, update_inventory_item, delete_inventory_item, view_inventory,
    record_sale, view_sales, generate_financial_reports, session, User
)


def view_users():
    pass


def main():
    root = tk.Tk()
    root.title("Expense Tracking System")
    root.geometry("800x600")

    # Notebook for tabbed navigation
    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill="both")

    user_tab = ttk.Frame(notebook)
    expense_tab = ttk.Frame(notebook)
    inventory_tab = ttk.Frame(notebook)
    sales_tab = ttk.Frame(notebook)
    reports_tab = ttk.Frame(notebook)

    notebook.add(user_tab, text="User Management")
    notebook.add(expense_tab, text="Expense Management")
    notebook.add(inventory_tab, text="Inventory Management")
    notebook.add(sales_tab, text="Sales Tracking")
    notebook.add(reports_tab, text="Reports")

    # User Management
    def register_user_ui():
        def submit():
            username = username_entry.get()
            password = password_entry.get()
            email = email_entry.get()
            register_user(username, password, email)
            messagebox.showinfo("Success", "User registered successfully!")

        for widget in user_tab.winfo_children():
            widget.destroy()

        tk.Label(user_tab, text="Register User", font=("Arial", 14)).pack(pady=10)

        tk.Label(user_tab, text="Username:").pack()
        username_entry = tk.Entry(user_tab)
        username_entry.pack()

        tk.Label(user_tab, text="Password:").pack()
        password_entry = tk.Entry(user_tab, show="*")
        password_entry.pack()

        tk.Label(user_tab, text="Email:").pack()
        email_entry = tk.Entry(user_tab)
        email_entry.pack()

        tk.Button(user_tab, text="Register", command=submit).pack(pady=10)
        tk.Button(user_tab, text="Back", command=lambda: display_main_ui()).pack(pady=10)

    def update_user_ui():
        def submit():
            user_id = user_id_entry.get()
            username = username_entry.get()
            password = password_entry.get()
            email = email_entry.get()
            update_user(user_id, username, password, email)
            messagebox.showinfo("Success", "User information updated successfully!")

        for widget in user_tab.winfo_children():
            widget.destroy()

        tk.Label(user_tab, text="Update User Information", font=("Arial", 14)).pack(pady=10)

        tk.Label(user_tab, text="User ID:").pack()
        user_id_entry = tk.Entry(user_tab)
        user_id_entry.pack()

        tk.Label(user_tab, text="Username:").pack()
        username_entry = tk.Entry(user_tab)
        username_entry.pack()

        tk.Label(user_tab, text="Password:").pack()
        password_entry = tk.Entry(user_tab, show="*")
        password_entry.pack()

        tk.Label(user_tab, text="Email:").pack()
        email_entry = tk.Entry(user_tab)
        email_entry.pack()

        tk.Button(user_tab, text="Update", command=submit).pack(pady=10)
        tk.Button(user_tab, text="Back", command=lambda: display_main_ui()).pack(pady=10)

    def delete_user_ui():
        def submit():
            username = username_entry.get()
            delete_user_by_username(username)
            messagebox.showinfo("Success", "User deleted successfully!")

        for widget in user_tab.winfo_children():
            widget.destroy()

        tk.Label(user_tab, text="Delete User", font=("Arial", 14)).pack(pady=10)

        tk.Label(user_tab, text="Username:").pack()
        username_entry = tk.Entry(user_tab)
        username_entry.pack()

        tk.Button(user_tab, text="Delete", command=submit).pack(pady=10)

        tk.Button(user_tab, text="Back", command=lambda: display_main_ui()).pack(pady=10)

    def delete_user_by_username(username):
        try:
            # Query user by username
            user = session.query(User).filter(User.username == username).first()

            if user:
                # Delete user from 'User' table
                session.delete(user)

                # Commit the changes
                session.commit()
            else:
                messagebox.showerror("Error", f"User with username '{username}' does not exist.")
        except Exception as e:
            session.rollback()
            messagebox.showerror("Error", str(e))

    def display_main_ui():
        for widget in user_tab.winfo_children():
            widget.destroy()

        tk.Label(user_tab, text="Main User Interface", font=("Arial", 14)).pack(pady=10)

        # Add buttons or other UI elements that allow navigation to different parts of your application
        tk.Button(user_tab, text="Register User", command=register_user_ui).pack(pady=5)
        tk.Button(user_tab, text="Update User", command=update_user_ui).pack(pady=5)
        tk.Button(user_tab, text="Delete User", command=delete_user_ui).pack(pady=5)
        tk.Button(user_tab, text="View Users", command=view_users_ui).pack(pady=5)

    def view_users_ui():
        def fetch_users():
            users_text.delete("1.0", tk.END)
            users = session.query(User).all()  # Assuming User is the mapped class for users
            if users:
                for user in users:
                    users_text.insert(tk.END, f"ID: {user.id}, Username: {user.username}, Email: {user.email}\n")
            else:
                users_text.insert(tk.END, "No users found.")

        for widget in user_tab.winfo_children():
            widget.destroy()

        tk.Label(user_tab, text="User List", font=("Arial", 14)).pack(pady=10)

        users_text = tk.Text(user_tab, width=80, height=20)
        users_text.pack()

        tk.Button(user_tab, text="Fetch Users", command=fetch_users).pack(pady=10)
        tk.Button(user_tab, text="Back", command=lambda: display_main_ui()).pack(pady=10)

    tk.Button(user_tab, text="Register User", command=register_user_ui).pack(pady=5)
    tk.Button(user_tab, text="Update User", command=update_user_ui).pack(pady=5)
    tk.Button(user_tab, text="Delete User", command=delete_user_ui).pack(pady=5)
    tk.Button(user_tab, text="View Users", command=view_users_ui).pack(pady=5)
    # Expense Management
    def record_expense_ui():
        def submit():
            user_id = user_id_entry.get()
            date = date_entry.get()
            amount = amount_entry.get()
            category = category_entry.get()
            description = description_entry.get()
            record_expense(user_id, date, amount, category, description)
            messagebox.showinfo("Success", "Expense recorded successfully!")

        for widget in expense_tab.winfo_children():
            widget.destroy()

        tk.Label(expense_tab, text="Record Expense", font=("Arial", 14)).pack(pady=10)

        tk.Label(expense_tab, text="User ID:").pack()
        user_id_entry = tk.Entry(expense_tab)
        user_id_entry.pack()

        tk.Label(expense_tab, text="Date (YYYY-MM-DD):").pack()
        date_entry = tk.Entry(expense_tab)
        date_entry.pack()

        tk.Label(expense_tab, text="Amount:").pack()
        amount_entry = tk.Entry(expense_tab)
        amount_entry.pack()

        tk.Label(expense_tab, text="Category:").pack()
        category_entry = tk.Entry(expense_tab)
        category_entry.pack()

        tk.Label(expense_tab, text="Description:").pack()
        description_entry = tk.Entry(expense_tab)
        description_entry.pack()

        tk.Button(expense_tab, text="Submit", command=submit).pack(pady=10)

    def view_expenses_ui():
        def fetch_expenses():
            user_id = user_id_entry.get()
            expenses = view_expenses(user_id)
            expenses_text.delete("1.0", tk.END)
            for expense in expenses:
                expenses_text.insert(tk.END, f"{expense.date}: {expense.category} - {expense.amount} ({expense.description})\n")

        for widget in expense_tab.winfo_children():
            widget.destroy()

        tk.Label(expense_tab, text="View Expenses", font=("Arial", 14)).pack(pady=10)

        tk.Label(expense_tab, text="User ID:").pack()
        user_id_entry = tk.Entry(expense_tab)
        user_id_entry.pack()

        tk.Button(expense_tab, text="Fetch Expenses", command=fetch_expenses).pack(pady=10)

        expenses_text = tk.Text(expense_tab, width=80, height=20)
        expenses_text.pack()

    tk.Button(expense_tab, text="Record Expense", command=record_expense_ui).pack(pady=5)
    tk.Button(expense_tab, text="View Expenses", command=view_expenses_ui).pack(pady=5)


    # Inventory Management
    def add_inventory_ui():
        def submit():
            item_name = item_name_entry.get()
            quantity = quantity_entry.get()
            cost = cost_entry.get()
            add_inventory_item(item_name, quantity, cost)
            messagebox.showinfo("Success", "Inventory item added successfully!")

        for widget in inventory_tab.winfo_children():
            widget.destroy()

        tk.Label(inventory_tab, text="Add Inventory Item", font=("Arial", 14)).pack(pady=10)

        tk.Label(inventory_tab, text="Item Name:").pack()
        item_name_entry = tk.Entry(inventory_tab)
        item_name_entry.pack()

        tk.Label(inventory_tab, text="Quantity:").pack()
        quantity_entry = tk.Entry(inventory_tab)
        quantity_entry.pack()

        tk.Label(inventory_tab, text="Cost:").pack()
        cost_entry = tk.Entry(inventory_tab)
        cost_entry.pack()

        tk.Button(inventory_tab, text="Submit", command=submit).pack(pady=10)

    def update_inventory_ui():
        def submit():
            item_id = item_id_entry.get()
            item_name = item_name_entry.get()
            quantity = quantity_entry.get()
            cost = cost_entry.get()
            update_inventory_item(item_id, item_name, quantity, cost)
            messagebox.showinfo("Success", "Inventory item updated successfully!")

        for widget in inventory_tab.winfo_children():
            widget.destroy()

        tk.Label(inventory_tab, text="Update Inventory Item", font=("Arial", 14)).pack(pady=10)

        tk.Label(inventory_tab, text="Item ID:").pack()
        item_id_entry = tk.Entry(inventory_tab)
        item_id_entry.pack()

        tk.Label(inventory_tab, text="Item Name:").pack()
        item_name_entry = tk.Entry(inventory_tab)
        item_name_entry.pack()

        tk.Label(inventory_tab, text="Quantity:").pack()
        quantity_entry = tk.Entry(inventory_tab)
        quantity_entry.pack()

        tk.Label(inventory_tab, text="Cost:").pack()
        cost_entry = tk.Entry(inventory_tab)
        cost_entry.pack()

        tk.Button(inventory_tab, text="Update", command=submit).pack(pady=10)

    def delete_inventory_ui():
        def submit():
            item_id = item_id_entry.get()
            delete_inventory_item(item_id)
            messagebox.showinfo("Success", "Inventory item deleted successfully!")

        for widget in inventory_tab.winfo_children():
            widget.destroy()

        tk.Label(inventory_tab, text="Delete Inventory Item", font=("Arial", 14)).pack(pady=10)

        tk.Label(inventory_tab, text="Item ID:").pack()
        item_id_entry = tk.Entry(inventory_tab)
        item_id_entry.pack()

        tk.Button(inventory_tab, text="Delete", command=submit).pack(pady=10)

    def view_inventory_ui():
        def fetch_inventory():
            inventory_text.delete("1.0", tk.END)
            items = view_inventory()
            print(items)
            if items:
                for item in items:
                    inventory_text.insert(tk.END, f"{item.item_name}: {item.quantity} units at {item.cost} each\n")
            else:
                inventory_text.insert(tk.END, "No inventory items found.")

        tk.Label(inventory_tab, text="View Inventory", font=("Arial", 14)).pack(pady=10)

        inventory_text = tk.Text(inventory_tab, width=80, height=20)
        inventory_text.pack()

        tk.Button(inventory_tab, text="Fetch Inventory", command=fetch_inventory).pack(pady=10)

    tk.Button(inventory_tab, text="Add Item", command=add_inventory_ui).pack(pady=5)
    tk.Button(inventory_tab, text="Update Item", command=update_inventory_ui).pack(pady=5)
    tk.Button(inventory_tab, text="Delete Item", command=delete_inventory_ui).pack(pady=5)
    tk.Button(inventory_tab, text="View Inventory", command=view_inventory_ui).pack(pady=5)

    # Sales Tracking
    def sales_ui():
        def submit():
            user_id = user_id_entry.get()
            date = date_entry.get()
            amount = amount_entry.get()
            items_sold = items_sold_entry.get()
            record_sale(user_id, date, amount, items_sold)
            messagebox.showinfo("Success", "Sale recorded successfully!")

        for widget in sales_tab.winfo_children():
            widget.destroy()

        tk.Label(sales_tab, text="Record Sale", font=("Arial", 14)).pack(pady=10)

        tk.Label(sales_tab, text="User ID:").pack()
        user_id_entry = tk.Entry(sales_tab)
        user_id_entry.pack()

        tk.Label(sales_tab, text="Date (YYYY-MM-DD):").pack()
        date_entry = tk.Entry(sales_tab)
        date_entry.pack()

        tk.Label(sales_tab, text="Amount:").pack()
        amount_entry = tk.Entry(sales_tab)
        amount_entry.pack()

        tk.Label(sales_tab, text="Items Sold:").pack()
        items_sold_entry = tk.Entry(sales_tab)
        items_sold_entry.pack()

        tk.Button(sales_tab, text="Submit", command=submit).pack(pady=10)

    def view_sales_ui():
        def fetch_sales():
            user_id = user_id_entry.get()
            sales = view_sales(user_id)
            sales_text.delete("1.0", tk.END)
            if sales:
                for sale in sales:
                    sales_text.insert(tk.END, f"{sale.date}: {sale.items_sold} - {sale.amount}\n")
            else:
                sales_text.insert(tk.END, "No sales found.")

        for widget in sales_tab.winfo_children():
            widget.destroy()

        tk.Label(sales_tab, text="View Sales", font=("Arial", 14)).pack(pady=10)

        tk.Label(sales_tab, text="User ID:").pack()
        user_id_entry = tk.Entry(sales_tab)
        user_id_entry.pack()

        tk.Button(sales_tab, text="Fetch Sales", command=fetch_sales).pack(pady=10)

        sales_text = tk.Text(sales_tab, width=80, height=20)
        sales_text.pack()

    tk.Button(sales_tab, text="Record Sale", command=sales_ui()).pack(pady=5)
    tk.Button(sales_tab, text="View Sales", command=view_sales_ui).pack(pady=5)

    # Reports
    # Generate Reports
    def generate_reports_ui():
        def generate_reports():
            reports_text.delete("1.0", tk.END)
            report_data = generate_financial_reports()
            reports_text.insert(tk.END, report_data)

        for widget in reports_tab.winfo_children():
            widget.destroy()

        tk.Label(reports_tab, text="Generate Financial Reports", font=("Arial", 14)).pack(pady=10)

        reports_text = tk.Text(reports_tab, width=80, height=20)
        reports_text.pack()

        tk.Button(reports_tab, text="Generate Reports", command=generate_reports).pack(pady=10)

    tk.Button(reports_tab, text="Generate Reports", command=generate_reports_ui).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()