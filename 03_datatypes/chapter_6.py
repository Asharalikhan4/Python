# Strings are immutable in Python
# Last number is not inclusive


# there are two colons first number: second number: third number
# first number will be start
# Second number will be end + 1
# third number is the step

chai_type = "Ginger chai"
customer_name = "ashar"

print(f"Order for {customer_name} : {chai_type} please !")

chai_description = "Aromatice and Bold"
print(f"First Word: {chai_description[0:8]}")   # or you can remove 0
print(f"First Word: {chai_description[0:8:2]}")
print(f"First Word: {chai_description[12:]}")

# Reverse a string
print(f"Reversed: {chai_description[::-1]}")

label_text = "Chai Special"
encoded_label = label_text.encode("utf-8")
decoded_label = encoded_label.decode("utf-8")
print(f"Non Encoded Label : {label_text}")
print(f"Encoded Label : {encoded_label}")
print(f"Decoded Label : {decoded_label}")