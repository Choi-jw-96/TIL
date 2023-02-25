# SQL Advanced

## 학습 목표


## Transaction
여러 쿼리문을 묶어서 하나의 작업처럼 처리하는 방법

모든 과정이 성공해야 한다(일관성 유지)

- 예) 계좌이체 (인출 & 입금) : 인출과 입금이 둘다 함께 성공해야 성공


```sql
# 자동 COMMIT 비활성화
SET AUTOCOMMIT = 0
START TRANSACTION;

[ROLLBACK COMMIT]
```
- START TRANSACTION : 문구 시작
- COMMIT : 모든 작업이 정상적으로 완료 되면 한꺼번에 DB반영
- ROLLBACK : 하나라도 실패시 연산을 취소하고 연산전으로 되돌린


```sql
SET AUTOCOMMIT = 0;
START TRANSACTION;
INSERT INTO users (name)
VALUES ('harry'), ('test');

SELECT * FROM users;

ROLLBACK;

COMMIT;
```

## Triggers
특정 이벤트(insert, update, delete)에 대한 응답으로 자동으로 실행되는 것

- ~ 하기 전/후에 ~ 하겠다

```sql
CREATE TRIGGER trigger name
{before | after} {insert | update | delect}
ON table name FOR EACH ROW
trigger_body;
```
- CREATE TRIGGER : 트리거 이름 지정
- 트리거 시점(커밋 전/후) 실행 작성
- ON 키워드 뒤 트리거에 속하는 테이블 지정

Q. 변경
```sql
-- 종료 구문을 //로 바꿔줘
DELIMITER //
CREATE TRIGGER mytrigger
	BEFORE UPDATE
    ON articles FOR EACH ROW
-- 다중구문 구성
BEGIN
	-- 트리커에서 특정 시점 전(OLD)/후(NEW) 값에 접근 할 수 있도록 제공하는 키워드
    SET NEW.updateAt = current_time();
END //
DELIMITER ;
```

Q. 삽입
```sql
DELIMITER //
CREATE TRIGGER log
	AFTER INSERT
    ON articles FOR EACH ROW
BEGIN
    INSERT INTO articlelogs (description, createdAt)
    VALUES(concat(NEW.id, "글이 작성 되었습니다."), current_time());
END //
DELIMITER ;
```

Q. 삭제
```sql
CREATE TRIGGER del
	BEFORE DELETE
    ON articles FOR EACH ROW
    INSERT INTO backuparticles(title, createdAt, updateAt)
    VALUES (OLD.title, OLD.createdAt, OLD.updateAt);
```

---
참고
error code: 2013, 2015

select * from information_schema.innodb_trx;

Kill [trx_mysql_tread_id1];

