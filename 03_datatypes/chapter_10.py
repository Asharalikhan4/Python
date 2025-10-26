'''
Dictionary
'''

chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"Chair Order : {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"Recipe base: {chai_recipe['base']}")
print(f"Recipe base: {chai_recipe}")

del chai_recipe["liquid"]
print(f"Recipe base: {chai_recipe}")