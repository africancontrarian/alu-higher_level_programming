# SQL - Introduction

Basic MySQL: creating and dropping databases, creating tables, and the
core DDL/DML statements (`SELECT`, `INSERT`, `UPDATE`, `DELETE`) plus
simple functions (`COUNT`, `AVG`) and `GROUP BY`.

## Requirements

- Ubuntu 20.04 LTS, MySQL 8.0 (8.0.25)
- Every `.sql` file starts with a comment describing the task, and every
  query has a comment directly above it
- All SQL keywords are uppercase
- Scripts are run as: `cat script.sql | mysql -hlocalhost -uroot -p [database]`

## Files

| File                                 | Contents                                                        |
|----------------------------------------|--------------------------------------------------------------------|
| `0-list_databases.sql`                 | List all databases                                              |
| `1-create_database_if_missing.sql`     | `CREATE DATABASE IF NOT EXISTS hbtn_0c_0`                        |
| `2-remove_database.sql`                | `DROP DATABASE IF EXISTS hbtn_0c_0`                              |
| `3-list_tables.sql`                    | List all tables of the database passed as argument              |
| `4-first_table.sql`                    | Create `first_table (id INT, name VARCHAR(256))`                 |
| `5-full_table.sql`                     | Print `first_table`'s full `CREATE TABLE` description            |
| `6-list_values.sql`                    | List all rows of `first_table`                                   |
| `7-insert_value.sql`                   | Insert `(89, "Best School")` into `first_table`                  |
| `8-count_89.sql`                       | Count records with `id = 89` in `first_table`                    |
| `9-full_creation.sql`                  | Create `second_table` and insert 4 records                       |
| `10-top_score.sql`                     | List `second_table`, ordered by score descending                 |
| `11-best_score.sql`                    | List `second_table` records with `score >= 10`                   |
| `12-no_cheating.sql`                   | Set Bob's score to 10, matched by name only                      |
| `13-change_class.sql`                  | Delete records with `score <= 5`                                 |
| `14-average.sql`                       | Compute the average score (column `average`)                     |
| `15-groups.sql`                        | Count records per score, ordered by count descending             |
| `16-no_link.sql`                       | List records with a non-`NULL` name, ordered by score descending |
