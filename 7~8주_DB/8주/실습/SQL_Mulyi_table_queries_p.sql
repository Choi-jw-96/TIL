-- 문제 1
SELECT employeeNumber, lastName, firstName, city
FROM employees
INNER JOIN offices
	ON employees.officeCode = offices.officeCode
ORDER BY
	employeeNumber;
    
    
-- 문제 2
SELECT customerNumber, officeCode, customers.city, offices.city
FROM customers
LEFT JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;
    

-- 문제 3
SELECT customerNumber, officeCode, customers.city, offices.city
FROM customers
RIGHT JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;
    
    
-- 문제 4
SELECT customerNumber, officeCode, customers.city, offices.city
FROM customers
INNER JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;
    
-- 문제 5
-- LEFT JOIN : customers 차집합 + 교집합 => customers(in office와의 교집합)
-- RIGHT JOIN : customers 여집합 + 교집합 => offices(in customers 교집합)
-- INNER JOINT : 교집합


-- 문제 6
SELECT customerNumber, officeCode, customers.city, offices.city
FROM customers LEFT JOIN offices
ON customers.city = offices.city
UNION 
SELECT customerNumber, officeCode, customers.city, offices.city
FROM customers RIGHT JOIN offices
ON customers.city = offices.city
ORDER BY
	customerNumber DESC;
    
    
-- 문제 7
SELECT orders.orderNumber, orderDate
FROM orderdetails
INNER JOIN orders
	ON orderdetails.orderNumber = orders.orderNumber
ORDER BY orderNumber;


-- 문제 8
SELECT orderNumber, orderdetails.productCode, productName
FROM orderdetails
INNER JOIN products
	ON orderdetails.productCode = products.productCode
ORDER BY orderNumber;


-- 문제 9
SELECT orderdetails.orderNumber, orderdetails.productCode, orderDate, productName
FROM orderdetails
INNER JOIN orders
INNER JOIN products
	ON 
		orderdetails.orderNumber = orders.orderNumber And
		orderdetails.productCode = products.productCode
ORDER BY
	orderNumber;