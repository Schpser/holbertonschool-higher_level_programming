--CREATE TABLE;
CREATE TABLE second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

--ADD ROWS;
INSERT INTO second_table (id, name, score) VALUES 
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4,'George', 8);
ON DUPLICATE KEY UPDATE 
name = VALUES(name), 
score = VALUES(score);
