'''
-> A lambda function in Python is a small, anonymous function that you write on a single line.
-> While a standard function is created using the def keyword and given a specific name, a lambda function is created using the lambda keyword and doesn't need a name at all. They are designed to be "throwaway" functions—used once for a quick calculation and then forgotten.
-> Syntax:
    lambda arguments: expression
-> Take any number of arguements, performs exactly one mathematical or logical expression, and automatically returns the result. You cannot use a return keyword, and you cannot write multiple lines of code.
-> Feature,Standard def,lambda
Name,Required,Anonymous (no name)
Length,Unlimited lines,Strictly one expression
Return,Requires explicit return keyword,Implicitly returns the expression's result
Complexity,"Can use loops, try/except, variable assignments",Restricted to a single evaluation
'''

# Standard function
from ntpath import defpath
def add_ten(num):
    return num + 10

# Lambda equivalent
lambda num: num + 10


# Real world example of lambda function
'''
1. Imagine you have a list of tuples representing a shopping cart, and you want to sort them by price (the second item in the tuple). A lambda is perfect here.
'''
cart = [("Apples", 2.50), ("Milk", 3.10), ("Bread", 1.80)]
sorted_cart = sorted(cart, key=lambda item: item[1])
print(sorted_cart)


'''
2. The filter() function requires a function that returns True or False. If you want to extract only the even numbers from a list, a lambda makes it a one-liner.
'''
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda number: number % 2 == 0, numbers))
print(evens)


'''
-> Very Common Mistake
Many of you try to store a lambda function in a variable to call it later which is wrong, it defeat it's purpose as an anonymous function, if it needs a name, use def. 
'''