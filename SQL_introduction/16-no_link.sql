-- List all records of second_table that have a name, displaying the
-- score and the name, ordered by score (highest first)
SELECT score, name FROM second_table
    WHERE name IS NOT NULL ORDER BY score DESC;
