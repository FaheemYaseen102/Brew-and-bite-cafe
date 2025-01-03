from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, create_engine
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# User Table
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    expenses = relationship('Expense', back_populates='user')
    sales = relationship('Sale', back_populates='user')

# Expense Table
class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    date = Column(Date, nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    description = Column(String)

    user = relationship('User', back_populates='expenses')

# Inventory Table
class InventoryItem(Base):
    __tablename__ = 'inventory'

    id = Column(Integer, primary_key=True, autoincrement=True)
    item_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    cost = Column(Float, nullable=False)

# Sales Table
class Sale(Base):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    date = Column(Date, nullable=False)
    amount = Column(Float, nullable=False)
    items_sold = Column(String, nullable=False)

    user = relationship('User', back_populates='sales')

# Initialize Database
if __name__ == "__main__":
    engine = create_engine('sqlite:///expense_tracking_system.db', echo=True)
    Base.metadata.create_all(engine)