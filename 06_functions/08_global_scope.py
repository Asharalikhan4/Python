'''
What It Does
The global keyword allows you to modify variables at the module/global scope from within a function. Without it, assigning to a variable inside a function creates a new local variable instead of modifying the global one.
- global keyword can also create a new variable if it does not exist, while in the case of nonlocal it must exist.

global/non-local are the ways of to tell python that you really want to modify the variables.
'''

chai_type = "Plain"

def front_desk():
    def kitchen():
        # global chai_type
        chai_type = "Irani"
    kitchen()


front_desk()
print("Final global chai: ", chai_type)