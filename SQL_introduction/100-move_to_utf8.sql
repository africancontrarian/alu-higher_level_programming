-- Convert the hbtn_0c_0 database to utf8mb4
ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Convert first_table to utf8mb4
ALTER TABLE hbtn_0c_0.first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Change only the column collation
ALTER TABLE hbtn_0c_0.first_table
MODIFY name VARCHAR(256) COLLATE utf8mb4_unicode_ci;
