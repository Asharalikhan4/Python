# chai = "Ginger Chai"

# def prepare_chai(order):
#     print("Preparing", order)


# prepare_chai(chai)
# print(chai)



chai = [1, 2, 3]
def edit_chai(cup):
    cup[1] = 42

edit_chai(chai)
print(chai)

'''
function take paramters
function call take arguements


- There are two typs of arguements that i can pass here first one is
1. args -> also know for position parameters.
2. *kwargs -> 
'''

def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "Yes", "Low")   # Positional
make_chai(tea = "Green", sugar = "Medium", milk = "No") #Keyword


def special_chai(*ingrediants, **extras):
    print("Ingrediants", ingrediants)
    print("Extras", extras)

special_chai("Cinnamon", "Cardmom", sweetner="Honey", foam="Yes")

# Function below will cause the issue for better check for other function blow down
# def chai_order(order=[]):
#     order.append("Masala")
#     print(order)

def chai_order(order=None):
    if order is None:
        order = []
    print(order)

chai_order()
chai_order()