'''
-> A function is a reusable block of code designed to perform one specific task. You can think of it as a mini-program inside your main script: you feed it data, it does some work, and it hands you back a result.
-> Parameter's are defined with the function and arguements are defined when the function is being called. We also have something called default parameter if not argument is provided then it will take that value as a default value.
'''

# 1. 'def' defines the function
# 2. 'calculate_total' is the function name
# 3. 'price' and 'tax_rate' are parameters (inputs)
def calculate_total(price, tax_rate=0.05):
    """Calculates the final price after tax."""  # 4. Docstring (explains what it does)
    
    # 5. Function body (the actual work)
    tax = price * tax_rate
    total = price + tax
    
    # 6. 'return' sends the result back to whoever called it
    return total

# Calling the function and storing the result in a variable
coffee_price = calculate_total(4.00)
laptop_price = calculate_total(1000.00, 0.08)

print(coffee_price)  # Outputs: 4.2
print(laptop_price)  # Outputs: 1080.0


'''
-> *args: Unlimited Positional Arguments
'''

def calculate_sum(*args):
    total = 0
    for number in args:
        total += number
    return total

print(calculate_sum(1, 2, 3))
print(calculate_sum())

'''
-> **kwargs: Unlimited Keyword arguments
'''

def build_profile(first, last, **kwargs):
    # 'first' and 'last' are standard parameters
    # 'kwargs' is a dictionary containing everything else
    profile = {
        'first_name': first,
        'last_name': last
    }
    
    # We can iterate through the dictionary and add the items
    for key, value in kwargs.items():
        profile[key] = value
        
    return profile

user = build_profile("Jane", "Doe", location="New York", role="Admin")

# Outputs: {'first_name': 'Jane', 'last_name': 'Doe', 'location': 'New York', 'role': 'Admin'}
print(user)


'''
Combining *args and **Kwargs
'''
def display_info(title, *args, **kwargs):
    print(f"Title: {title}")
    
    print("Positional arguments (*args):")
    for arg in args:
        print(f" - {arg}")
        
    print("Keyword arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f" - {key}: {value}")

# Calling the function with a mix of everything
display_info("Server Logs", "Error 404", "Rebooting", user="admin", ip="192.168.1.1")


'''
-> Enforcing the keyword only arguements
'''
# 'host' can be passed by position.
# 'secure' and 'timeout' MUST be passed by keyword.
def connect_to_server(host, *, secure=True, timeout=30):
    print(f"Connecting to {host} | Secure: {secure} | Timeout: {timeout}s")

# ✅ THIS WORKS: 
# We explicitly name the keyword arguments.
connect_to_server("localhost", secure=False, timeout=15)

# ✅ THIS ALSO WORKS: 
# We omit them, so they fall back to their defaults.
connect_to_server("localhost")

# ❌ THIS FAILS: 
# Python throws a TypeError: connect_to_server() takes 1 positional argument but 3 were given
connect_to_server("localhost", False, 15)