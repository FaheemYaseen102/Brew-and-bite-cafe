from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func
from models import User, Expense, InventoryItem, Sale
from datetime import datetime

# Database setup
engine = create_engine('sqlite:///expense_tracking_system.db')
Session = sessionmaker(bind=engine)
session = Session()

# User Management
def register_user(username, password, email):
    user = User(username=username, password=password, email=email)
    session.add(user)
    session.commit()
    print(f"User {username} registered successfully.")

def update_user(user_id, username=None, password=None, email=None):
    user = session.query(User).get(user_id)
    if user:
        if username:
            user.username = username
        if password:
            user.password = password
        if email:
            user.email = email
        session.commit()
        print(f"User {user_id} updated successfully.")
    else:
        print(f"User {user_id} not found.")

def delete_user(user_id):
    user = session.query(User).get(user_id)
    if user:
        session.delete(user)
        session.commit()
        print(f"User {user_id} deleted successfully.")
    else:
        print(f"User {user_id} not found.")

# Expense Management
def record_expense(user_id, date, amount, category, description=None):
    try:
        # Convert the date string to a datetime.date object
        date_obj = datetime.strptime(date, "%Y-%m-%d").date()
        expense = Expense(user_id=user_id, date=date_obj, amount=float(amount), category=category, description=description)
        session.add(expense)
        session.commit()
        print(f"Expense recorded: {expense}")
    except Exception as e:
        print(f"Error: {e}")

def view_expenses(user_id):
    try:
        expenses = session.query(Expense).filter(Expense.user_id == user_id).all()
        return expenses
    except Exception as e:
        print(f"Error retrieving expenses: {e}")
        return []


# Inventory Management
def add_inventory_item(item_name, quantity, cost):
    item = InventoryItem(item_name=item_name, quantity=quantity, cost=cost)
    session.add(item)
    session.commit()
    print(f"Inventory item {item_name} added successfully.")

def update_inventory_item(item_id, item_name=None, quantity=None, cost=None):
    item = session.query(InventoryItem).get(item_id)
    if item:
        if item_name:
            item.item_name = item_name
        if quantity is not None:
            item.quantity = quantity
        if cost is not None:
            item.cost = cost
        session.commit()
        print(f"Inventory item {item_id} updated successfully.")
    else:
        print(f"Inventory item {item_id} not found.")

def delete_inventory_item(item_id):
    item = session.query(InventoryItem).get(item_id)
    if item:
        session.delete(item)
        session.commit()
        print(f"Inventory item {item_id} deleted successfully.")
    else:
        print(f"Inventory item {item_id} not found.")

def view_inventory():
    try:
        items = session.query(InventoryItem).all()
        return items
    except Exception as e:
        print(f"Error retrieving inventory: {e}")
        return []

def record_sale(user_id, date_str, amount, items_sold):
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        sale = Sale(user_id=user_id, date=date, amount=amount, items_sold=items_sold)
        session.add(sale)
        session.commit()
        print("Sale recorded successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error recording sale: {e}")

def view_sales(user_id):
    try:
        sales = session.query(Sale).filter(Sale.user_id == user_id).all()
        return sales
    except Exception as e:
        print(f"Error retrieving sales: {e}")
        return []

# Reporting
def generate_financial_reports():
    total_expenses = session.query(Expense).with_entities(func.sum(Expense.amount)).scalar() or 0
    total_sales = session.query(Sale).with_entities(func.sum(Sale.amount)).scalar() or 0
    inventory_summary = session.query(InventoryItem).all()

    report_data = f"Total Expenses: {total_expenses}\nTotal Sales: {total_sales}\nInventory Summary:\n"
    for item in inventory_summary:
        report_data += f"{item.item_name}: {item.quantity} units at {item.cost} each\n"

    return report_data