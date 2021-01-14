-- show databases; 
-- create database toko;
-- show databases;

-- use toko;
-- show tables; 

-- > new database
-- create database sales;
-- use sales;

-- > new table
-- create table Assets (noAsset TinyInt, Name char(30), stock smallint);  
-- create table Coba(NoCoba tinyint);

-- > show table
-- show tables;

-- > delete table
-- drop table Coba;


-- > insert data
-- INSERT INTO Assets VALUES(1, 'Book', 60);
-- INSERT INTO Assets (Name, noAsset, stock) VALUES ('Pen', 23, 120);
-- INSERT INTO Assets VALUES
-- (15, 'Table', 86),
-- (20, 'Cupboard', 65),
-- (31, 'PC', 20);
-- select * from Assets;

-- > update data
-- UPDATE Assets SET stock=240 WHERE Name='PC';

-- > add column
-- ALTER TABLE employee ADD COLUMN 
-- age TINYINT DEFAULT 23 AFTER name; -- AFTER is to positioning in certain place

-- > shift column position
-- ALTER TABLE employee MODIFY COLUMN
-- age tinyint AFTER city;

-- > change column name
-- ALTER TABLE employee RENAME COLUMN
-- age TO age_range;

-- > delete column
-- ALTER TABLE employee DROP COLUMN
-- age;

-- > change data type of column
-- ALTER TABLE employee MODIFY COLUMN
-- city varchar(50);


-- > sorting the data
-- SELECT name, city, salary FROM employee
-- -- ORDER BY salary; -- ORDER BY salary ASC
-- ORDER BY salary DESC;


-- > reading the data
-- 1. select
-- 2. from
-- 3. where (having -> if syntectic column)
-- 4. like
-- 5. group by
-- 6. order by
-- 7. limit


-- SELECT name, city, salary FROM employee
-- ORDER BY city DESC, salary;

-- SELECT name, city, salary FROM employee
-- ORDER BY city DESC, salary;

-- SELECT name, city, salary FROM employee
-- WHERE city!='Jakarta';

-- SELECT name, city, salary FROM employee 
-- WHERE salary > 20000000 ORDER BY salary;

-- > HAVING is for syntetic column
-- > WHERE is for original column
-- SELECT name, city, 0.2*salary AS increment FROM employee
-- HAVING increment > 3000000;

-- > LIKE
-- SELECT name, city, salary FROM employee
-- WHERE name LIKE '%y';
-- SELECT name, city, salary FROM employee
-- WHERE name LIKE 'C%y%';


-- CREATE TABLE employee (
-- employeeID mediumint not null auto_increment,
-- name char(50) DEFAULT 'Anonymous',
-- gender ENUM('Male', 'Female') default 'Male',
-- salary INT DEFAULT 10000000,
-- city char(25) DEFAULT 'Jakarta',
-- time_created timestamp DEFAULT current_timestamp,
-- Primary Key (employeeID)
-- );

-- INSERT INTO employee (name, gender, salary) VALUES
-- ('Ali', 'Male', 15000000); -- only insert 3 columns and others are default
-- INSERT INTO employee (name) VALUES ('Deni'); -- only insert 1 column and others are default
-- INSERT INTO employee(city) VALUES('Malang');
-- UPDATE employee SET name='Rendi' WHERE name='Anonymous';
-- INSERT INTO employee (name, gender, salary, city) VALUES
-- ('Rey', 'Male', 25000000, 'Malang'),
-- ('Sisca', 'Female', 30000000, 'Bandung'),
-- ('Jeki', 'Male', 12000000, 'Bandung'),
-- ('Cindy', 'Female', 25000000, 'Jakarta'),
-- ('Cindy', 'Female', 20000000, 'Bandung'),
-- ('Devy', 'Female', 17000000, 'Malang'),
-- ('Andre', 'Male', 25000000, 'Bandung'),
-- ('Dito', 'Male', 15000000, 'Jakarta'),
-- ('Rio', 'Male', 20000000, 'Bandung');

-- DELETE FROM employee WHERE name='Rendi';
-- INSERT INTO employee(name, gender) VALUES('Lulu', 'Female');
-- INSERT INTO employee(name, salary, city) VALUES('Beni', 30000000, 'Malang');
-- INSERT INTO employee(name, gender, salary, city) VALUES('Nila', 'Female', 21000000, 'Bandung');
-- INSERT INTO employee(name) VALUES
-- ('Billy'),
-- ('Kimberly'),
-- ('Tommy');

-- UPDATE employee SET age_range=21
-- WHERE name='Devy';

-- SELECT name, salary, age_range FROM employee;
-- SELECT name, salary, 0.2*salary AS final_salary
-- FROM employee;

-- SELECT name, city, salary FROM employee
-- ORDER BY city DESC, salary;

-- SELECT name, city, salary FROM employee
-- WHERE city!='Jakarta';

-- SELECT name, city, salary FROM employee 
-- WHERE salary > 20000000 ORDER BY salary;

-- SELECT name, city, salary FROM employee
-- WHERE city IN ('Bandung', 'Jakarta');

-- SELECT name, city, salary FROM employee
-- WHERE city NOT IN ('Jakarta', 'Bandung') ORDER BY salary;

-- SELECT name, city, salary FROM employee
-- WHERE city='Jakarta' AND salary<20000000;

-- SELECT name, city, salary FROM employee
-- WHERE salary BETWEEN 15000000 AND 25000000;

-- SELECT name, city, salary FROM employee
-- WHERE salary >=15000000 AND salary <= 25000000;

-- SELECT name, city, 0.2*salary AS increment FROM employee
-- HAVING increment > 3000000;

-- SELECT name, city, salary FROM employee
-- WHERE name LIKE 'Deni';

-- SELECT name, city, salary FROM employee
-- WHERE name LIKE '%y';

-- SELECT name, city, salary FROM employee
-- WHERE name LIKE 'C%y%';

-- SELECT name, city, salary FROM employee
-- ORDER BY salary DESC LIMIT 5;

-- SELECT name, city, salary FROM employee
-- WHERE city IN ('Jakarta', 'Malang') 
-- ORDER BY salary DESC
-- LIMIT 3;

-- SELECT * FROM employee
-- LIMIT 3, 4;

-- SELECT name, city, salary FROM employee 
-- WHERE city!='Jakarta' 
-- ORDER BY salary DESC
-- LIMIT 4,3;

-- SELECT name, city, salary FROM employee
-- WHERE city='Jakarta' AND salary>20000000;

-- SELECT name, city, salary FROM employee
-- WHERE salary BETWEEN 15000000 AND 25000000;

-- SELECT name, city, 0.2*salary AS increment FROM employee
-- HAVING increment > 3000000;

-- SELECT name, city, salary FROM employee
-- WHERE name LIKE '%t%';

-- SELECT * FROM employee
-- ORDER BY salary
-- LIMIT 5;

-- > agregation
-- (SUM, AVG, MAX, MIN) + HAVING + ORDER BY --> for numeric
-- ORDER BY --> for non-numeric
-- SELECT SUM(salary) FROM employee;
-- SELECT SUM(salary) AS total, city FROM employee
-- GROUP BY city;

-- SELECT SUM(salary) AS total, city FROM employee
-- WHERE city IN ('Jakarta', 'Bandung')
-- GROUP BY city;

-- SELECT SUM(salary) AS total, city FROM employee
-- WHERE city IN ('Jakarta', 'Bandung')
-- GROUP BY city
-- HAVING total > 8000000
-- ORDER BY total;

-- SELECT AVG(salary) AS average, city FROM employee
-- GROUP BY city;

-- SELECT SUM(salary) AS total, city FROM employee
-- WHERE salary > 
-- 	(SELECT AVG(salary) AS average FROM employee
--     HAVING salary > average);

SELECT SUM(salary) AS total, city FROM employee
WHERE salary > 
	(SELECT AVG(salary) AS average FROM employee
    HAVING salary > average) 
    GROUP BY city;
    
