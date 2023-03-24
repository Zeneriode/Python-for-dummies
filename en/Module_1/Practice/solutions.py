"""
Solutions of the practical tasks for Module 1

Author:
    Zener

Version:
    1.0.0

License:
    MIT
"""

"""
Task 1:
Store any 3 numbers
"""
a, b, c = 1, 2, 3  # you can change values and names of variables if you want

"""
Task 2:
Split words in any string by spaces (From "Hello there" create ["Hello", "there"])
"""
words = input().split()  # by default, the string will be split by spaces
print(words)

"""
Task 3:
Count number of times `c` letter occurs in string
"""
string = input()
number_c_occurs = string.count('c')
print(number_c_occurs)

"""
Task 4:
Find position of `y` sign in this string
"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxyxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
"""
string = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxyxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
         "xxxxxxxxxxx"
index = string.find('y')
print(index + 1)  # because of indexing in the string starts from 0, the position must be increased by 1

"""
Task 5:
Take 3 numbers: A, B and C. Print sum of B and A in power of C.
"""
a = float(input())
b = float(input())
c = float(input())

print(b + a ** c)
