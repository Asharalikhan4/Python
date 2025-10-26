'''
List Symbol -> []
- They are mutable in nature
'''

ingredients = ["water", "milk", "black tea"]

ingredients.append("sugar")
ingredients.remove("water")

print(f"Ingredients are : {ingredients}")

spice_options = ["ginger", "cardamom"]
chai_ingrediants = ["water", "milk"]

chai_ingrediants.extend(spice_options)
print(f"Chai : {chai_ingrediants}")

chai_ingrediants.insert(2, "black tea")     # Insert at defined position
print(f"Chai : {chai_ingrediants}")

last_added = chai_ingrediants.pop()     # Remove the last element and return to you
print(f"Chai : {chai_ingrediants}")
print(f"Last Added : {last_added}")

chai_ingrediants.reverse()
print(f"Reversed : {chai_ingrediants}")

sugar_levels = [1, 2, 3, 4, 5]
print(f"Maximum sugar level : {max(sugar_levels)}")
print(f"Maximum sugar level : {min(sugar_levels)}")


'''
Operator Overloading -> Whenver a operator is used to do more then one task that is called operator overloading
'''

base_liquid = ["water", "milk"]
extra_flavour = ["ginger"]

full_liquid_mix = base_liquid + extra_flavour
print(f"Liquid Mix : {full_liquid_mix}")

strong_brew = ["black tea"] * 3
print(f"Strong Brew : {strong_brew}")

raw_spice_data = bytearray(b"CINNAMOM")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Bytes : {raw_spice_data}")