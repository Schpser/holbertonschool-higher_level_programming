--DELETE TABLE IF IT EXISTS;
DROP TABLE IF EXISTS second_table;

--CREATE TABLE;
CREATE TABLE second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- DELETE OLD DATAS;
DELETE FROM second_table WHERE id IN (1, 2, 3, 4);

--ADD ROWS;
INSERT INTO second_table (id, name, score) VALUES 
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4,'George', 8);
