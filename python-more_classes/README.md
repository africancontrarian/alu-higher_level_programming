# 0x07. Python - More Classes and Objects

A deeper dive into Object-Oriented Programming in Python, built through a
`Rectangle` class: class vs. instance attributes, `__str__`/`__repr__`,
`__del__`, static methods, and class methods.

## Learning Objectives

By the end of this project you should be able to explain, without help:

- What a class attribute is, and how it differs from an instance attribute
- What `__str__` and `__repr__` are for, and how they differ
- What a class method is, and what a static method is
- How to dynamically create new attributes on an existing instance
- What `__dict__` contains, for a class and for an instance
- How Python resolves attribute lookups, and how `getattr` works

## Requirements

- Ubuntu 20.04 LTS, Python 3.8.5
- All files start with `#!/usr/bin/python3`, end with a newline, and are
  executable
- `pycodestyle` (2.7.*) compliant
- No imports used anywhere in this project

## Files

Each file is cumulative — it adds one feature on top of the previous file.

| File            | Adds on top of the previous file                                          |
|-----------------|------------------------------------------------------------------------------|
| `0-rectangle.py` | An empty `Rectangle` class                                                  |
| `1-rectangle.py` | Private `width`/`height` as validated properties                            |
| `2-rectangle.py` | `area()` and `perimeter()` (perimeter is 0 if either side is 0)             |
| `3-rectangle.py` | `__str__` — prints the rectangle with `#` (`""` if either side is 0)        |
| `4-rectangle.py` | `__repr__` — `eval(repr(r))` recreates an equal, distinct instance          |
| `5-rectangle.py` | `__del__` — prints `Bye rectangle...` when an instance is deleted           |
| `6-rectangle.py` | `number_of_instances` class attribute, tracked in `__init__`/`__del__`      |
| `7-rectangle.py` | `print_symbol` class attribute — `__str__` uses it instead of a fixed `#`   |
| `8-rectangle.py` | `bigger_or_equal()` static method — compares two rectangles by area         |
| `9-rectangle.py` | `square()` class method — builds a `Rectangle` with `width == height`       |
| `101-nqueens.py` | N queens solver (backtracking) — independent of the `Rectangle` series      |

## Usage

Each file is self-contained and can be run through a matching test/main
script, e.g.:

```bash
$ cat > 9-main.py << 'EOF'
#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {}".format(my_square.area()))
print(my_square)
EOF
$ chmod +x 9-main.py
$ ./9-main.py
```

Or interactively:

```bash
$ python3
>>> Rectangle = __import__('7-rectangle').Rectangle
>>> r = Rectangle(4, 2)
>>> r.print_symbol = "*"
>>> print(r)
****
****
```

## A couple of notes

- In `1-rectangle.py` onward, `__init__` validates/sets `width` before
  `height`. This matters beyond `__dict__` ordering: `9-rectangle.py`'s
  `square(size)` calls `cls(size, size)`, so on an invalid `size` (e.g.
  `Rectangle.square(-2)`), whichever attribute is assigned first is the
  one named in the raised error — the checker expects `width must be...`,
  not `height must be...`, so `width` has to go first.
- `print_symbol` (from `7-rectangle.py` on) is looked up via plain
  `self.print_symbol`, not a private/mangled name, so it naturally picks
  up either a per-instance override (`my_rect.print_symbol = "&"`) or a
  class-wide change (`Rectangle.print_symbol = "C"`) with no extra code.

## `101-nqueens.py`

Solves the N queens puzzle with classic row-by-row backtracking: place a
queen in the first open row at every column that isn't attacked by a
queen already placed, recurse, and undo (`board[row] = -1`) whenever a
branch runs out of safe columns. Each complete placement is printed as
`[[row, col], [row, col], ...]`.

```bash
$ ./101-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

Validation, in order: wrong argument count → `Usage: nqueens N`; `N` not
parseable as an int → `N must be a number`; `N < 4` → `N must be at
least 4`. All three exit with status 1.

## Author

africancontrarian
