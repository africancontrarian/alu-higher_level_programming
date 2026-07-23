# 0x09. Python - Inheritance

Class hierarchies built on top of `object`: introspecting attributes with
`dir`, comparing classes with `type`/`isinstance`/`issubclass`, and a small
`BaseGeometry` → `Rectangle` → `Square` hierarchy that shows attribute
privacy, validation, and method overriding through inheritance.

## Requirements

- Ubuntu 20.04 LTS, Python 3.8.5
- `.py` files: `#!/usr/bin/python3` shebang, executable, `pycodestyle` (2.7.*)
- Every module, class, and function/method has a real, descriptive docstring
- Doctest files live under `tests/` and run with `python3 -m doctest ./tests/*`

## Files

| File                    | Contents                                                              |
|-------------------------|------------------------------------------------------------------------|
| `0-lookup.py`            | `lookup(obj)` — list of an object's attributes and methods            |
| `1-my_list.py`           | `MyList`, a `list` subclass with `print_sorted()`                     |
| `2-is_same_class.py`     | `is_same_class(obj, a_class)` — exact type match                      |
| `3-is_kind_of_class.py`  | `is_kind_of_class(obj, a_class)` — `isinstance`-style check            |
| `4-inherits_from.py`     | `inherits_from(obj, a_class)` — true subclass check (excludes exact)  |
| `5-base_geometry.py`     | Empty `BaseGeometry` class                                             |
| `6-base_geometry.py`     | `BaseGeometry` with an unimplemented `area()`                         |
| `7-base_geometry.py`     | `BaseGeometry` with `area()` and `integer_validator()`                |
| `8-rectangle.py`         | `Rectangle(BaseGeometry)` with private, validated `width`/`height`    |
| `9-rectangle.py`         | `Rectangle` with `area()` and `__str__`                                |
| `10-square.py`           | `Square(Rectangle)` built from a single `size`                        |
| `11-square.py`           | `Square` with its own `__str__`                                        |
| `tests/1-my_list.txt`    | Doctest coverage for `MyList`                                          |
| `tests/7-base_geometry.txt` | Doctest coverage for `BaseGeometry`                                |
