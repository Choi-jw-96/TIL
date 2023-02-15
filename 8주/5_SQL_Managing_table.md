# SQL MAnaging table(DDL-기본구조 및 형식 변경)

## 학습목표
- create drop문을 이용하여 데이터 테이블 생성/ 삭제
- mysql의 데이터 제약조건을 사용하여 요구사항의 맞는 스키마를 작성

## 1. Create a table(생성)
```sql
create table table_name(
    colume_1 data_tpye,
    colume_2 data_tpye,
    ...
    constraints(제약 조건)
);
```
---

```sql
CREATE TABLE exmples(
    -- 이름, 데이터 타입, 속성 / 필드의 제약조건
    examID INT AUTO_INCREMENT, 
    lastName VARCHAR(50) NOT NULL, 
    firstName VARCHAR(50) NOT NULL, 
    -- PK 설정(제일 밑에 권장)
    PRIMARY KEY (examId)
);
-- 테이블 구조 확인
SHOW COLUMNS FROM exmples;
```

### ● Data Type
1. 숫자형
    : int, float...
2. 문자형
    : `varcher(가변길이)`, text, ....
3. 날짜형
    : date, datetime


varcher(n) : n글자를 안채워도 됨

cher(n) : n글자를 무조건 채움


### ● Constraint(제약 조건)
데이터의 **무결성**을 지키기 위해 입력 시에 검사 규칙

무결성? 
    : 데이터의 정확성과 일관성 보증

### ● Attribute
- Auto_increment
    
    기본 키 필드에 사용(고유 숫자 부여)
    시작은 1부터 1씩 증가
    이미 사용한 값은 **재사용 안 함**
    기본적으로 Not Null이 제약조건




## 2. Delete a Table(삭제)
```sql
DROP TABLE exmples;
--  테이플 자체를 삭제
```
delet 아님 주위!


## 3.  Modifying Table Fields(수정)
```sql
Alter Talbe
    talbe_name
```
---

### ★ Alter Table
#### Add : 필드 추가
```sql
ALTER TABLE
	table_name
ADD
	colume;
```
---
Q. exmples에 country를 추가
(가변길이 100, null 허용하지 않음)
```sql
ALTER TABLE
	exmples
ADD
	country VARCHAR(100) NOT NULL;
```
Q. exmples에 age(정수, null 허용 안 함), address(가변길이 100, null 허용하지 않음) 추가
```sql
ALTER TABLE
	exmples
ADD	age INT NOT NULL, 
ADD address VARCHAR(100) NOT NULL;
```

#### Modify : 필드 속성 변경
```sql
ALTER TABLE
	table_name
MODIFY
	colume;
```
---
Q. exmples에 addressdml *가변길이 50 변경 null 허용하지 않음*
```sql
ALTER TABLE exmples
MODIFY
	address VARCHAR(50) NOT NULL;
-- 변경시 not null도 지워지니 다시 작성
```

#### Change Colume : 필드 이름 변경
```sql
ALTER TABLE
	table_name
CHANGE COLUME
	colume new_colume;
```
modify의 기능도 함

---
Q. exmples에 country 필드의 *이름을 state로 변경*
```sql
ALTER TABLE exmples
CHANGE COLUMN
	country state VARBINARY(100) NOT NULL;
```
#### Drop Colume : 필드 삭제
```sql
ALTER TABLE table_name
DROP COLUMN colume_name;
```
Q.  exmples에 state와 age 삭제
```sql
ALTER TABLE exmples
DROP COLUMN state,
DROP COLUMN age;
```

---
참고

- 반드시 not null를 사용하나요?
> NO    
프로그램에 따라 null을 저장할 필요가 없는 경우가 많아서 NOT NULL로 정의     
값이 없다 = 0, 빈문자열

