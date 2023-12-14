-- Get all DB of server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
    id INT UNIQUE NOT NULL AUTO_INCREMENT,
    state_id INT NOT null,
    name VARCHAR(256) NOT null,
    FOREIGN KEY(state_id) REFERENCES states(id)),
    PRIMARY KEY (id)
    );
