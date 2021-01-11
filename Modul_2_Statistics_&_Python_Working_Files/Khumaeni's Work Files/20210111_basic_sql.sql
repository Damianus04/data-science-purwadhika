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
INSERT INTO employee(name, gender, salary, city) VALUES('Nila', 'Female', 21000000, 'Bandung');

select * from employee;