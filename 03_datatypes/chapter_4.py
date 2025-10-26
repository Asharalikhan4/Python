is_boiling = True
stir_count = 5
total_actions = stir_count + is_boiling     # upcasting - here is_boiling will get convert to number with value 1
print(f"Total Actions {total_actions}")

milk_present = 0        # no milk
print(f"Is ther milk? {bool(milk_present)}")

water_hot = True
tea_added = False
can_serve = water_hot and tea_added
print(f"Can serve chai? {can_serve}")