# SQL 1개의 테이블 - Filter data

## 학습 목표
- 단일 테이블 내에서 `SELECT`문을 사용해여 결과를 반환
- SELECT문과 다양한 절을 사용해 쿼리 결과를 `정렬 및 필터링`
- Group By와 Aggregation Function을 사용해 각 데이터 값에 대한 `계산된 단일 값을 그룹화하여 반환`

## DQL(검색/조회)

### 1. Querying data(조회)
#### ◆ SELECT Statement

**테이블**에서 **데이터를 조회**

```SQL
SELECT
    select_list
    -- 필드(열)를 하나 지정
FROM
    talbe_name;
    -- 테이플 이름을 지정
```

Q. 테이블 employees에서 lastName 필드를 조회
```SQL
SELECT lastName FROM employees;
```


Q. 테이블 employees에서 *lastName, firstName* 필드를 조회
```SQL
SELECT lastName, firstName FROM employees;
```


Q. *모든 필드*의 테이터 조회
```SQL
SELECT * FROM employees;
```
- `*` : 전체


Q. 테이블 employees에서 *firstName를 "이름"으로* 필드의 모든 데이터를 조회
```SQL
SELECT firstName As "이름" FROM employees;
```
- `AS` 

	: 별칭을 지어줘
	- 여러개도 각각 지어줄 수 있음
	- 색략 가능하다
	- 조회 결과만 바꾼 것(테이블 변경 X)


Q. 테이블 orderdetils에서 productCode, 주문총액 (quantityOrdered*priceEach)필드의 모든 데이터를 조회
```SQL
SELECT 
	productCode, 
	quantityOrdered*priceEach AS "주문 총액" 
FROM 
	orderdetails;
```
기본적인 **사칙연산이 가능**하다



### 2. Sorting data(정렬)

조회한 데이터의 정렬

```SQL
SELECT
    select_list
FROM
    talbe_name
ORDER BY
    -- []는 option
    column1 [ASCIDESC],
    column1 [ASCIDESC],
    ...;
```
- `ASC` : 오름차순(기본값)
- `DESC` : 내림차순

Q. 테이블 employees에서 firstName를 *오름차순*으로 조회
```SQL
SELECT 
	firstName 
FROM 
	employees
ORDER BY 
	firstName;
```


Q. 테이블 employees에서 firstName를 *내림차순*으로 조회
```SQL
SELECT 
	firstName 
FROM 
	employees
ORDER BY 
    firstName DESC;
```


Q. 테이블 employees에서 *lastName를 내림차순 후 firstName 오름차순*으로 조회
```SQL
SELECT
	lastName, firstName
FROM
	employees
ORDER BY
	lastName DESC, firstName;
```
위와 같이 정렬 한다면 **lastName이 같은 애들 중 오름차순**으로 나타남.


Q.  테이블 orderdetils에서 *totalSales의 내림차순*으로 productCode, totalSales (quantityOrdered*priceEach)필드를 조회
```SQL
SELECT
	productCode,
    (quantityOrdered * priceEach)  AS "totalSales"
FROM
	orderdetails
ORDER BY
	totalSales DESC;
```
order by에서 ""를 쓰면 문자열로 인식되어 가동되지 않는다.

* 실행 순서 : 
 from → select →  order by


---
참고

`--` : 주석