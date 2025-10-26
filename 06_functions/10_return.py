def make_chai():
    return "Here is your masala chai"

return_value = make_chai()
print(return_value)


# Returning multiple values

def chai_report():
    return 100, 20, 50  # Sold, remaining

sold, remaining, _ = chai_report()
print("Sold", sold)
print("Remaining", remaining)