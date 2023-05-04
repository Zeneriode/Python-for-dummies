# Boolean algebra and comparisons of values #

- [What is boolean algebra?](#what-is-boolean-algebra-)
- [How to work with logical values?](#how-to-work-with-logical-values-)
- [How are other types converted to bool type?](#how-are-other-types-converted-to-bool-type-)
- [How to compare values?](#how-to-compare-values-)
- [Operator `is`](#operator-is-)
- [A trouble of floating numbers](#a-trouble-of-floating-numbers-)
---
## What is boolean algebra? ##
Computers can work only with ones and zeros. Thus, all information is stored as sequences of ones and zeros in some
cases. Because computers also cannot understand arithmetic actions, we must work only with boolean algebra.

Boolean algebra is a branch of algebra that deals with mathematical operations on binary (`True`/`False`) values.
Boolean algebra has its own set of logical operations, such as `and`, `or`, and `not`, which are used to manipulate and
evaluate boolean expressions. These logical operations can be applied to boolean values to create more complex
expressions, which can be used to test conditions in computer programs or digital circuits.

---
## How to work with logical values? ##
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
## How are other types converted to bool type? ##
This is important to understand because some code in the future will rely on that, not only on education.
There are some cases, when `bool()` function can return us `False` value:
1) If `int`/`float` value equals `0`.
2) If `str` value equals to `""` (empty string).
3) If there is a `None` value.
4) If there is an empty structure. For example, empty list(will be learned in
[Module 2](../Module_2/Lesson%206%20-%20lists.md))

All other combinations/values return `True` value.

---
## How to compare values? ##
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

## Operator `is` ##
There is also `is` operator in Python, which can compare values by reference.
It means we can check if any 2 variables reference to the same object.
There is example of `is` operator:
```python
a = 14.2
b = a
c = 14.2
print(a is b)  # True
print(a is c)  # False
```
This operator needs when we try to find the same object (see [Module 3](../Module_3)). 

However, there are some notes in standard types. Here's an example:
```python
a = 10
print(a is 10)  # True
a = 300
print(a is 300)  # False
```
This is because Python caches (pre-allocates) and reuses small integers in the range of `-5` to `256` for performance
optimization reasons. This means that if you create an integer within this range, any other reference to that same
value will point to the same object in memory.

However, for values outside this range, a new object is created every time you create a new integer. So when you write
`a = -6`, Python creates a new integer object for `-6`, and when you later check `a is -6`, it compares the memory
address of the `a` variable with the memory address of a newly created `-6` integer object, and they are not the same,
hence the result is `False`. So use `==` to compare numbers and strings.

---
## A trouble of floating numbers ##
Sometimes you can meet some troubles in comparing floating numbers. For example, consider we have to compare to numbers:
```python
print(1.15 * 100 == 115)  # It would print `False`
```
So it happens because of the way that floating-point numbers are represented in computers.

Floating-point numbers are represented using a finite number of bits, which means that not all real numbers can be
represented exactly. This can lead to rounding errors when performing arithmetic operations on floating-point numbers.

In the case of 1.15 * 100, the actual result is a number very close to 115, but not exactly 115. This is because 1.15
cannot be represented exactly in binary (the base used by computers), and so some rounding occurs during the
multiplication.
To see the full version of the number `1.15`, you can use that:
```python
print("{:.55f}".format(1.15))
# 1.1499999999999999111821580299874767661094665527343750000
```
As you can see, the result is very close to 115, but not exactly equal to it. This is why 1.15 * 100 == 115 evaluates
to False in Python.

To compare floating-point numbers, it's often better to check if they are "close enough" to each other, using a
tolerance value. For example, you could check if the absolute difference between the two numbers is less than a small
value, such as 0.0001:
```python
print(abs(1.15 * 100 - 115) < 0.0001)  # True
```
This expression evaluates to True, because the absolute difference between the result of the multiplication and 115 is
less than 0.0001.