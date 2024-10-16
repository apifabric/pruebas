# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  October 16, 2024 20:40:47
# Database: sqlite:////tmp/tmp.f1oM5C2hmJ/pruebas/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Customer(SAFRSBaseX, Base):
    """
    description: Table to store customer information.
    """
    __tablename__ = 'customers'
    _s_collection_name = 'Customer'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    # parent relationships (access parent)

    # child relationships (access children)
    OrderList : Mapped[List["Order"]] = relationship(back_populates="customer")



class Employee(SAFRSBaseX, Base):
    """
    description: Table to store employee details who work in the store.
    """
    __tablename__ = 'employees'
    _s_collection_name = 'Employee'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    position = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    SaleList : Mapped[List["Sale"]] = relationship(back_populates="employee")



class Fruit(SAFRSBaseX, Base):
    """
    description: Table to store information about different types of fruits available in the store.
    """
    __tablename__ = 'fruits'
    _s_collection_name = 'Fruit'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price_per_kg = Column(Float, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    ExpiryList : Mapped[List["Expiry"]] = relationship(back_populates="fruit")
    InventoryList : Mapped[List["Inventory"]] = relationship(back_populates="fruit")
    PromotionList : Mapped[List["Promotion"]] = relationship(back_populates="fruit")
    SaleList : Mapped[List["Sale"]] = relationship(back_populates="fruit")
    SupplierFruitList : Mapped[List["SupplierFruit"]] = relationship(back_populates="fruit")
    OrderDetailList : Mapped[List["OrderDetail"]] = relationship(back_populates="fruit")
    SaleDetailList : Mapped[List["SaleDetail"]] = relationship(back_populates="fruit")



class Supplier(SAFRSBaseX, Base):
    """
    description: Table to store details about suppliers providing fruits to the store.
    """
    __tablename__ = 'suppliers'
    _s_collection_name = 'Supplier'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_info = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    SupplierFruitList : Mapped[List["SupplierFruit"]] = relationship(back_populates="supplier")



class Expiry(SAFRSBaseX, Base):
    """
    description: Table to track the expiry dates of fruits in inventory.
    """
    __tablename__ = 'expiries'
    _s_collection_name = 'Expiry'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    fruit_id = Column(ForeignKey('fruits.id'), nullable=False)
    expiry_date = Column(DateTime, nullable=False)

    # parent relationships (access parent)
    fruit : Mapped["Fruit"] = relationship(back_populates=("ExpiryList"))

    # child relationships (access children)



class Inventory(SAFRSBaseX, Base):
    """
    description: Table to manage the inventory levels of different fruits.
    """
    __tablename__ = 'inventory'
    _s_collection_name = 'Inventory'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    fruit_id = Column(ForeignKey('fruits.id'), nullable=False)
    quantity_kg = Column(Float, nullable=False)

    # parent relationships (access parent)
    fruit : Mapped["Fruit"] = relationship(back_populates=("InventoryList"))

    # child relationships (access children)



class Order(SAFRSBaseX, Base):
    """
    description: Table to store orders placed by customers.
    """
    __tablename__ = 'orders'
    _s_collection_name = 'Order'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customers.id'), nullable=False)
    order_date = Column(DateTime, nullable=False)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("OrderList"))

    # child relationships (access children)
    OrderDetailList : Mapped[List["OrderDetail"]] = relationship(back_populates="order")



class Promotion(SAFRSBaseX, Base):
    """
    description: Table to store promotional offers for various fruits.
    """
    __tablename__ = 'promotions'
    _s_collection_name = 'Promotion'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    fruit_id = Column(ForeignKey('fruits.id'), nullable=False)
    discount_percentage = Column(Float, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)

    # parent relationships (access parent)
    fruit : Mapped["Fruit"] = relationship(back_populates=("PromotionList"))

    # child relationships (access children)



class Sale(SAFRSBaseX, Base):
    """
    description: Table to store sales transactions made by employees.
    """
    __tablename__ = 'sales'
    _s_collection_name = 'Sale'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    employee_id = Column(ForeignKey('employees.id'), nullable=False)
    fruit_id = Column(ForeignKey('fruits.id'), nullable=False)
    quantity_kg = Column(Float, nullable=False)
    sale_date = Column(DateTime, nullable=False)

    # parent relationships (access parent)
    employee : Mapped["Employee"] = relationship(back_populates=("SaleList"))
    fruit : Mapped["Fruit"] = relationship(back_populates=("SaleList"))

    # child relationships (access children)
    SaleDetailList : Mapped[List["SaleDetail"]] = relationship(back_populates="sale")



class SupplierFruit(SAFRSBaseX, Base):
    """
    description: Table to manage the relationship between suppliers and the fruits they supply.
    """
    __tablename__ = 'supplier_fruits'
    _s_collection_name = 'SupplierFruit'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    supplier_id = Column(ForeignKey('suppliers.id'), nullable=False)
    fruit_id = Column(ForeignKey('fruits.id'), nullable=False)

    # parent relationships (access parent)
    fruit : Mapped["Fruit"] = relationship(back_populates=("SupplierFruitList"))
    supplier : Mapped["Supplier"] = relationship(back_populates=("SupplierFruitList"))

    # child relationships (access children)



class OrderDetail(SAFRSBaseX, Base):
    """
    description: Table to store details of each order, including the fruits and quantities ordered.
    """
    __tablename__ = 'order_details'
    _s_collection_name = 'OrderDetail'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('orders.id'), nullable=False)
    fruit_id = Column(ForeignKey('fruits.id'), nullable=False)
    quantity_kg = Column(Float, nullable=False)

    # parent relationships (access parent)
    fruit : Mapped["Fruit"] = relationship(back_populates=("OrderDetailList"))
    order : Mapped["Order"] = relationship(back_populates=("OrderDetailList"))

    # child relationships (access children)



class SaleDetail(SAFRSBaseX, Base):
    """
    description: Table to store detailed information of each sale including pricing.
    """
    __tablename__ = 'sale_details'
    _s_collection_name = 'SaleDetail'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    sale_id = Column(ForeignKey('sales.id'), nullable=False)
    fruit_id = Column(ForeignKey('fruits.id'), nullable=False)
    price_sold = Column(Float, nullable=False)

    # parent relationships (access parent)
    fruit : Mapped["Fruit"] = relationship(back_populates=("SaleDetailList"))
    sale : Mapped["Sale"] = relationship(back_populates=("SaleDetailList"))

    # child relationships (access children)
