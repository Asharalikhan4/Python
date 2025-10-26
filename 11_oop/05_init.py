class ChaiOrder:
    def __init__(self, type_, size) -> None:
        self.type = type_
        self.size = size
    
    def summary(self):
        return f"{self.size}ml of {self.type} chai"

order = ChaiOrder("Masala Chai", 200)
print(order.summary())

order_two = ChaiOrder("Ginger", 220)
print(order_two.summary())