# SQL_Nested_queries

## 학습 목표


## 서브쿼리란?
단일 쿼리문에 여러 테이블의 데이터를 결합

### 예시
table에서 가장 나이가 어린 사람을 삭제 할 수 있을까?
```sql
DELEDT FROM talbe1
WHERE age = (SELECT MIN(age) FROM table1);
```

### 특징
- 조건이 하나 이상인 테이블을 검색
- 다양한 맥락에서 사용

---
Q.돈을 가장 많이 쓴 고객을 출력
```sql
SELECT customerNumber, amount
FROM payments
WHERE amount = (
	SELECT MAX(amount)
	FROM payments);
```

Q 미국에 근무하는 직원의 이름을 출력해라(2개의 테이블을 비교)
```sql
SELECT lastName, firstName
FROM employees
WHERE officeCode IN (
	SELECT officeCode
	FROM offices
	WHERE country = "USA");
```

Q. 주문하지 않은 고객의 이름 출력
```sql
SELECT customerName
FROM customers
WHERE customerNumber NOT IN (
	SELECT DISTINCT customerNumber
	FROM orders);
```

Q. 돈을 가장 많이 쓴 고객 이름은? 단 *이름은 다른 테이블에서 가져와라*
```sql
SELECT customerNumber, amount, contactFirstName
FROM (SELECT *
	FROM payments
    INNER JOIN customers USING (customerNumber)) AS my
WHERE amount = (
		SELECT MAX(amount)
		FROM payments);
```
**from에서 서브쿼리**를 쓰는경우 무조건 **별칭 지정이 필요**하다

### EXISTS operat

```sql
SELECT
    list
FROM
    table
WHERE
    EXISTS (subquery);
```
subquery가 true 라면 반환 false라면  반환


Q. 한번이라도 주문한 적이 있는 고객 번호와 이름 조회
```sql
SELECT customerNumber, customerName
FROM customers
WHERE EXISTS (
	SELECT *
    FROM orders
    WHERE customers.customerNumber = orders.customerNumber);
```


Q. **Paris에 있는** 사무실에 근무하는 직원 번호 이름 을 조회
```sql
SELECT employeeNumber, firstName, lastName
FROM employees
WHERE EXISTS(
	SELECT *
    FROM offices
    WHERE 
		city = "Paris" AND
		employees.officeCode = offices.officeCode);
```


## Conditional Statement

### Case syntax
```sql
CASE case_value
    WHEN when_value1 THEN statements
    WHEN when_value1 THEN statements
...
    [ELSE else-statemnets]
END CASE;
```
else는 써주는게 무조건 좋다

---
Q. creditlimite에 따라서 grade라는 열을 만들어서 등급을 넣어라
```sql
SELECT contactFirstName, creditLimit,
	CASE 
		WHEN creditLimit > 100000 THEN "VIP"
        WHEN creditLimit > 70000 THEN "Platinum"
        ELSE "Bronze"
    END AS grade
FROM customers;
```

Q. status에 따라 details를 만들어 맞는 값을 집어 넣으시오
```sql
SELECT orderNumber, status,
	CASE
		WHEN status = "In Process" THEN "주문중"
        WHEN status = "Shipped" THEN "발주완료"
        WHEN status = "Cancelled" THEN "주문취소"
        ELSE "기타사유"
	END AS details
FROM orders;
```

---
참고
N:1 관계에서 FK키는 N table이 가져간다

해커 랭크