import custom_module
from importlib.resources import Package

'''
-> A module in Python is simply a file containing Python code—functions, classes, and variables—that you can bring into another script.
-> If you put every piece of code for a large application into a single file, it would become thousands of lines long and impossible to maintain. Modules allow you to break your code down into organized, logical, and reusable pieces.
-> Think of your main script like a workshop. If you kept every tool in the world on your workbench, it would be a chaotic mess. Modules are like specialized toolboxes stored in the garage. When you need to do electrical work, you just import the electrical toolbox.
-> There are three type of modules:
    1. Custom Module
    2. InBuilt Module
    3. Third Party Module (install using tools like pip)
'''

message = custom_module.shout("hello")
print(message)

'''
Syntax,How it works,When to use it
import math,"Imports the entire module. You must type the module name first (e.g., math.sqrt(9)).",Default choice. It keeps it obvious exactly where a function came from.
from math import sqrt,"Plucks out exactly what you need. You can use it directly (e.g., sqrt(9)).",When you are calling a specific function dozens of times and want to save typing.
import pandas as pd,Imports the whole module but gives it a nickname (an alias).,"When the module name is long, or there is an industry-standard alias (like pd for Pandas)."
'''

'''
Concept of __name__ variable
-> That snippet—if __name__ == '__main__':—is one of the most common lines in Python, and it acts as a gatekeeper.
-> It solves a very specific problem: preventing code from running unintentionally when you import a module.
-> To understand how it works, you need to know how Python handles the special built-in variable called __name__.
-> Whenever Python runs a file, it automatically creates a few special hidden variables behind the scenes. One of them is __name__. Python uses this variable to keep track of how the file is being used:
    Scenario A (Running directly): If you run a file directly from your terminal (e.g., python calculator.py), Python says, "This is the main event!" and assigns the string "__main__" to the __name__ variable.
    
    Scenario B (Importing): If you import that same file into another script (e.g., import calculator), Python says, "This is just a helper module," and assigns the file's actual name ("calculator") to the __name__ variable.
'''


'''
Package
-> 1. The Module (The File)
A module is simply a single Python file ending in .py. It contains a collection of related functions, classes, or variables.
Example: A file named shopping_cart.py is a module.
Usage: You import it by referencing its file name: import shopping_cart.

-> 2. The Package (The Folder)
When your project gets bigger, having 50 separate modules in one directory becomes a mess. A package allows you to group related modules together inside a directory (folder).
However, Python doesn't automatically treat every folder as a package. To tell Python, "Hey, this folder contains a library of code," you must place a special file inside it called __init__.py.
(Note: While Python 3.3+ technically allows "namespace packages" without this file, using __init__.py is still the standard, professional best practice.)

-> What does __init__.py actually do?
The __init__.py file is usually completely empty. Its mere existence is enough to tell Python that the folder is a package.

However, because Python runs this file the moment the package is imported, advanced developers use it to run setup code or bundle imports together. For example, if you put from .shopping_cart import add_item inside the __init__.py file, users can skip typing the module name and just run from ecommerce import add_item.
'''