'''
1. You have a file auth.py that imports a function from database.py. But database.py also imports a function from auth.py. What happens when you run the code, and how do you fix it?
-> This creates a circular import. Python will throw an ImportError (or AttributeError) because the modules get stuck in an infinite loop trying to load each other before either one has finished initializing.
How to fix it:
    1. Best solution: Redesign your code. Extract the shared logic into a third, independent module (like config.py) that both auth.py and database.py can import without relying on each other.
    2. Quick hack (Local Import): Move the import statement inside the function that actually needs it, rather than putting it at the very top of the file. This delays the import until the function is actually called, breaking the initialization loop.
'''


'''
2. How Python Finds Modules (sys.path), When you write import requests or import my_module, exactly how does Python know where to find those files? What order does it search in?

-> When you run an import statement, Python searches through a list of directories stored in a system variable called sys.path. It searches in this strict order:
The current working directory (the folder your main script is sitting in).
Built-in modules (like math or sys that are baked into the Python interpreter).
Directories listed in the PYTHONPATH environment variable (if you configured it).
Standard Library directories (where modules like os or json live).
site-packages (the folder where third-party libraries installed via pip are stored).
Bonus point: This is why you should never name your own file math.py or random.py. Python will find your file first (Step 1) and ignore the actual standard library, crashing your code. This is called "shadowing."
'''


'''
3. Why is using from my_package import * considered a bad practice? If you are writing a package, how can you control what that wildcard (*) actually imports?
-> Wildcard imports are bad practice because they cause namespace pollution. They dump every single function, class, and variable from the module into your current file. This makes it impossible for someone reading the code to know which module a specific function came from, and it risks accidentally overwriting a variable you already created.

How to control it:
If you are the author of the module, you can define a special dunder variable called __all__ at the top of your file. It takes a list of strings representing the names you want to make public.

# database.py
__all__ = ['connect', 'disconnect']

def connect(): ...
def disconnect(): ...
def _internal_helper(): ... # This won't be imported by the * wildcard
'''