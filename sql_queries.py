# Drop tables

categories_table_drop = 'DROP TABLE IF EXISTS categories'
customers_table_drop = 'DROP TABLE IF EXISTS customers'
employees_table_drop = 'DROP TABLE IF EXISTS employees'
order_details_table_drop = 'DROP TABLE IF EXISTS order_details'
orders_table_drop = 'DROP TABLE IF EXISTS orders'
products_table_drop = 'DROP TABLE IF EXISTS products'
shippers_table_drop = 'DROP TABLE IF EXISTS shippers'
suppliers_table_drop = 'DROP TABLE IF EXISTS suppliers'


# Create tables

categories_table_create = 'CREATE TABLE categories (categoryID int, categoryName text, description text)'
customers_table_create = 'CREATE TABLE customers (customerID int, customerName text, contactName text, address text, city text, postalCode text, country text)'
employees_table_create = 'CREATE TABLE employees (EmployeeID int, LastName text, FirstName text, BirthDate date, Photo text, Notes text)'
order_details_table_create = 'CREATE TABLE orderDetails (OrderDetailID int, OrderID int, ProductID int, Quantity int)'
orders_table_create = 'CREATE TABLE orders (OrderID int, CustomerID int, EmployeeID int, OrderDate date, ShipperID int)'
products_table_create = 'CREATE TABLE products (ProductID int, ProductName text, SupplierID int, CategoryID int, Unit text, Price float)'
shippers_table_create = 'CREATE TABLE shippers (ShipperID int, ShipperName text, Phone text)'
suppliers_table_create = 'CREATE TABLE suppliers (SupplierID int, SupplierName text, ContactName text, Address text, City text, PostalCode text, Country text, Phone text)'

# Insert records

categories_table_insert = 'INSERT INTO categories (categoryID, categoryName, description) VALUES(?,?,?)'
customers_table_insert = 'INSERT INTO customers (customerID, customerName, contactName, address, city, postalCode, country) VALUES (?,?,?,?,?,?,?)'
employees_table_insert = 'INSERT INTO employees (EmployeeID, LastName, FirstName, BirthDate, Photo, Notes)  VALUES(?,?,?,?,?,?)'
order_details_table_insert = 'INSERT INTO orderDetails (OrderDetailID, OrderID, ProductID, Quantity) VALUES(?,?,?,?)'
orders_table_insert = 'INSERT INTO orders (OrderID, CustomerID, EmployeeID, OrderDate, ShipperID) VALUES(?,?,?,?,?)'
products_table_insert = 'INSERT INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price) VALUES(?,?,?,?,?,?)'
shippers_table_insert = 'INSERT INTO shippers (ShipperID, ShipperName, Phone) VALUES(?,?,?)'
suppliers_table_insert = 'INSERT INTO suppliers (SupplierID, SupplierName, ContactName, Address, City, PostalCode, Country, Phone) VALUES(?,?,?,?,?,?,?,?)'

# Query list

drop_tables_queries = [categories_table_drop, customers_table_drop, employees_table_drop, order_details_table_drop, orders_table_drop, products_table_drop, shippers_table_drop, suppliers_table_drop]

create_tables_queries = [categories_table_create, customers_table_create, employees_table_create, order_details_table_create, orders_table_create, products_table_create, shippers_table_create, suppliers_table_create]

insert_records_queries = [categories_table_insert, customers_table_insert, employees_table_insert, order_details_table_insert, orders_table_insert, products_table_insert, shippers_table_insert, suppliers_table_insert]