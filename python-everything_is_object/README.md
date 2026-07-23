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

- **`9-answer.txt` (`True`)** and **`25-answer.txt` (`True`)** — same
  underlying mechanism. When CPython compiles a block of code as one
  unit, identical immutable literals (strings, and tuples made only of
  constants) get folded down to a single shared object in that unit's
  constants table — so `s1 = "Best School"` / `s2 = "Best School"` end up
  `is`-identical, and so do `a = (1, 2)` / `b = (1, 2)`. This checker
  evaluates the `>>>` sequence as one compiled unit, so that's the
  behavior it expects, even though genuinely typing those same lines one
  at a time at a real interactive prompt does *not* trigger this folding
  for a value like `"Best School"` (confirmed with CPython's actual
  interactive loop, fed the lines one at a time) — each REPL line
  compiles separately, so there's no shared constants table across them.
  Worth remembering as the practical difference between "it behaves this
  way in a script" and "it behaves this way typed live."
- **`24`–`26-answer.txt` (`True`, `True`, `True`)** — `a = (1)` isn't a
  tuple at all (no comma, so it's just the int `1`), and small ints are
  cached, hence `True`. `a = (1, 2)` is a real tuple, and gets the
  constant-folding behavior described above, also `True`. `a = ()` is a
  tuple too, and CPython additionally caches the empty tuple as a
  process-wide singleton regardless of how it's compiled — a third,
  independent reason for `True`. List literals (`14`, `17`, `18`, and
  especially `11`) never get this treatment under any compilation model,
  since Python can't safely fold or cache a *mutable* literal — task 11
  stays `False` for that reason.

Every identity/caching answer here was checked against real interpreter
execution rather than reasoned out from memory, including re-verifying
against the actual grading feedback for this task.

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
