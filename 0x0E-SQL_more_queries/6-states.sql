-- Get all DB of server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
    id INT UNIQUE NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT null,
    PRIMARY KEY (id)
);
