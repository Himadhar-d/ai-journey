# Block 1: Python Basics (Notes)

Topics: running Python, variables and types, type conversion and input, operators, strings.

---

## 1. Running Python, print, comments

**What it is:** A Python program is a list of instructions that run from top to bottom. `print()` shows output on the screen.

```python
print("Hello")          # shows Hello
print("Age:", 25)       # separate items with commas
# This is a comment: Python ignores it
```

**Run a file:** `python hello.py` in the terminal. **Save the file first** (Ctrl + S), or the old version runs.

**Common mistakes**
- Forgetting to save the file before running it
- Missing quotes or brackets in `print("...")`
- Wrong capitalisation: `Print` is an error, `print` is correct

---

## 2. Variables and data types

**Variable:** a label that points to a value. `price = 120` means the name `price` points to 120.

| Type | Example | Meaning |
|------|---------|---------|
| `str` | `"Chennai"` | text |
| `int` | `120` | whole number |
| `float` | `99.5` | decimal number |
| `bool` | `True` / `False` | yes or no |

```python
city = "Chennai"
price = 120
print(type(price))      # <class 'int'>
```

**Rules for names:** letters, digits and `_`; cannot start with a digit; case-sensitive (`Name` and `name` are different); use meaningful names like `total_price`, not `x`.

**`=` vs `==`**
```python
x = 5       # assignment: store 5 in x
x == 5      # comparison: is x equal to 5? gives True or False
```

---

## 3. Type conversion and input()

`input()` **always returns text (`str`)**, even if the user types a number.

```python
age = input("Age: ")          # "25" is a string
age = int(input("Age: "))     # now 25 is an int
price = float(input("Price: "))   # use float for decimals like 99.50
```

| Function | Converts to |
|----------|-------------|
| `int()`  | whole number |
| `float()`| decimal |
| `str()`  | text |

```python
x = input("Enter number: ")   # user types 5
print(x + 1)                  # TypeError: you can't add str and int
print(int(x) + 1)             # 6
```

**Common mistakes**
- Forgetting `int()` or `float()` after `input()`
- Using `int()` for prices (fails on `99.50`; use `float()`)
- `"5" + "5"` gives `"55"` (text joining), while `5 + 5` gives `10`

---

## 4. Operators

**Arithmetic**

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `+ - *` | add, subtract, multiply | `4 * 3` | 12 |
| `/` | division (always float) | `7 / 2` | 3.5 |
| `//` | whole-number division | `7 // 2` | 3 |
| `%` | remainder | `7 % 2` | 1 |
| `**` | power | `2 ** 4` | 16 |

**Comparison:** `==  !=  >  <  >=  <=` give `True` or `False`.

**Logical:** `and`, `or`, `not`

```python
print(10 > 5 and not (3 == 4))
# 10 > 5       -> True
# 3 == 4       -> False, and not False -> True
# True and True -> True
```

**Tip:** when a logic line confuses you, solve the smallest pieces first, then combine them.

**Rounding:** `%` is NOT rounding. Use `round(value, 2)`.
```python
total = 100 * 1.18
print(round(total, 2))   # 118.0
```

**Common mistakes**
- Using `%` to round (it gives a remainder)
- Mixing up `/` and `//`
- Forgetting that `not` flips the whole bracket

---

## 5. Strings

A string is text in quotes. Each character has a position (index) starting at 0. Negative indexes count from the end.

```python
s = "python"
print(s[0])       # p
print(s[-1])      # n
print(s[1:4])     # yth  (start included, stop excluded)
print(s[::2])     # pto  (step of 2; a negative step walks backwards)
print(len(s))     # 6
```

**Slice pattern:** `s[start:stop:step]`. Any part can be left empty.

**Common methods**
```python
s.upper()  s.lower()  s.title()
s.strip()                  # remove spaces at both ends
s.replace("p", "P")
s.split(" ")               # text to list
s.startswith("py")  s.endswith("on")
s.find("th")               # position, or -1 if missing
```

**f-strings** (the easiest way to build text)
```python
name = "Hima"
year = 2030
print(f"Hello {name}, welcome to {year}")
```

**Strings are immutable:** you can't change one character in place. `s[0] = "P"` is an error. Make a new string instead.

**Common mistakes**
- Index out of range (`s[10]` when the length is 6)
- Forgetting that stop is excluded in slices
- Expecting methods to change the original (they return a new string)

---

## Practice mistakes from my own work (revise these)

1. `not` and brackets: break the line into pieces and evaluate each.
2. `%` is the remainder, not rounding. Use `round(value, 2)`.
3. Re-read the task before submitting. I missed the "reversed" part once.
4. Use every value I collect (I asked for a name and forgot to print it).
5. Use `float()` for prices, and name variables honestly (`total`, not `gst`).
6. Test every program with at least 2 different inputs.

---

## Interview questions (short answers)

1. **What is a variable?** A name that refers to a value stored in memory.
2. **What does `input()` return?** Always a string.
3. **Difference between `/` and `//`?** `/` gives a float result; `//` gives the whole-number part.
4. **What is the difference between `=` and `==`?** `=` assigns a value; `==` compares two values.
5. **Are strings mutable?** No, they're immutable. Operations create new strings.
6. **What does `"5" + "5"` give?** `"55"`, because `+` joins strings.

---

## 2-minute summary

- A program runs top to bottom; save before you run.
- Types: `str`, `int`, `float`, `bool`; check with `type()`.
- `input()` returns text; convert with `int()` or `float()`.
- `//` whole division, `%` remainder, `**` power; `round()` rounds.
- `and`, `or`, `not` combine True/False values.
- Strings: index from 0, slice `[start:stop:step]`, use f-strings, they are immutable.
