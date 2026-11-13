# Block 2: Control Flow (Notes)

Topics: if / elif / else, for loops and range(), while loops with break and continue, nested loops and patterns.

---

## 6. if / elif / else

**What it is:** Lets the program choose what to do. Python checks conditions from top to bottom, and **runs only the first block whose condition is True**. The rest are skipped.

```python
marks = 72
if marks >= 90:
    print("A")
elif marks >= 60:
    print("B")
else:
    print("C")
```

**Rules**
- A colon `:` ends every `if`, `elif`, `else` line.
- The code inside must be **indented** (4 spaces). Indentation is how Python knows what belongs to the block.
- Use `==` to compare, not `=`.
- `elif` and `else` are optional; `else` has no condition.

**Order matters:** put the most specific condition first.
```python
n = 15
if n % 3 == 0 and n % 5 == 0:   # most specific first
    print("both")
elif n % 3 == 0:
    print("three")
```
If you check `n % 3 == 0` first, 15 would stop there and the "both" case would never run.

**Truthy and falsy:** `0`, `""`, `[]` and `None` count as False; other values count as True.
```python
name = ""
if not name:
    print("Name is empty")
```

**Common mistakes**
- Missing colon or wrong indentation (IndentationError)
- Using `=` instead of `==`
- Putting a general condition before a specific one
- Using separate `if`s when you meant `elif` (separate `if`s all get checked)

---

## 7. for loops and range()

**What it is:** Repeats code for each item in a sequence, or a fixed number of times.

```python
for fruit in ["apple", "mango"]:
    print(fruit)

for ch in "hi":
    print(ch)
```

**range(start, stop, step)**: stop is excluded, start defaults to 0, step defaults to 1.
```python
range(5)          # 0 1 2 3 4
range(2, 6)       # 2 3 4 5
range(2, 10, 3)   # 2 5 8
range(5, 0, -2)   # 5 3 1  (counting down)
print(list(range(5, 0, -2)))   # [5, 3, 1]  (list() shows the values)
```

**When to use `for`:** you know how many times, or you're going through a collection.

**Useful patterns**
```python
total = 0
for n in range(1, 6):
    total += n          # running total
print(total)            # 15

for i, ch in enumerate("abc"):
    print(i, ch)        # 0 a / 1 b / 2 c
```

**Common mistakes**
- Forgetting that `stop` is excluded (`range(1, 5)` stops at 4)
- Changing the loop variable inside the loop and expecting it to affect the loop
- Wrong indentation, so code runs inside or outside the loop by accident

---

## 8. while loops, break, continue

**What it is:** Repeats **as long as a condition is True**. Use it when you don't know in advance how many rounds you need.

```python
count = 3
while count > 0:
    print(count)
    count -= 1      # without this, the loop never ends
```

**break** stops the whole loop immediately.
**continue** skips the rest of the current round and jumps to the next round.

```python
for i in range(1, 6):
    if i == 3:
        continue    # skip 3
    if i == 5:
        break       # stop at 5
    print(i)        # 1 2 4
```

**Infinite loop with a safe exit**
```python
while True:
    text = input("Type 'q' to quit: ")
    if text == "q":
        break
```

**Counting attempts:** decide where the counter goes so that every attempt is counted, including the last one.
```python
attempts = 0
while True:
    attempts += 1          # count at the top: every round counts
    word = input("Say hi: ")
    if word == "hi":
        break
print("Attempts:", attempts)
```

**Common mistakes**
- Forgetting to change the condition variable (infinite loop; stop it with Ctrl + C)
- Putting `count += 1` in the wrong place, so one attempt is missed
- Confusing `break` (leave the loop) with `continue` (next round)

---

## 9. Nested loops and patterns

**What it is:** A loop inside a loop. For each round of the outer loop, the inner loop runs completely.

```python
for i in range(1, 4):        # rows
    for j in range(i):       # columns in this row
        print("*", end="")
    print()                  # new line after each row
```
Output:
```
*
**
***
```

**Key ideas**
- `end=""` keeps the next print on the same line.
- An empty `print()` moves to the next line.
- The outer loop controls rows; the inner loop controls what is printed in each row.

**Tracing method (use this whenever you're unsure)**
Write a table and update it one step at a time.

| step | i | j | printed |
|------|---|---|---------|
| 1 | 1 | 0 | `*` |
| 2 | 2 | 0 | `*` |
| 3 | 2 | 1 | `*` then newline |

**Common mistakes**
- Mixing up which variable is for rows and which is for columns
- Forgetting the empty `print()` between rows
- Putting a `print` at the wrong indentation level

---

## Digits trick (while loop with % and //)

```python
n = 123
while n > 0:
    last = n % 10     # last digit: 3, then 2, then 1
    n //= 10          # remove the last digit: 12, then 1, then 0
```

---

## Mistakes from my own work (revise these)

1. **Indentation changes meaning.** A `print` outside the loop runs once, after it ends.
2. **Trace the code on paper** (a table of variable values) before running it. Order matters: `n += 1` before `print(n)` means 0 never prints.
3. **Counters:** decide where `+= 1` goes so that every attempt is counted.
4. **Read the whole task.** FizzBuzz was for 1 to 30 and needed a loop, and every other number needed an `else` branch.
5. **Use f-strings** for neat output: `f"{num} x {i} = {num * i}"`.
6. **Think about edge cases:** zero, negative numbers, empty input.
7. Python prints a list as `[5, 3, 1]`, so use the exact output format.

---

## Interview questions (short answers)

1. **Difference between `break` and `continue`?** `break` exits the loop; `continue` skips to the next iteration.
2. **When use `for` vs `while`?** `for` when you know the count or have a collection; `while` when you repeat until a condition changes.
3. **What does `range(1, 10, 3)` produce?** 1, 4, 7.
4. **If several conditions in an `if/elif` chain are true, how many blocks run?** Only the first one.
5. **What is an infinite loop, and how do you avoid it?** A loop whose condition never becomes False; make sure something inside changes the condition, or use `break`.
6. **What does `end=""` do in `print`?** Stops the newline, so the next print continues on the same line.

---

## 2-minute summary

- `if/elif/else` runs only the first true block; order matters; indentation is required.
- `for` loops go through a sequence or `range(start, stop, step)`; stop is excluded.
- `while` repeats while a condition is True; change something inside to avoid an infinite loop.
- `break` leaves the loop; `continue` jumps to the next round.
- Nested loops: the inner loop completes for each round of the outer loop.
- Trace code on paper with a variable table to avoid prediction mistakes.
