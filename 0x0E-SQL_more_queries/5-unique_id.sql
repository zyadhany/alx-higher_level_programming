-- Get all DB of server.
CREATE TABLE if NOT EXISTS id_not_null (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
