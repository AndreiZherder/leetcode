SELECT Customers.name AS Customers
FROM Customers
WHERE Customers.id NOT IN
    (SELECT Customers.id
     FROM Customers
     JOIN Orders ON Customers.id = Orders.customerId)