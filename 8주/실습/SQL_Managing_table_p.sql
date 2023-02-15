-- 문제 1
CREATE TABLE posts(
	postID INT AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    content VARCHAR(200) NOT NULL,
    PRIMARY KEY (postID)
    );
    
SHOW COLUMNS FROM posts;

-- 문제 2 
ALTER TABLE
	posts
ADD
	-- null = yes & Default 값 설정 & current_timestamp 하면 extre 자동 설정
	(writer VARCHAR(100) DEFAULT "Anonymous",
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP);

SHOW COLUMNS FROM posts;


-- 문제 3
ALTER TABLE
	posts
MODIFY
	content TEXT;
SHOW COLUMNS FROM posts;



-- 문제 4
ALTER TABLE
	posts
DROP writer;

SHOW COLUMNS FROM posts;


-- 문제 5
DROP TABLE posts;

-- 문제 6 
--  해당 테이블이 존재하지 않으면 생성
CREATE TABLE IF NOT EXISTS post(
	postID INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    content TEXT NOT NULL,
    writer VARCHAR(20) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (postID)
    );
    

-- 문제 7
DROP TABLE IF EXISTS post;



    
