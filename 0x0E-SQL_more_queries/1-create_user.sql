-- A script to create a user with all priviledges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES *.* to 'user_0d_1'@'localhost';
