'''
-> A context manager is a programming construct that allows you to properly manage resources. It guarantees that if you "borrow" a resource (like opening a file, connecting to a database, or acquiring a thread lock), that resource will be cleanly handed back or closed when you are done with it—even if your code crashes halfway through.
-> You will almost always recognize a context manager by the use of the with keyword.


The Problem It Solves
-> When you open a file in Python, the operating system locks that file. If you forget to close it, or if your program crashes before it reaches the close() command, that file remains locked. This is called a "resource leak."
The Old, Messy Way:
    To safely handle this in the past, developers had to write verbose try...finally blocks to guarantee the file would close:
'''

file = open("my_data.text", "w")
try:
    file.write("Hello, World!")
    # If an error hapens here, the code jumps to "finally"
finally:
    file.close()    # This is guaranteed to run

'''
The Context Manager Way (The with Statement)
A context manager abstracts all that messy try...finally logic away into a single, clean line of code.
'''

with open("my_data.txt", "w") as file:
    file.write("Hello, World!")

'''
- Once you un-indent, the file is automatically closed!
- In this example, open() acts as the context manager. When the code enters the indented block, it prepares the file. The moment the block ends—whether it finishes successfully or throws a massive error—the context manager automatically closes the file.

How Does It Work Under the Hood?
For an object to be a context manager, it must have two specific "magic methods" built into its class:
    __enter__(): This runs the moment the with statement is called. It sets up the resource and optionally returns it (the as file part).
    __exit__(): This runs the exact moment the indented block finishes. It cleans up the resource, closes connections, and handles any exceptions that were thrown inside the block.

Use of Context Manager:
    1. Databases.
    2. Threading.
    3. Network Connections.
'''