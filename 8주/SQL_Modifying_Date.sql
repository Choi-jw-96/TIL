CREATE TABLE articles(
	id INT AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    content VARCHAR(2articles00) NOT NULL,
    createdAt DATE NOT NULL,
    PRIMARY KEY (id)
    );
    
SHOW COLUMNS FROM articles;

SELECT * FROM articles;

INSERT INTO articles(title, content, createdAt)
VALUES ('hello', 'world', '2000-01-01'),
	("title1", "contnent1", "1900-01-01"),
    ("title2", "contnent2", "1800-01-01"),
    ("title3", "contnent3", "1700-01-01");

INSERT INTO articles(title, content, createdAt)
VALUES ('mytitle', 'mycontent', curdate());

UPDATE articles
SET title = "newTitle"
WHERE
	id = 1;
    
UPDATE articles
SET title = "newTitle",
	content = "newContent2"
WHERE id = 3;

UPDATE articles
SET content = replace(content, "contnent", "TEST");

SET SQL_SAFE_UPDATES = 0; 

DELETE FROM articles
WHERE id = 1;


SELECT * FROM articles
ORDER BY createdAt DESC;

DELETE FROM 
	articles
ORDER BY
	createdAt DESC
LIMIT 2;

