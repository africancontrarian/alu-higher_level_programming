Python - Object-relational mapping

This project links Python with MySQL databases in two ways: first with
the low-level `MySQLdb` driver (raw SQL queries), then with the
`SQLAlchemy` ORM, which maps Python classes to tables so no SQL has to
be written by hand.

## Requirements

- Ubuntu 20.04 LTS, `python3` (3.8.5)
- `MySQLdb` version 2.0.x
- `SQLAlchemy` version 1.4.x

## Files

### MySQLdb (raw SQL)

- `0-select_states.py` — list every state, sorted by id.
- `1-filter_states.py` — list states whose name starts with `N`.
- `2-my_filter_states.py` — filter states by a name argument (unsafe).
- `3-my_safe_filter_states.py` — the same, safe from SQL injection.
- `4-cities_by_state.py` — list every city with its state name.
- `5-filter_cities.py` — list the cities of a given state.

### SQLAlchemy ORM

- `model_state.py` / `model_city.py` — the `State` and `City` models.
- `6-model_state.py` — create the `states` table.
- `7-model_state_fetch_all.py` — list all states.
- `8-model_state_fetch_first.py` — print the first state.
- `9-model_state_filter_a.py` — list states containing an `a`.
- `10-model_state_my_get.py` — print the id of a state by name.
- `11-model_state_insert.py` — add the state `Louisiana`.
- `12-model_state_update_id_2.py` — rename state `id = 2`.
- `13-model_state_delete_a.py` — delete states containing an `a`.
- `14-model_city_fetch_by_state.py` — list cities with their state.

### Advanced — relationships

- `relationship_state.py` / `relationship_city.py` — models with a
  `cities`/`state` relationship and cascading delete.
- `100-relationship_states_cities.py` — create a state with a city.
- `101-relationship_states_cities_list.py` — list states then cities.
- `102-relationship_cities_states_list.py` — list cities then state.
