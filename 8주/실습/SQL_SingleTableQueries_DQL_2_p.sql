-- 문제 1
SELECT DISTINCT
	country
FROM 
	customers
ORDER BY
	country;
    
    
-- 문제 2
SELECT DISTINCT
	state
FROM
	customers
ORDER BY
	state DESC;
    

-- 문제 3
SELECT
	customerNumber, customerName, country
FROM
	customers
WHERE
	country != "USA"
ORDER BY
	customerNumber DESC;
    

-- 문제 4
SELECT
	*
FROM
	offices
WHERE
	city = "Paris";


-- 문제 5
SELECT
	customerNumber, customerName, country, state
FROM
	customers
WHERE
	country = "USA"
    AND state = "CA"
ORDER BY
	customerName DESC;
    
    
-- 문제 6
SELECT
	customerNumber, customerName, country, state
FROM
	customers
WHERE
	country = "USA" AND
    state in ("CA", "NY") 
ORDER BY
	customerNumber DESC;
    


-- 문제 7
SELECT
	customerNumber, customerName, state
FROM
	customers
WHERE
	state in ("CA", "NY", "CT", "PA")
ORDER BY
	customerNumber DESC;
    
    
-- 문제 8
SELECT
	productCode, productName, quantityInStock
FROM
	products
WHERE
	quantityInStock < 1000
ORDER BY
	quantityInStock;
    
    
    
-- 문제 9
SELECT
	productCode, productName, quantityInStock
FROM
	products
WHERE
	quantityInStock BETWEEN 2000 AND 3000
ORDER BY
	quantityInStock DESC;
    

-- 문제 10
SELECT
	customerNumber, customerName, phone
FROM
	customers
WHERE
	phone LIKE "%555"
ORDER BY
	customerName DESC;
    
    

-- 문제 11
SELECT
	productCode, quantityInStock
FROM
	products
ORDER BY
	quantityInStock DESC LIMIT 5;
    
    
-- 문제 12
SELECT
	jobTitle, COUNT(jobTitle) AS count_job
FROM
	employees
GROUP BY
	jobTitle
ORDER BY
	count_job DESC;
    
    

-- 문제 13
SELECT
	country, COUNT(country) AS count_country
FROM
	customers
GROUP BY
	country
ORDER BY
	count_country DESC;
    
    
-- 문제 14
SELECT
	orderNumber, SUM(quantityOrdered * priceEach) as total
FROM 
	orderdetails
GROUP BY
	orderNumber
ORDER BY
	total DESC;
    

-- 문제 15
SELECT
	year(orderDate) as year, COUNT(orderNumber)
FROM
	orders
GROUP BY
	year;
	

-- 문제 16
SELECT
	productLine, MAX(quantityInStock) as max_stock
FROM
	products
GROUP BY
	productLine
HAVING
max_stock < 9000;



-- 문제 17
SELECT
	orderNumber, SUM(quantityOrdered) AS itemsCount, SUM(priceEach * quantityOrdered) as total
FROM
	orderdetails
GROUP BY
	orderNumber
HAVING
	itemsCount >= 500 and
    total >= 50000;
    