class Chai:
    temperature = "hot"
    strength = "Strong"

cutting = Chai()
print(cutting.temperature)

cutting.temperature = "Mild"
print("After Changing", cutting.temperature)
print("Direct look into the class", Chai.temperature)

del cutting.temperature
print("After Deleting", cutting.temperature)

cutting.cup = "small"
print("After adding cup", cutting.cup)

del cutting.cup
print("After deleting cup", cutting.cup)