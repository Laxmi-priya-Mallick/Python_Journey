# FUNCTIONS & VARIABLES

"""FUNCTION: similar to a action or verb that basically let's you do something in the program.
ARGUMENTS: an input to a function that influences function's behaviour.
SIDE EFFECT: output received from a set of code (can visual, audio, etc)."""
#---------------------------------------------------------------------------------------------------------#

# 1.using print and input func:
name = input("Enter your name:")
print("Hello, ")
print(name)

# 2.concatenation and f-strings
"""f-STRINGS: short for 'format strings', is a way to embed expressions or variables directly inside
string literals.
CONCATENATION: to join two or more strings using '+'."""

# 2.1.using + operator:
name = input("Enter your name:")
print("Hello, "+ name)

# 2.2.using f-string:
name = input("Enter your name:")
print(f"Hello, {name}")

# 3.string method: (to clean the input)
"""STRIP: removes extra, unwanted spaces from the ends of the input
TITLE: capitalizes the first letter of every word in input"""

name = input("What is your name?").strip().title()
print(f"Hello, {name}")

# 4.custom functions: (defining and using a custom hello function)
def hello(to):
    print("Hello, ", to)

name = input("What is your name?")
hello(name)

# 5. parameterized functions:
def hello1(to = "world"):
    print(f"Hello, {to}")

hello1()
name = input("What is your name?")
hello1(name)

