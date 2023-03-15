## Variables

- [What are variables?](#what-are-variables)
- [Basic usage of variables](#basic-usage-of-variables)
- [How not to name variables](#how-not-to-name-variables)
- [How to name variables better](#how-to-name-variables-better)
- [What can we store in a variable?](#what-can-we-store-in-a-variable)

---

### What are variables?

When you run any program, it asks the computer to store some information in memory. However, if the program stores all
necessary data in files, for example, it wastes a lot of time, and you might notice that your computer works slowly.
This is why every program uses temporary variables - the fastest way to store information in high-level programming
languages. But how do they work?

---

### Basic usage of variables

To create a variable, we just have to type a name of the variable, then put an `=` sign and type what to store in this
variable:

```python
variable = "Hello, I am a variable"
```
---
### How not to name variables
Of course, there are some constraints in naming variables. You cannot name variable:
1) If name is the same as a keyword in Python. For example, name `if` is not allowed.
2) If name is the same as a built-in function. For example, name `print` is not allowed.
3) If name starting with one of these letter: `@#$%&*+-/^|~?!._`.
4) If name starts with a number. For example, name `9nine` is not allowed.
---
### How to name variables better
I suggest you use descriptive and meaningful variable names that reflect their purpose.
For example, if you want to store the largest value of FPS in a game, it's better to name this variable as `max_fps`.

Also, there are some cases where you can use variables in the program. If you have some value, which must be the same
for the whole execution of the program, you can note in the code that this value is constant by typing with capital
letters. Remember the previous example with fps? So maybe it would be better to name this variable as `MAX_FPS`.
---
### What can we store in a variable?
The answer is so simple: you can store the variables whatever you want? But what exactly?
For now, it's enough to remember basic types of Python, which you will meet in every code:
1) `int` - type of values describing integer numbers.
    ```python
    just_int = 10  # simple case
    str_to_int = int("100")  # conversion from any other type to int
    binary_to_decimal = int("1010", base=2)  # conversion from binary to decimal (advanced knowledge)
    ```
2) `float` - type of values describing not integer number (with floating point)
    ```python
    just_float_number = 10.2  # simple case
    str_to_float = float("100.52")  # conversion from any other type to int
    ```
3) `str` - type of values describing some string
    ```python
    just_str = "Just a string"  # simple case
    another_str = 'Still a string'  # You can both either " or ', but it's better to use "
    str_number = str(10)  # Numbers can be stored as strings
    ```
4) `bool` - type of values describing either `True` or `False`. It takes a bit more information about this type, now
try to remember simple cases only
    ```python
    just_bool = True  # simple case
    num_to_bool = bool(10)  # True, explanation a bit later
    ```