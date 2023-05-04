# Loops #

- [Introduction](#introduction-)
- [While loops](#while-loops-)
- [For loops](#for-loops-)
- [Range](#range-)

---

## Introduction ##
Loops are a fundamental concept in programming, and they allow us to repeat a block of code multiple
times. In Python, there are two types of loops: `for` loops and `while` loops. They are a powerful
tool for automating repetitive tasks and processing data.

---

## While loops ##
A `while` loop is used when you want to repeat a code block until a certain condition is met.
The syntax for a while loop is as follows:
```python
while condition:
    # Code block to be repeated
```
Here, `condition` is a boolean expression that is checked at the start of each iteration. If it is
`True`, the code block indented under the while statement is executed. This continues until the
condition becomes `False`.

For example, let's say we want to print the numbers from `1` to `5` using a `while` loop.
We can do this as follows:
```python
i = 1
while i <= 5:
    print(i)
    i += 1
```
Output is following:
```
1
2
3
4
5
```

Here, the condition is `i <= 5`, which is initially `True` because `i` is `1`. The code block is
executed, printing the value of `i`, and then `i` is incremented by `1`. This continues until `i`
becomes `6`, at which point the condition becomes `False` and the loop ends.

---

## For loops ##

A for loop is used when you want to iterate over a sequence of elements. The syntax for a `for` loop
is as follows:
```python
for variable in sequence:
    # Code block to be repeated
```
Here, `variable` is a variable that takes on each value in the `sequence`, one at a time. The code
block indented under the `for` statement is executed once for each value of `variable`.

For example, let's say we want to print the numbers from 1 to 5 using `for` loop.
We can use it like this:
```python
for i in range(1, 6):
    print(i)
```
Output:
```
1
2
3
4
5
```
Here, `range(1, 6)` generates a sequence of integers from `1` to `5` (inclusive), which is then
iterated over by the for loop. `range` is a useful type when you want to generate a sequence of
numbers without having to manually create a list of numbers.

---

## Range ##
`range` is a built-in Python type that returns a sequence of numbers. It's often used in conjunction
with loops, especially `for` loops, to iterate over a sequence of numbers.

The syntax for range is as follows:
```python
range(start, stop, step)
```
Here, `start` is the starting number of the sequence (inclusive, default is 0), `stop` is the
stopping number of the sequence (exclusive), and `step` is the step size between numbers
(default is 1).

For example, `range(1, 6)` will return a sequence of integers from `1` to `5` (inclusive), while
`range(0, 10, 2)` will return a sequence of even numbers from `0` to `8` (inclusive).

In the context of a `for` loop, `range` is often used to iterate over a sequence of numbers.
You may see the example above.
