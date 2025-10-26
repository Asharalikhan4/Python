'''
Sets -> This is overlap of two data ( data of a and b). Data will be Unique
Union -> This is overlap of two data, In this all the data will be stored
'''

essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

all_spices = essential_spices | optional_spices     # Union
print(f"All Spices : {all_spices}")

common_spices = essential_spices& optional_spices
print(f"Common Spices : {common_spices}")

only_in_essential = essential_spices - optional_spices
print(f"Only in essential spices : {only_in_essential}")

print(f"Is 'cloves' in essential spices? {'cloves' in essential_spices}")
