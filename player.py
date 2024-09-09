class Player:
    def __init__(self, icon="P"):
        self.icon = icon
        self.hp = 100
        self.attack = 10
        self.inventory = ["Sword", "Apple"]
        self.level = 1
        
    def get_icon(self):
        return self.icon
    
    def get_hp(self):
        return self.hp

    def get_attack(self):
        return self.attack
    
    def get_inventory(self):
        return self.inventory
    
    def set_icon(self, icon):
        self.icon = icon
    
    def set_hp(self, hp):
        self.hp = hp
        
    def set_attack(self, attack):
        self.attack = attack
        
    def set_inventory(self, inventory):
        self.inventory = inventory
        
    def set_level(self, level):
        self.level = level
    
    def get_player_info(self):
        return [
            f" ",
            f"Player Info:",
            f"Health: {self.hp}",
            f"Attack: {self.attack}",
            f"Inventory: {', '.join(self.inventory)}"
        ]
