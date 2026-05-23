'''
- A decorator is a powerful design pattern that allows you to modify or extend the behavior of a function, method, or class without permanently changing its source code.
- We can use multiple decorator at once, this is called decorator stacking or chaining, the execute from the bottom-up, closet to the function first.
- Decorator format explantion
1. The Inner wrapper Function
Purpose: To defer execution.
Without an inner function, the code inside the decorator runs the moment the function is defined (at import time). We use the wrapper to ensure the logic runs every time the function is called.

2. Using *args and **kwargs
Purpose: To ensure generic compatibility.
A professional decorator should be able to wrap any function, whether it takes zero arguments or fifty. Using *args and **kwargs ensures that the decorator doesn't "break" the signature of the function it is decorating.

3. The @functools.wraps(func) Decorator
Purpose: To preserve Identity and Metadata.
This is the most critical "standard" part. In Python, every function has metadata like __name__, __doc__ (docstrings), and __module__.
-- Without @wraps: If you decorate process_data, and then call process_data.__name__, it will return "wrapper". This breaks automated documentation (Sphinx), debuggers, and certain frameworks (like Flask) that route based on function names.
-- With @wraps: It copies the original function's identity onto the wrapper, so process_data still looks and acts like process_data.

- Standard template for decorators
import functools

def standard_decorator(func):
    """Standard template for a robust decorator."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 1. Logic to run BEFORE the function call
        print(f"Calling {func.__name__}")
        
        # 2. Execute the actual function
        result = func(*args, **kwargs)
        
        # 3. Logic to run AFTER the function call
        print(f"{func.__name__} finished")
        
        # 4. Return the result so the caller receives it
        return result
    return wrapper
'''

# Real world implementation ( The Timer Decorator ) - Use case is performance monitoring to identify slow functions.

import time
import functools

def timer_decorator(func):
    '''Logs the execution time of a function.'''
    @functools.wraps(func)  # Preserve the original function's metadata
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)  # Execute the original function
        end_time = time.perf_counter()
        print(f"Executed {func.__name__} in {end_time - start_time:.4f}s")
        return result
    return wrapper

def printName(func):
    '''Print Name'''
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Ashar Ali Khan")
        return func(*args, **kwargs)
    return wrapper

@timer_decorator
@printName
def process_data():
    time.sleep(1.5) # Simulate heavy work
    return "Data Processed"
    
result = process_data()
print("Result:", result)