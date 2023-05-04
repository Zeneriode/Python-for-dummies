# Conditional statements

- [Basic definition](#basic-definition-)
- [Advanced: elif and else](#advanced-elif-and-else-)
- [How to check condition better](#how-to-check-condition-better-)
- [Match statement](#match-statement-)

---

## Basic definition ##
In Python, if is a conditional statement used to specify a block of code to be executed if a particular condition is true.

The basic syntax of an if statement in Python is as follows:
```python
if {condition}:
    {action}
```
The `condition` in the above syntax is an expression that is evaluated to either `True` or `False`. If the `condition` is `True`, then the
code inside (`action`) the `if` block will be executed. If the `condition` is `False`, then the `action` will be skipped and the program
will continue executing the next line of code after the `if` block.

---

## Advanced: elif and else ##
Optionally, you can also include `elif` and `else` clauses after the `if` statement to handle additional cases. Here's an example that
demonstrates the use of `if`, `elif`, and `else` statements:
```python
x = 10

if x < 0:
    print("x is negative")
elif x == 0:
    print("x is zero")
else:
    print("x is positive")
```
In the above example, the code checks the value of the variable `x`. If `x` is less than 0, it prints "x is negative". If `x` is equal to 0,
it prints "x is zero". If `x` is greater than 0, it prints "x is positive".

Note that you cannot create `elif` or `else` statements with no `if` before them.

---

## How to check condition better ##
There are lots of cases when you have to initialize variable or print something using `if`. For that you might use conditional expression.

In Python, a conditional expression, also known as a ternary operator, is a way to write a short and concise if statement in a single line
of code.

The syntax of a conditional expression is as follows:
```python
{value_if_true} if {condition} else {value_if_false}
```
Here, `condition` is the expression to be evaluated, and if it's `True`, the `value_if_true` expression will be executed, otherwise, the
`value_if_false` expression will be executed.

Using a conditional expression can make your code more concise and easier to read, especially for simple conditions. However, it's important
to use them judiciously and not to make your code too complex or difficult to understand.

---

## Match statement ##
Also, Python contains `match` statement.
`match` is a new pattern matching feature that was introduced in Python 3.10. It's a new way to write conditional statements that allows you
to match patterns in data structures such as tuples, lists, and dictionaries.

Here's an example of how you can use the match statement to match patterns in a list:
```python
color = input()
match color:
    case "red":
        print("#FF0000")
    case "green":
        print("#00FF00")
    case "blue":
        print("#0000FF")
    case _:
        print("Unknown color")
```
In this example, the `match` statement checks if the `color` matches one of the predefined cases using the case keyword. If there is a
match, the corresponding value is printed. The `_` pattern acts as a default case, similar to an `else` block in an `if` statement.