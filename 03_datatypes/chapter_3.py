# Integar

black_tea_gram = 14
ginger_grams = 3

total_grams = black_tea_gram + ginger_grams
print(f"Total gram of base tea is {total_grams}")

remaining_tea = black_tea_gram - ginger_grams
print(f"Total gram of remaining tea is {remaining_tea}")

milk_liters = 7
servings = 4
milk_per_servings = milk_liters / servings
print(f"Milk per servings {milk_per_servings}")

# we use // ( double backslash where we don't care about what comes after the decimal)
total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"While tea bags per pot {bags_per_pot}")

total_cadamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cadamom_pods % pods_per_cup
print(f"Leftover cadamom pods {leftover_pods}")

base_flavour_strength = 2
scale_factor = 3
powerful_flavour = base_flavour_strength ** scale_factor
print(f"Scaled flavour strength {powerful_flavour}")

total_tea_leaves_harvested = 1_000_000_000
print(total_tea_leaves_harvested)