# Boolean algebra and comparisons of values

- [What is boolean algebra?](#what-is-boolean-algebra)
- [How to work with logical values?](#how-to-work-with-logical-values)
- [How are other types converted to bool type?](#how-are-other-types-converted-to-bool-type)
- [How to compare values?](#how-to-compare-values)
---
### What is boolean algebra?
Computers can work only with ones and zeros. Thus, all information is stored as sequences of ones and zeros in some
cases. Because computers also cannot understand arithmetic actions, we must work only with boolean algebra.

Boolean algebra is a branch of algebra that deals with mathematical operations on binary (`True`/`False`) values.
Boolean algebra has its own set of logical operations, such as `and`, `or`, and `not`, which are used to manipulate and
evaluate boolean expressions. These logical operations can be applied to boolean values to create more complex
expressions, which can be used to test conditions in computer programs or digital circuits.
---
### How to work with logical values?
To start to do something, we firstly need to have some boolean values in the program, i.e. some variables `bool` type.
In example, let's find if we all variables contain `True` value:
```python
var1 = bool(input())  # If nothing will be printed, then variable will take 'False' value
var2 = bool(input())
var3 = bool(input())
print(var1 and var2 and var3)
```
By using `and` statements we can combine all values to get 1. I will consider you know how `and`, `or` and `not`
operations work from school/self-study.
---
### How are other types converted to bool type?
This is important to understand because some code in the future will rely on that, not only on education.
There are some cases, when `bool()` function can return us `False` value:
1) If `int`/`float` value equals `0`.
2) If `str` value equals to `""` (empty string).
3) If there is a `None` value.
4) If there is an empty structure. For example, empty list(will be learned in
[Module 2](../Module_2/Lesson%206%20-%20lists.md))

All other combinations/values return `True` value.

---
### How to compare values?
You can compare values using comparison operators. The result of a comparison is a boolean value (`True` or `False`).
Here are the available comparison operators:
- `==`: equal to
- `!=`: not equal to
- `<`: less than
- `>`: greater than
- `<=`: less than or equal to
- `>=`: greater than or equal to
In example:
```python
x = 10
y = 5

print(x == y)   # False
print(x != y)   # True
print(x < y)    # False
print(x > y)    # True
print(x <= y)   # False
print(x >= y)   # True
```
You can also chain multiple comparison operators together using the `and`/`or`/`not` keywords. For example:
```python
x = 10
y = 5
z = 8

print(x > y and x > z)   # True, because x is greater than both y and z
print(x > y or x < z)    # True, because x is greater than y or less than z (or both)
```
Note that the order of operations matters when chaining comparison operators together.
You can use parentheses to group operations together if needed.