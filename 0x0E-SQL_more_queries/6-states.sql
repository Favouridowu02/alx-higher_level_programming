-- A Script that creates a database and a table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS `htbn_0d_usa`.`states` (
	PRIMARY KEY(`id`),
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256)) NOT NULL
);
