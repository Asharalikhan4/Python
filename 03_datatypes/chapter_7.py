'''
() -> paranthesis
[] -> Square Brackets
{} -> Curly Braces

Tuple Symbol -> ()
- They are immutable in nature
'''

masala_spices = ("cardamom", "cloves", "cinnamon")
(spice1, spice2, spice3) = masala_spices

print(f"Main Masla Spices: {spice1}, {spice2}, {spice3}")

ginger_ratio, cardamom_ratio = 2, 1
print(f"Ratio of G : {ginger_ratio} and C : {cardamom_ratio}")

# Swapping of variable
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print(f"Ratio of G : {ginger_ratio} and C : {cardamom_ratio}")

# Membership testing
print(f"Is ginger in masala spices ? {"cinnamon" in masala_spices}")