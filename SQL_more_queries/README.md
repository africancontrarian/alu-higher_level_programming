# SQL - More queries

MySQL users and privileges, column constraints (`NOT NULL`, `UNIQUE`,
`DEFAULT`), foreign keys, subqueries, and `JOIN`s (`INNER`/`LEFT`) across
multiple tables.

## Requirements

- Ubuntu 20.04 LTS, MySQL 8.0 (8.0.25)
- Every `.sql` file starts with a comment describing the task, and every
  query has a comment directly above it
- All SQL keywords are uppercase
- Scripts are run as: `cat script.sql | mysql -hlocalhost -uroot -p [database]`

## Files

| File                                        | Contents                                                          |
|----------------------------------------------|----------------------------------------------------------------------|
| `0-privileges.sql`                            | `SHOW GRANTS` for `user_0d_1` and `user_0d_2`                       |
| `1-create_user.sql`                           | Create user `user_0d_1`                                             |
| `2-create_read_user.sql`                      | Create database `hbtn_0d_2` and a `SELECT`-only user `user_0d_2`    |
| `3-force_name.sql`                            | Create `force_name (id INT, name VARCHAR(256) NOT NULL)`             |
| `4-never_empty.sql`                           | Create `id_not_null (id INT DEFAULT 1, name VARCHAR(256))`           |
| `5-unique_id.sql`                             | Create `unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256))`      |
| `6-states.sql`                                | Create database `hbtn_0d_usa` and table `states`                     |
| `7-cities.sql`                                | Create table `cities`, `state_id` foreign key to `states.id`         |
| `8-cities_of_california_subquery.sql`         | Cities of California, found via subquery                             |
| `9-cities_by_state_join.sql`                  | Cities joined with their state name, ordered by city id              |
| `10-genre_id_by_show.sql`                     | Shows with at least one genre linked (`INNER JOIN`)                  |
| `11-genre_id_all_shows.sql`                   | All shows, `NULL` genre if none linked (`LEFT JOIN`)                 |
| `12-no_genre.sql`                             | Shows with no genre linked                                           |
| `13-count_shows_by_genre.sql`                 | Genres with their show count, ordered descending                     |
| `14-my_genres.sql`                            | All genres of the show `Dexter`                                      |
| `15-comedy_only.sql`                          | All `Comedy` shows                                                   |
| `16-shows_by_genre.sql`                       | All shows with their genre(s), `NULL` if none                        |
| `100-not_my_genres.sql`                       | Genres not linked to the show `Dexter`                                |
| `101-not_a_comedy.sql`                        | Shows not linked to the `Comedy` genre                                |
| `102-rating_shows.sql`                        | Shows by rating (sum), descending                                     |
| `103-rating_genres.sql`                       | Genres by rating (sum), descending                                    |

Tasks 10-16 and 100-101 query the `hbtn_0d_tvshows` database dump
provided with the project (`tv_shows(id, title)`, `tv_genres(id, name)`,
`tv_show_genres(show_id, genre_id)`). Tasks 102-103 query a separate
`hbtn_0d_tvshows_rate` dump, adding a `tv_show_ratings(show_id, rate)`
table. The scripts themselves only contain the queries.
