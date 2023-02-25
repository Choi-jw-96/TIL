-- 문제 1
SELECT productCode, productName, MSRP
FROM products
WHERE MSRP > (
	SELECT AVG(MSRP)
    FROM products)
ORDER BY MSRP;

-- 문제 2
SELECT * FROM orders;

SELECT customerNumber, customerName
FROM customers
WHERE customerNumber IN (
	SELECT customerNumber
    FROM orders
    WHERE orderDate BETWEEN "2003-01-06" AND "2003-03-26")
ORDER BY
	customerNumber;


-- 문제 3
SELECT * FROM products;

SELECT productCode, productName, productLine, MSRP
FROM products
WHERE MSRP = (
	SELECT MAX(MSRP)
    FROM products) AND
    productLine = "Classic Cars";



-- 문제 4
SELECT country
FROM customers
GROUP BY country
HAVING count(country) 
ORDER BY count(country) DESC
LIMIT 1;
--
SELECT customerNumber, customerName, country
FROM customers
WHERE country = (
	 -- 서브쿼리 안에서 리밋을 사용하기 위해 묶고 별칭
	SELECT * FROM (
	SELECT country
	FROM customers
	GROUP BY country
	HAVING count(country) 
	ORDER BY count(country) DESC
	LIMIT 1) as tmp)
ORDER BY customerNumber;

--

SELECT customerNumber , customerName , country
FROM customers
WHERE country = (
SELECT country
FROM customers
GROUP BY country
ORDER BY COUNT(country) DESC
LIMIT 1
)
ORDER BY customerNumber;

-- 문제 5
SELECT customerNumber, customerName, COUNT(orderNumber) AS order_count
FROM (
	SELECT *
    FROM customers
    INNER JOIN orders USING (customerNumber)) AS my
GROUP BY customerNumber
ORDER BY order_count DESC
LIMIT 1;
    
    
-- 문제 6
SELECT * FROM orders;
SELECT * FROM orderdetails;
SELECT * FROM products;

SELECT DISTINCT productCode, productName
FROM (
	SELECT *
    FROM products
    INNER JOIN orderdetails USING (productCode)) AS mymy
WHERE orderNumber IN (
	SELECT orderNumber
    FROM orders
    WHERE year(orderDate) = "2004")
ORDER BY
	productCode DESC;
    
    
-- 서브 쿼리를 사용 안해도 됨
SELECT DISTINCT productCode , productName
FROM orderdetails
INNER JOIN orders USING (orderNumber)
INNER JOIN products USING (productCode)
WHERE year(orderDate) = '2004'
ORDER BY productCode DESC;


--
SELECT DISTINCT productCode, productName
FROM products a1
INNER JOIN orderdetails a2 USING (productCode)
WHERE productCode IN (
    SELECT productCode
    FROM orders 
    WHERE YEAR(orderDate) = '2004')
ORDER BY productCode DESC;

-- exisits
SELECT productCode, productName
FROM products
WHERE EXISTS (
    SELECT *
    FROM orders
    WHERE
    YEAR(orderDate) = '2004'
)
ORDER BY productCode DESC;