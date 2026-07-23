# 0x0A. Python - Input/Output

File I/O and JSON serialization: reading and writing text files with the
`with` statement, converting Python data structures to and from JSON, and
a small `Student` class used to demonstrate a full serialize -> save ->
load -> deserialize round trip.

## Requirements

- Ubuntu 20.04 LTS, Python 3.8.5
- `.py` files: `#!/usr/bin/python3` shebang, executable, `pycodestyle` (2.7.*)
- Every module, class, and function/method has a real, descriptive docstring

## Files

| File                       | Contents                                                              |
|-----------------------------|------------------------------------------------------------------------|
| `0-read_file.py`             | `read_file(filename)` — print a UTF8 file's content                  |
| `1-write_file.py`            | `write_file(filename, text)` — write/overwrite, returns char count   |
| `2-append_write.py`          | `append_write(filename, text)` — append, returns char count added    |
| `3-to_json_string.py`        | `to_json_string(my_obj)` — object to JSON string                     |
| `4-from_json_string.py`      | `from_json_string(my_str)` — JSON string to object                   |
| `5-save_to_json_file.py`     | `save_to_json_file(my_obj, filename)` — object to JSON file          |
| `6-load_from_json_file.py`   | `load_from_json_file(filename)` — JSON file to object                |
| `7-add_item.py`              | Script: appends `argv[1:]` to `add_item.json`                        |
| `8-class_to_json.py`         | `class_to_json(obj)` — an instance's serializable attributes         |
| `9-student.py`               | `Student` with `to_json()`                                            |
| `10-student.py`              | `Student` with `to_json(attrs=None)` attribute filtering              |
| `11-student.py`              | `Student` adds `reload_from_json(json)` for a full round trip        |
| `12-pascal_triangle.py`      | `pascal_triangle(n)` — Pascal's triangle as a list of lists          |
| `100-append_after.py`        | `append_after(filename, search_string, new_string)` — insert a line after every matching line |
| `101-stats.py`               | Script: reads HTTP access logs from stdin, prints size/status-code metrics every 10 lines and on interrupt |
