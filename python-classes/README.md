# 0x06. Python - Classes and Objects

An introduction to Object-Oriented Programming in Python, built incrementally
through a single `Square` class: private attributes, instantiation,
validation, properties (Pythonic getters/setters), and instance methods.

## Learning Objectives

By the end of this project you should be able to explain, without help:

- What OOP is, and what "first-class everything" means in Python
- What a class, an object, and an instance are — and how they differ
- What an attribute is, and what `self` refers to
- Public, protected, and private attributes
- What a method is, and what `__init__` does
- Data abstraction, encapsulation, and information hiding
- What a property is, and how it differs from a plain attribute
- The Pythonic way to write getters and setters (`@property`)
- How Python looks up attributes, `__dict__`, and `getattr`

## Requirements

- Ubuntu 20.04 LTS, Python 3.8.5
- All files start with `#!/usr/bin/python3`, end with a newline, and are
  executable
- `pycodestyle` (2.7.*) compliant
- Every module, class, and function/method has a real, descriptive docstring
- No imports used anywhere in this project

## Files

| File          | Adds on top of the previous file                                          |
|---------------|------------------------------------------------------------------------------|
| `0-square.py` | An empty `Square` class                                                      |
| `1-square.py` | Private `size` attribute, no validation, mandatory `size` argument           |
| `2-square.py` | `size` validation (`TypeError`/`ValueError`), `size` now optional (default `0`) |
| `3-square.py` | `area()` method                                                              |
| `4-square.py` | `size` becomes a property (getter + validating setter)                       |
| `5-square.py` | `my_print()` — prints the square with `#`; an empty line if `size` is `0`    |
| `6-square.py` | `position` property (2 non-negative ints); `my_print()` honors it            |

## Usage

Each file is self-contained and can be run through a matching test/main
script, e.g.:

```bash
$ cat > 6-main.py << 'EOF'
#!/usr/bin/python3
Square = __import__('6-square').Square

my_square = Square(3, (2, 1))
my_square.my_print()
EOF
$ chmod +x 6-main.py
$ ./6-main.py
```

Or interactively:

```bash
$ python3
>>> Square = __import__('4-square').Square
>>> s = Square(5)
>>> s.area()
25
```

## `position` in `6-square.py`

`position` is a tuple `(x, y)` of 2 non-negative integers used only by
`my_print()`:

- `x` (`position[0]`) adds that many leading spaces to every printed row
- `y` (`position[1]`) adds that many blank lines above the square
- Rows are never padded with trailing spaces

## Author

africancontrarian
