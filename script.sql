-- Create the database "BookStore"
CREATE DATABASE BookStore;

-- Create the table "books"
USE BookStore;
CREATE TABLE books (
    SKU INTEGER PRIMARY KEY,
    Category TEXT,
    Name TEXT,
    Author TEXT,
    Publisher TEXT,
    Price REAL,
    Synopsis TEXT,
    Discount REAL NOT NULL DEFAULT 0.0
);

-- Insert into the table 30 books from 3 different book genres
INSERT INTO books (SKU, Category, Name, Author, Publisher, Price, Synopsis)
VALUES
    -- Genre 1 books
    (1, 'ادب عربى', 'هذا هو إسمي', 'ادونيس', 'دار الاداب', 180.00, 'Synopsis 1'),
    (2, 'ادب عربى', 'Book 2', 'Author 2', 'Publisher 1', 200.00, 'Synopsis 2'),
    (3, 'ادب عربى', 'Book 3', 'Author 3', 'Publisher 2', 140.00, 'Synopsis 3'),
    -- Genre 2 books
    (4, 'أدب مترجم', 'Book 4', 'Author 4', 'Publisher 3', 220.00, 'Synopsis 4'),
    (5, 'أدب مترجم', 'Book 5', 'Author 5', 'Publisher 4', 190.00, 'Synopsis 5'),
    (6, 'أدب مترجم', 'Book 6', 'Author 6', 'Publisher 4', 250.00, 'Synopsis 6'),
    -- Genre 3 books
    (7, 'دراسات أدبية', 'Book 7', 'Author 7', 'Publisher 5', 80.00, 'Synopsis 7'),
    (8, 'دراسات أدبية', 'Book 8', 'Author 8', 'Publisher 6', 110.00, 'Synopsis 8'),
    (9, 'دراسات أدبية', 'Book 9', 'Author 9', 'Publisher 7', 130.00, 'Synopsis 9');
    -

-- Search for books priced between 100.00 and 200.00 pounds
SELECT *
FROM books
WHERE Price > 100.00 AND Price <= 200.00;

-- Show unique publishers and the number of books they have published
SELECT DISTINCT Publisher, COUNT(Publisher)
FROM books
GROUP BY Publisher;

-- Arrange the previous result in descending order
SELECT DISTINCT Publisher, COUNT(Publisher)
FROM books
GROUP BY Publisher
ORDER BY COUNT(Publisher) DESC;

-- Apply the specified discount rates to the book prices and display the final prices
SELECT Name, (Price * (100.0 - Discount) / 100.0) AS final_price
FROM books
ORDER BY final_price DESC;

-- Delete records with a discount rate of 0.0 and publishers with more than 3 books
DELETE FROM books
WHERE Discount = 0.0 AND Publisher IN (
    SELECT Publisher
    FROM books
    GROUP BY Publisher
    HAVING COUNT(Publisher) > 3
);
