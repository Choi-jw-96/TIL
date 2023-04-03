SELECT DISTINCT
	lastName
FROM 
	employees
ORDER BY 
	lastName;


SELECT 
	lastName, firstName, jobTitle
FROM
	employees
WHERE
	jobTitle != "Sales Rep";
    
    
    
SELECT 
	lastName, firstName, officeCode, jobTitle
FROM
	employees
WHERE
	officeCode >= 3 AND
    jobTitle = "Sales Rep";
    
    
SELECT 
	lastName, firstName, officeCode, jobTitle
FROM
	employees
WHERE
	officeCode < 5
    OR
    jobTitle != "Sales Rep";
    
SELECT
	lastName, firstName, officeCode
FROM 
	employees
WHERE
	officeCode BETWEEN 1 AND 4
ORDER BY
	officeCode;


SELECT
	lastName, firstName, officeCode
FROM
	employees
WHERE
	officeCode NOT IN (1, 3, 4);
    
SELECT
	lastName, firstName
FROM
	employees
WHERE
	lastName LIKE "%son";

SELECT
	lastName, firstName
FROM 
	employees
WHERE
    firstName LIKE "___y";


SELECT
	firstName, officeCode
FROM
	employees
ORDER BY
	officeCode DESC
LIMIT 3, 5;


SELECT
	country,
    AVG(creditLimit) AS avgOfCreditLimit
FROM 
	customers
GROUP BY
    country
ORDER BY
	avgOfCreditLimit DESC;
    
SELECT
	country,
    AVG(creditLimit)
FROM
	customers
-- WHERE
-- 	AVG(creditLimit) > 800000
GROUP BY
	country
HAVING
	AVG(creditLimit) > 80000;

