DROP TABLE users;

SET AUTOCOMMIT = 0;

CREATE TABLE users(
	id INT AUTO_INCREMENT,
    name VARBINARY(10) NOT NULL,
    PRIMARY KEY (id)
    );
    
START TRANSACTION;
INSERT INTO users (name)
VALUES ('harry'), ('test');
SELECT * FROM users;
ROLLBACK;

COMMIT; 


DROP TABLE articles;

CREATE TABLE articles(
	id INT AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    createdAt DATETIME NOT NULL,
    updateAt DATETIME NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO articles (title, createdAt, updateAt)
VALUES ("title1", current_time(), current_time());

SELECT * FROM articles;

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

SHOW TRIGGERS;

UPDATE articles
SET title = "new title"
WHERE id = 1;

SELECT * FROM articles;

CREATE TABLE articleLogs(
	id INT AUTO_INCREMENT,
    description VARCHAR(100) NOT NULL,
    createdAt DATETIME NOT NULL,
    PRIMARY KEY (id)
);


DELIMITER //
CREATE TRIGGER log
	AFTER INSERT
    ON articles FOR EACH ROW
BEGIN
    INSERT INTO articlelogs (description, createdAt)
    VALUES("글이 작성 되었습니다.", current_time());
END //
DELIMITER ;

SHOW TRIGGERS;

DROP TRIGGER log;

DELIMITER //
CREATE TRIGGER log
	AFTER INSERT
    ON articles FOR EACH ROW
BEGIN
    INSERT INTO articlelogs (description, createdAt)
    VALUES(concat(NEW.id, "글이 작성 되었습니다."), current_time());
END //
DELIMITER ;

INSERT INTO articles(title, createdAt, updateAt)
VALUES("title1", current_time(), current_time());

SELECT * FROM articles;
SELECT * FROM articlelogs;


CREATE TABLE backupArticles(
	id INT AUTO_INCREMENT, 
    title VARCHAR(100) NOT NULL,
    createdAt DATETIME NOT NULL, 
    updatedAt DATETIME NOT NULL,
    PRIMARY KEY (id)
);

CREATE TRIGGER del
	BEFORE DELETE
    ON articles FOR EACH ROW
    INSERT INTO backuparticles(title, createdAt, updateAt)
    VALUES (OLD.title, OLD.createdAt, OLD.updateAt);

DELETE FROM articles
WHERE id = 1;

SELECT * FROM backuparticles;
