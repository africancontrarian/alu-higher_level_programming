-- Create the database hbtn_0d_usa, without failing if it already exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create the table states in hbtn_0d_usa, without failing if it already
-- exists
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
