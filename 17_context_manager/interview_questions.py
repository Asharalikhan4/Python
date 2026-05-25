'''
1. What is a context manager, and why do we use the with keyword?
-> Explain that it provides automatic resource management (setup and teardown). It guarantees that resources like files, network connections, or database locks are safely released, even if the code throws an exception.
'''


'''
2. If you didn't have the with statement, how would you safely open and close a file?
-> You would use a try...finally block. The interviewer wants to hear the word finally because that guarantees execution of the close() method.
'''


'''
3. How do you create a custom context manager using a class?
-> You must define a class that implements two specific magic methods: __enter__() (which runs at the start of the block) and __exit__() (which runs at the end).
'''


'''
4. What arguments does the __exit__ method take?
-> It takes three arguments related to exceptions: exc_type (the type of error), exc_value (the error message), and traceback (the stack trace). If no error occurred, all three are None.
'''


'''
5. if an error occurs inside a with block, how do you stop that error from crashing the rest of your program using the context manager?
-> Inside the __exit__() method, you handle the error and then explicitly return True. Returning True tells Python, "I have handled this exception, please suppress it and continue running the rest of the script." If you return False (or nothing), the error propagates and crashes the script.
'''


'''
6. Can you write a context manager without writing a full class?
-> Answer focus: Yes. You can use the @contextmanager decorator from Python's built-in contextlib module. You apply it to a regular function and use the yield keyword.
Code explanation: Everything before yield acts like __enter__, and everything after yield acts like __exit__.
'''


'''
7. Build a custom Context Manager
'''

# Class Based Approach
class CustomFileOpener:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"-> Setting up: Opening '{self.filename}'")
        self.file = open(self.filename, self.mode)
        # What we return here is bound to the variable after 'as'

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"-> Tearing down: Closing '{self.filename}'")
        if self.file:
            self.file.close()

        # If an error occurred inside the 'with' block, exc_type will not be None
        if exc_type is not None:
            print(f"-> An exception of type {exc_type} occurred: {exc_value}")
            # Return True to suppress the error, or False to let it crash the program.
            # We will return False here to mimic normal file handling.
            return False

with CustomFileOpener("test.txt", "w") as f:
    print("Writing to file...")
    f.write("Hello World!")

# Output:
# -> Setting up: Opening 'test.txt'
# Writing to file...
# -> Tearing down: Closing 'test.txt'



'''
from contextlib import contextmanager

@contextmanager
def custom_file_opener(filename, mode):
    print(f"-> Setting up: Opening '{filename}'")
    file = open(filename, mode)
    
    try:
        # Everything BEFORE yield acts like __enter__
        # The yielded value is assigned to the 'as' variable
        yield file 
        
    finally:
        # Everything AFTER yield acts like __exit__
        # The finally block guarantees the file closes even if an error occurs above
        print(f"-> Tearing down: Closing '{filename}'")
        file.close()


with custom_file_opener("test.txt", "w") as f:
    print("Writing to file...")
    f.write("Hello World again!")
'''



'''
class SuppressError:
    def __init__(self, error_to_suppress):
        self.error_to_suppress = error_to_suppress

    def __enter__(self):
        pass # No setup needed

    def __exit__(self, exc_type, exc_value, traceback):
        # If the error matches the one we want to suppress, return True
        if exc_type is not None and issubclass(exc_type, self.error_to_suppress):
            print(f"Caught a {exc_type.__name__}, but suppressed it!")
            return True # This tells Python "I handled it, do not crash"
        return False


with SuppressError(ZeroDivisionError):
    print("About to divide by zero...")
    x = 1 / 0
    print("This line will never run.")

print("The program continues safely!")

# Output:
# About to divide by zero...
# Caught a ZeroDivisionError, but suppressed it!
# The program continues safely!
'''