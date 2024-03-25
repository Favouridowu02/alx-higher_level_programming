-- A Script that creates a database and a table states
CREATE DATABASE hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE states(
	id INT UNIQUE AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256));
