# 0x08. Python - Everything is object

Short-answer questions and one function about how CPython actually stores
and passes around values: identity (`is`) vs equality (`==`), mutable vs
immutable types, small-integer/empty-tuple caching, and how arguments are
passed into functions.

## Requirements

- Ubuntu 20.04 LTS, Python 3.8.5
- `.py` files: `#!/usr/bin/python3` shebang, executable, `pycodestyle` (2.7.*)
- `.txt` answer files: exactly one line, no shebang, no leading/trailing
  whitespace, ends with a newline

## Files

| File               | Contents                                                                |
|--------------------|--------------------------------------------------------------------------|
| `0-answer.txt`      | `type` — prints an object's type                                        |
| `1-answer.txt`      | `id` — prints an object's identifier (its memory address in CPython)    |
| `2`–`5-answer.txt`  | Identity (`is`) of small ints: caching applies to `-5..256`             |
| `6`–`13-answer.txt` | `==` vs `is` for strings and lists (equal value vs. same object)        |
| `14`–`18-answer.txt`| Mutation vs. rebinding: `.append()`/`+=` mutate in place; `x = x + y` and simple parameter reassignment inside a function do not |
| `19-copy_list.py`   | `copy_list(l)` — returns a shallow copy via `l[:]`                      |
| `20`–`23-answer.txt`| What actually makes something a tuple (the comma, not the parentheses) |
| `24`–`26-answer.txt`| Identity of "tuples" via CPython's caching quirks                       |
| `27`–`28-answer.txt`| `a = a + [x]` (new object) vs. `a += [x]` (same object, mutated)        |

## Two answers worth explaining

- **`9-answer.txt` (`False`)** — `s1 = "Best School"` and `s2 = "Best School"`
  typed as two separate REPL statements are *not* the same object. CPython
  interns string literals two different ways: identifier-safe strings
  (letters/digits/underscore only, like `"Best"` in task 7) get interned
  regardless of context, but `"Best School"` contains a space, so it only
  gets deduplicated when both literals are compiled together as constants
  in the *same* code object — which two separate REPL inputs never are.
  Run the identical code as one script instead of line-by-line at the
  prompt and this flips to `True`, which is exactly why the task presents
  it as a `>>>` session rather than a script.
- **`24`–`26-answer.txt` (`True`, `False`, `True`)** — `a = (1)` isn't a
  tuple at all (no comma, so it's just the int `1`), and small ints are
  cached, hence `True`. `a = (1, 2)` is a real 2-tuple, and CPython does
  *not* cache arbitrary tuples the way it caches small ints, hence `False`.
  `a = ()` is a real tuple too, but CPython specifically caches the empty
  tuple as a singleton (there's only ever one `()` object per process),
  hence `True` again despite the middle answer being `False`.

Both were checked against real interpreter behavior — using
`exec(compile(..., 'single'), ns)` per statement to faithfully reproduce
"typed one line at a time at the prompt" rather than "pasted as one
script" — before being written down, since the two execution modes give
different answers here.

## `19-copy_list.py`

```python
#!/usr/bin/python3
def copy_list(l):
    return l[:]
```

`l[:]` (a full slice) builds a new list object with the same elements,
which is why `new_list == my_list` is `True` but `new_list is my_list` is
`False`. The parameter name `l` is exactly what the task specifies, and
in this one case it's kept even though `pycodestyle` flags it as `E741`
("ambiguous variable name") — the task explicitly requires the signature
`def copy_list(l):`, and plain `pycodestyle` (unlike `flake8`) doesn't
honor `# noqa` comments to suppress that specific warning, so there was
no way to satisfy both constraints at once. Every other file in this
project is fully `pycodestyle`-clean.

## Author

africancontrarian
