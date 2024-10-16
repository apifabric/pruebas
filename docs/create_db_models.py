# created from response - used to create database and project
#  should run without error
#  if not, check for decimal, indent, or import issues

import decimal

import logging



logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

import sqlalchemy



from sqlalchemy.sql import func  # end imports from system/genai/create_db_models_inserts/create_db_models_prefix.py

from logic_bank.logic_bank import Rule

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
import datetime

Base = declarative_base()

class Fruit(Base):
    """description: Table to store information about different types of fruits available in the store."""
    __tablename__ = 'fruits'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price_per_kg = Column(Float, nullable=False)

class Inventory(Base):
    """description: Table to manage the inventory levels of different fruits."""
    __tablename__ = 'inventory'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fruit_id = Column(Integer, ForeignKey('fruits.id'), nullable=False)
    quantity_kg = Column(Float, nullable=False)

class Supplier(Base):
    """description: Table to store details about suppliers providing fruits to the store."""
    __tablename__ = 'suppliers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    contact_info = Column(String)

class SupplierFruit(Base):
    """description: Table to manage the relationship between suppliers and the fruits they supply."""
    __tablename__ = 'supplier_fruits'
    id = Column(Integer, primary_key=True, autoincrement=True)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'), nullable=False)
    fruit_id = Column(Integer, ForeignKey('fruits.id'), nullable=False)

class Customer(Base):
    """description: Table to store customer information."""
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

class Order(Base):
    """description: Table to store orders placed by customers."""
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    order_date = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)

class OrderDetail(Base):
    """description: Table to store details of each order, including the fruits and quantities ordered."""
    __tablename__ = 'order_details'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    fruit_id = Column(Integer, ForeignKey('fruits.id'), nullable=False)
    quantity_kg = Column(Float, nullable=False)

class Promotion(Base):
    """description: Table to store promotional offers for various fruits."""
    __tablename__ = 'promotions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fruit_id = Column(Integer, ForeignKey('fruits.id'), nullable=False)
    discount_percentage = Column(Float, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)

class Employee(Base):
    """description: Table to store employee details who work in the store."""
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    position = Column(String, nullable=False)

class Sale(Base):
    """description: Table to store sales transactions made by employees."""
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    fruit_id = Column(Integer, ForeignKey('fruits.id'), nullable=False)
    quantity_kg = Column(Float, nullable=False)
    sale_date = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)

class SaleDetail(Base):
    """description: Table to store detailed information of each sale including pricing."""
    __tablename__ = 'sale_details'
    id = Column(Integer, primary_key=True, autoincrement=True)
    sale_id = Column(Integer, ForeignKey('sales.id'), nullable=False)
    fruit_id = Column(Integer, ForeignKey('fruits.id'), nullable=False)
    price_sold = Column(Float, nullable=False)

class Expiry(Base):
    """description: Table to track the expiry dates of fruits in inventory."""
    __tablename__ = 'expiries'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fruit_id = Column(Integer, ForeignKey('fruits.id'), nullable=False)
    expiry_date = Column(DateTime, nullable=False)

# Create SQLite database and table schema
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite', echo=False)
Base.metadata.create_all(engine)

# Prepare session
Session = sessionmaker(bind=engine)
session = Session()

# Insert sample data
fruits = [
    Fruit(name='Apple', price_per_kg=2.5),
    Fruit(name='Banana', price_per_kg=1.0),
    Fruit(name='Orange', price_per_kg=3.0)
]

suppliers = [
    Supplier(name='Fresh Farms', contact_info='freshfarms@example.com'),
    Supplier(name='Green Growers', contact_info='greengrowers@example.com')
]

customers = [
    Customer(name='Alice Johnson', email='alice@example.com'),
    Customer(name='Bob Smith', email='bob@example.com')
]

employees = [
    Employee(name='John Doe', position='Sales Manager'),
    Employee(name='Jane Smith', position='Cashier')
]

orders = [
    Order(customer_id=1, order_date=datetime.datetime.utcnow()),
    Order(customer_id=2, order_date=datetime.datetime.utcnow())
]

order_details = [
    OrderDetail(order_id=1, fruit_id=1, quantity_kg=5),
    OrderDetail(order_id=2, fruit_id=2, quantity_kg=10)
]

promotions = [
    Promotion(fruit_id=1, discount_percentage=10.0, start_date=datetime.datetime.utcnow(), end_date=datetime.datetime.utcnow() + datetime.timedelta(days=10)),
    Promotion(fruit_id=2, discount_percentage=15.0, start_date=datetime.datetime.utcnow(), end_date=datetime.datetime.utcnow() + datetime.timedelta(days=7))
]

sales = [
    Sale(employee_id=1, fruit_id=1, quantity_kg=2, sale_date=datetime.datetime.utcnow()),
    Sale(employee_id=2, fruit_id=2, quantity_kg=3, sale_date=datetime.datetime.utcnow())
]

sale_details = [
    SaleDetail(sale_id=1, fruit_id=1, price_sold=5.0),
    SaleDetail(sale_id=2, fruit_id=2, price_sold=3.0)
]

expiries = [
    Expiry(fruit_id=1, expiry_date=datetime.datetime.utcnow() + datetime.timedelta(days=30)),
    Expiry(fruit_id=2, expiry_date=datetime.datetime.utcnow() + datetime.timedelta(days=20))
]

# Add all entries
session.add_all(fruits + suppliers + customers + employees + orders + order_details + promotions + sales + sale_details + expiries)

# Commit the transaction
session.commit()

# Close the session
session.close()
