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
| `100-singly_linked_list.py` | `Node` (data + next_node) and `SinglyLinkedList` (sorted insert, printable) |
| `101-square.py` | `Square` (based on `6-square.py`) is printable via `print()`, same output as `my_print()` |
| `102-square.py` | `Square` (based on `4-square.py`) supports `==`, `!=`, `<`, `<=`, `>`, `>=` by area |
| `103-magic_class.py` | `MagicClass` — a circle class reconstructed from disassembled bytecode |

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

## Advanced tasks

### `100-singly_linked_list.py`

`Node` holds an integer `data` and an optional `next_node` (must be `None`
or another `Node`). `SinglyLinkedList` keeps a private `head` and exposes
`sorted_insert(value)`, which walks the list to insert a new `Node` in
increasing order. Printing a list (`print(sll)`) prints each node's data
on its own line.

### `101-square.py`

Same `Square` as `6-square.py`, plus a `__str__` method so `print(square)`
produces byte-for-byte the same output as `square.my_print()` — `my_print()`
is implemented as `print(self)` to guarantee they can never drift apart.
Note: this file's `position` setter raises `TypeError` with the message
`position must be a tuple of 2 positive integer` (singular), which is the
exact wording this task's rubric specifies — intentionally different from
`6-square.py`'s `...2 positive integers` (plural).

### `102-square.py`

Same `Square` shape as `4-square.py`, except `size` now accepts `int` or
`float` (`size must be a number` on a bad type), and the class defines
`__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, and `__ge__` so two
squares can be compared directly (`s_5 < s_6`), each comparison based on
`area()`.

### `103-magic_class.py`

`MagicClass` is a circle (radius, `area()`, `circumference()`) rebuilt by
reading the disassembled Python bytecode given in the task rather than
from a written spec — `radius` must be an `int` or `float`
(`radius must be a number` otherwise), and `area()`/`circumference()` use
`math.pi`, the one file in this project where an import is required
(and explicitly allowed) rather than forbidden.

## Author

africancontrarian
