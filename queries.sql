
-- Query 1:

SELECT SUM(o.quantity * m.price) AS total_revenue
FROM Orders o
JOIN MenuItems m ON o.item_id = m.item_id;


-- Query 2:

SELECT c.name, c.contact_number
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name, c.contact_number
HAVING COUNT(o.order_id) > 5;


-- Query 3:

SELECT name
FROM MenuItems
WHERE availability = FALSE;


-- Query 4:

SELECT c.customer_id, c.name, COUNT(DISTINCT m.category) AS category_count
FROM Orders o
JOIN Customers c ON o.customer_id = c.customer_id
JOIN MenuItems m ON o.item_id = m.item_id
GROUP BY c.customer_id, c.name
HAVING COUNT(DISTINCT m.category) > 3;


-- Query 5:

SELECT o.order_id, c.customer_id, c.name AS customer_name, c.contact_number, c.email, 
       m.item_id, m.name AS item_name, m.category, m.price, o.order_date, o.quantity
FROM Orders o
JOIN Customers c ON o.customer_id = c.customer_id
JOIN MenuItems m ON o.item_id = m.item_id
WHERE o.order_date >= CURDATE() - INTERVAL 7 DAY;

