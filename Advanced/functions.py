"""Functions are very useful, because you can split your work to some parts and complete them step by step"""


# To define a new function you have to write like this
def simple():
    pass


# To activate the function just write its name
simple()

# ----------------------------------------------------------------------------------------------------------------------


# functions can connect with global variables
a = 0


def change_a():
    global a  # explain that you use global 'a', not function's private variable
    a = 10


change_a()  # Since now the variable 'a' equals to 10


# ----------------------------------------------------------------------------------------------------------------------


# some functions can take some arguments
def new_value(value: int) -> None:
    global a
    a = value


# You can create some arguments and some of them can be initialized by default
def print_value(value1: int, value2: int, choose: int = 0):
    if choose == 0:
        print(value1)
    else:
        print(value2)


print_value(1, 2)  # 'choose' variable is 0 by default

# You can initialize the arguments by printing their names in the brackets
print_value(value2=5, value1=1, choose=1)


# ----------------------------------------------------------------------------------------------------------------------


# Some functions can take a list of arguments by default
def print_all(*values: object) -> None:
    """Prints each value in each line"""
    for value in values:
        print(value)


# prints all numbers in 4 lines using list of arguments
print_all(1, 2, 3, 4)


def print_some(**values) -> None:
    if "a" in values:
        print(values["a"])


# prints 1 value with key '1' if it's in the dictionary
print_some(a="Hey", b="World")
