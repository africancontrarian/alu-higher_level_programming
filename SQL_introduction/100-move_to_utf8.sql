-- Convert the hbtn_0c_0 database, its first_table, and the name column
-- of first_table to utf8mb4 with the utf8mb4_unicode_ci collation
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Set first_table's default character set to utf8mb4
ALTER TABLE hbtn_0c_0.first_table CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Explicitly convert the name column to utf8mb4
ALTER TABLE hbtn_0c_0.first_table MODIFY name VARCHAR(256) COLLATE utf8mb4_unicode_ci;
