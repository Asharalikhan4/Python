from functools import wraps

def my_decorator(func):
    @wraps(func)    # After writing this line your function will preserve it's name
    def wrapper():
        print("Before Function Runs")
        func()
        print("After Function Runs")
    return wrapper


@my_decorator
def greet():
    print("Hello From Decorators")
    
greet()
print(greet.__name__)