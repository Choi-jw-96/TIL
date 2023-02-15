DROP TABLE IF EXISTS user;
CREATE TABLE users(
	id INT AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
    );
    
CREATE TABLE articles(
	id INT AUTO_INCREMENT, 
    title VARCHAR(50) NOT NULL, 
    content VARCHAR(100) NOT NULL, 
    userId INT NOT NULL, 
    PRIMARY KEY (id)
);

INSERT INTO users(name)
VALUES 
	("권미자"),
    ("류준하"),
    ("정영식");

INSERT INTO
	articles(title, content, userID)
VALUES
	("제목1", "내용1", 1),
    ("제목2", "내용2", 2),
    ("제목3", "내용3", 4);
    
DELETE FROM articles;
SET SQL_SAFE_UPDATES = 0;
SELECT * FROM articles;


SELECT articles.id, title, content, name
FROM articles
INNER JOIN users
ON articles.userId = users.id;


SELECT productCode, productName, textDescription
FROM products
INNER JOIN productlines
	ON products.productLine = productlines.productLine;


SELECT orders.orderNumber, status, priceEach
FROM orders
INNER JOIN orderdetails
	ON orders.orderNumber = orderdetails.orderNumber;


SELECT orders.orderNumber, status, SUM(priceEach * quantityOrdered) AS totalSales
FROM orders
INNER JOIN orderdetails
	ON orders.orderNumber = orderdetails.orderNumber
GROUP BY  orders.orderNumber;


SELECT contactFirstName, orderNumber, status
FROM customers
LEFT JOIN orders
	ON customers.customerNumber = orders.customerNumber
WHERE orderNumber IS NULL;


SELECT employeeNumber, firstName, customerName, contactFirstName
FROM customers
RIGHT JOIN employees
	ON customers.salesRepEmployeeNumber = employees.employeeNumber;
    
    
SELECT employeeNumber, firstName, customerName, contactFirstName
FROM customers
RIGHT JOIN employees
	ON customers.salesRepEmployeeNumber = employees.employeeNumber
WHERE customerNumber IS NULL;