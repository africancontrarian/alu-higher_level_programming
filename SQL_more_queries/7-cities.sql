-- Create the database hbtn_0d_usa, without failing if it already exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create the table cities in hbtn_0d_usa, without failing if it already
-- exists
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
);
