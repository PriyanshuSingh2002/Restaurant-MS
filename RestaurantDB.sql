CREATE DATABASE restaurant_management;
USE restaurant_management;



CREATE TABLE MenuItems (
    item_id INT PRIMARY KEY AUTO_INCREMENT,
    item_name VARCHAR(200) NOT NULL,
    category VARCHAR(20) NOT NULL,
    price DECIMAL(10, 2),
    availability BOOLEAN
);


CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    contact_number VARCHAR(15),
    email VARCHAR(100)
);


CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    item_id INT,
    order_date DATE,
    quantity INT,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (item_id) REFERENCES MenuItems(item_id)
);




