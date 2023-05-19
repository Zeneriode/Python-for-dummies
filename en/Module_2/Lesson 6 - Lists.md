# Lists #

- [Definition](#definition-)
- [Indexing and slicing](#indexing-and-slicing-)
- [Modification](#modification-)
- [Methods](#methods-)

---

## Definition ##
In Python, a `list` is a built-in data structure that allows you to store and organize a collection of items. It is an
ordered and mutable collection, meaning you can change its elements and their positions within the list.

You can create a list by enclosing comma-separated values or items within square brackets (`[]`). The items can be of
any data type, and they don't have to be of the same type. For example:
```python
my_list = [1, 2, 3, "apple", "banana", True]
```
In this example, `my_list` contains integers, strings, and a boolean value.

---

## Indexing and slicing ##
You can access individual elements in a list using indexing. The index starts at 0 for the first element, and you can
use positive or negative indices to access elements from the beginning or end of the list, respectively. For example:
```python
my_list = [1, 2, 3, 4, 5]
print(my_list[0])   # Output: 1
print(my_list[3])   # Output: 4
print(my_list[-1])  # Output: 5 (last element)
```
Also, for choosing only a part of a list we may use slicing.
Slicing in Python is a way to extract a portion of a list (or other sequence types like strings or tuples) by specifying
a range of indices. It allows you to create a new list containing the selected elements from the original list.
Here are a few examples of slicing in Python:
```python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sliced_list = my_list[2:7]  # Elements from index 2 to 6 (7th element excluded)
print(sliced_list)
```
Output:
```
[3, 4, 5, 6, 7]
```
In this example, `sliced_list` contains elements from index `2` to `6` (inclusive), which are `[3, 4, 5, 6, 7]`.
Another example:
```python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sliced_list = my_list[1:9:2]  # Elements from index 1 to 8, skipping every second element
print(sliced_list)
```
Output:
```
[2, 4, 6, 8]
```
In this example, `sliced_list` contains elements from index `1` to `8` (inclusive), with a step of `2`. So, it skips
every second element and selects `[2, 4, 6, 8]`.

---

## Modification ##
Lists are mutable, which means you can change their elements. You can assign new values to specific indices to modify
the list. For example:
```python
my_list = [1, 2, 3, 4, 5]
my_list[2] = "apple"
print(my_list)  # Output: [1, 2, 'apple', 4, 5]
```

---

## Methods ##
There are lots of methods that can be used in list. I will show something only:
```python
a = []
a.append(value)  # Adds some value to the list
a.pop(index)  # Deletes value from the list by given index
a.remove(value)  # Deletes value from the list (only first one appeared)
```
All other methods are approximately understandable by their names.