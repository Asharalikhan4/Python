class Chai:
    origin = "India"
    
Chai.is_hot = True

print(Chai.origin)
print(Chai.is_hot)

# Creating objects from Class Chai

masala = Chai()
print(f"Masala : {masala.origin}")
print(f"Masala : {masala.is_hot}")

masala.is_hot = False
print(f"Class Value: {Chai.is_hot}")
print(f"Masala : {masala.is_hot}")

masala.flavour = "Masala"
print(f"Masala Object: {Chai.flavour}")