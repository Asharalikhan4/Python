'''
1. How would you write a @retry(times=3) decorator that automatically re-runs a function if it throws an error? (Example of decorator with arguments)
'''

def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed. Retrying...")
            print("All attempts failed.")
        return wrapper
    return decorator

@retry(times = 3)
def unstable_network_call():
    raise ConnectionError("Server Timeout")

unstable_network_call()


'''
2. Write a @call_counter decorator that tracks and prints exactly how many times a specific function has been executed. (Example of State Tracking and nonlocal)
'''

def call_counter(func):
    count = 0   # State is stored in the closure
    def wrapper(*args, **kwargs):
        nonlocal count  # Tells python to modify the 'count' variable above
        count += 1
        print(f"{func.__name__} has been called {count} times.")
        return func(*args, **kwargs)
    return wrapper
        

@call_counter
def process_item():
    pass

process_item()
process_item()


'''
Read about closure and nonlocal
'''