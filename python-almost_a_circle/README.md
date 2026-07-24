Python - Almost a circle

This project reviews the core of Python — imports, exceptions, classes,
private attributes, getters/setters, class and static methods,
inheritance, unit testing, reading/writing files, `*args`/`**kwargs`,
and JSON/CSV serialization — by building a small hierarchy of shapes.

## Directory

- `models/base.py` — the `Base` class: manages `id` and provides the
  JSON/CSV serialization and deserialization helpers.
- `models/rectangle.py` — the `Rectangle` class: a validated shape with
  a size, a position, and drawing/update/dictionary helpers.
- `models/square.py` — the `Square` class: a `Rectangle` whose width and
  height are always equal, exposed through a single `size` property.
- `tests/test_models/` — the `unittest` test suite mirroring the module
  layout.

## Running the tests

```
python3 -m unittest discover tests
```
