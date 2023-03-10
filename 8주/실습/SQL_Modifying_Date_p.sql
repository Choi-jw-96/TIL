-- 문제 1
CREATE TABLE users (
	userID int NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL, 
    birthday DATE NOT NULL,
    city VARCHAR(100), 
    country VARCHAR(100),
    email VARCHAR(100),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (userID)
    );

SHOW COLUMNS FROM users;



-- 문제 2
INSERT INTO 
	users(first_name, last_name, birthday, city, country, email)
VALUES
	("Beemo", "Jeong", "1000-01-01", NULL, NULL, "beemo@hphk.kr"),
    ("Jieun", "Lee", "1993-05-16", "Seoul", "Korea", NULL),
	("Dami", "Kim", "1995-04-09", "Seoul", "Korea", NULL)	,
	("Kwangsoo", "Lee", "1985-07-14", "Seoul", "Korea", NULL);
    
SELECT * FROM users;



-- 문제 3
INSERT INTO 
	users(first_name, last_name, birthday, city, country, email)
VALUES
	("f_1", "l_1", "1111-11-11", NULL, NULL, NULL),
    ("f_2", "l_2", "1111-11-11", NULL, NULL, NULL),
    ("f_3", "l_3", "1111-11-11", NULL, "America", NULL),
    ("f_4", "l_4", "1111-11-11", NULL, NULL, NULL),
    ("f_5", "l_5", "1111-11-11", NULL, NULL, NULL);


SELECT * FROM users;


-- 문제 4
UPDATE users
set
	first_name = "Jiwon",
    last_name = "Choi",
    birthday = "1996-09-17"
WHERE
	userID = 2;
    
SELECT * FROM users;


-- 문제 5
UPDATE users
set
	country = ifnull(country, "Korea");
    
SELECT * FROM users;

-- 문제 6
DELETE FROM users
WHERE 
	first_name = "Beemo";
    
SELECT * FROM users;


-- 문제 7
DELETE FROM users
WHERE 
	first_name = "Kwangsoo"
    and
    last_name = "Lee";
SELECT * FROM users;


-- 문제 8
DELETE FROM users
ORDER BY
	created_at DESC
LIMIT 1;

SELECT * FROM users;