# SQL_Modifying_Date(DML : 데이터 조작)

## 학습목표
- insert, update, delect의 역할을 설명
- 주어진 예시에 맞추어 테이블에 새로운 정보를 쓰거나 기존 레코드를 수정 삭제할 수 있다


## insert data into table

```sql
insert into table_name(c1..c2)
values (v1, v2...)
```
---
Q. articles 테이블에 테이터를 집어넣어라
```sql
INSERT INTO articles(title, content, createdAt)
VALUES ('hello', 'world', '2000-01-01');
```

Q. articles 테이블에 테이터를 *여러개* 집어넣어라
```sql
INSERT INTO articles(title, content, createdAt)
VALUES ('hello', 'world', '2000-01-01'),
	("title1", "contnent1", "1900-01-01"),
    ("title2", "contnent2", "1800-01-01"),
    ("title3", "contnent3", "1700-01-01");
```
Q. articles 테이블에 테이터 중 날짜는 자동으로 입력 받아라
```sql
INSERT INTO articles(title, content, createdAt)
VALUES ('mytitle', 'mycontent', curdate());
```
* curdate() : 현재 날짜 입력 함수

## Update statement(레코드 수정)
```sql
Update t_n
Set column_nme = expression
Where 
    condition;
```
set 절 다음 수정할 필드와 새 값을 지정
where 절에서 수정할 레코드 조건 작성

---
Q. articles 테이블에 테이터 중 *1번 데이터의 타이틀을 변경*해라
```sql
UPDATE articles
SET title = "newTitle"
WHERE
	id = 1;
```
Q. articles 테이블에 테이터 중 *3번 데이터의 타이틀과 컨텐트*를 변경해라
```sql
UPDATE articles
SET title = "newTitle",
	content = "newContent2"
WHERE id = 3;
```
Q. articles 테이블에 테이터 중 *컨텐트 중 content가 들어가있으면 TEST*로 변경해라
```sql
UPDATE articles
SET content = replace(content, "contnent", "TEST");
```


## Delete data(삭제)
```sql
DELETE FROM table_name
WHERE ..;
```
Q. articles 테이블에서 1번을 삭제해라
```sql
DELETE FROM articles
WHERE id = 1;
```
Q. articles 테이블에서 최근에 만들어진 데이터를 삭제해라
```sql
DELETE FROM 
	articles
ORDER BY
	createdAt DESC
LIMIT 2;
```
---
참조
safa 모드에 걸렸을때
SET SQL_SAFE_UPDATES = 0;