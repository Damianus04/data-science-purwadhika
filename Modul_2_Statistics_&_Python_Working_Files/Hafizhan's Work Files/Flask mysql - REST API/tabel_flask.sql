CREATE DATABASE flask_mysql;

USE flask_mysql;

CREATE TABLE employee (
id INT(6) AUTO_INCREMENT PRIMARY KEY, -- 123456 (7 ga muncul). range is from -2147483648 to 2.147.483.647
username VARCHAR(20) UNIQUE,          -- 20 karakter
name VARCHAR(20) NOT NULL,            -- 20 karakter
gender enum('M','F'),                 -- pilihan M or F
married tinyint                       -- range data lebih kecil (Signed range is from -128 to 127)
);

