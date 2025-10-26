'''
The nonlocal Keyword in Python
What It Does
The nonlocal keyword allows you to modify variables from an enclosing (outer) function's scope within a nested (inner) function. Without it, assigning to a variable in a nested function creates a new local variable instead of modifying the outer one.
Why We Use It
When you have nested functions and need the inner function to change a variable that belongs to the outer function's scope (not global, not local to the inner function).

in the non-local it is just above
'''

def update_order():
    chai_type = "Elaichi"
    def kitchen():
        nonlocal chai_type  # This tells python to use outer chai_type and don't create new
        chai_type = "Kesar"
    kitchen()
    print("After kitchen update", chai_type)

update_order()