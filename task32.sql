CREATE TABLE author(
    authorID INT AUTO_INCREMENT,
    authorName VARCHAR(50) NOT NULL ,
    authorSurname VARCHAR(50) NOT NULL ,
    PRIMARY KEY (authorID)

);

CREATE TABLE book(
    bookID INT AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    publicationYear SMALLINT,
    authorID INT,
    PRIMARY KEY (bookID),
    FOREIGN KEY (authorID) REFERENCES Author(authorID)
);

INSERT INTO Author (authorName, authorSurname)
VALUES
('Alice', 'Walker'),
('Gabrie;', 'Garcia Marquez'),
('Haruki', 'Murakami'),
('Jane', 'Austen'),
('Fyodor', 'Dostoevsky');

INSERT INTO Book (title, publicationYear, authorID)
VALUES
('The color purple', 1982, 1),
('One Hundred Years of Solitude', 1967, 2),
('Kafka on the Shore', 2002, 3),
('Pride and Prejudice', 1813, 4),
('Crime and Punishment', 1866, 5);

UPDATE book
SET title = 'The Color Blue'
WHERE bookID = 1;

START TRANSACTION;
DELETE FROM book;
DELETE FROM author;
COMMIT;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS author;



