'''
Scopes and Name Resolution

Local - inside a function
Enclosing from outer function if nested
global - Top level script
Built in
'''

def serve_chai():
    chai_type = "Masala"    # local Scope
    print(f"Inside function {chai_type}")
    
chai_type = "Lemon"
serve_chai()
print(f"Outside Function: {chai_type}")


def chai_counter():
    chai_order = "lemon"    # Enclosing Scope
    def print_order():
        chai_order = "Ginger"
        print("Inner: ", chai_order)
    print_order()
    print("Outer: ", chai_order)
    
chai_order = "Tulsi"    # Global
chai_counter()
print("Global :", chai_order)