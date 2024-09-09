class Item:
    def __init__(self, name, quantity, value):
        self.name = name
        self.quantity = quantity
        self.value = value
        
    def get_name(self):
        return self.name
    
    def get_quantity(self):
        return self.quantity
    
    def get_value(self):
        return self.value
    
    def get_item_info(self):
        return [
            f"Item Info:",
            f"Name: {self.name}",
            f"Quantity: {self.quantity}",
            f"Value: {self.value}"
        ]
    
    