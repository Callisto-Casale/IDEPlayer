class Player:
    def __init__(self, icon="P"):
        self.icon = icon
        self.hp = 100
        self.attack = 10
        self.inventory = ["Sword", "Apple"]
        
    def get_icon(self):
        return self.icon
    
    def get_hp(self):
        return self.hp

    def get_attack(self):
        return self.attack
    
    def get_inventory(self):
        return self.inventory

    def get_player_info(self):
        return [
            f" ",
            f"Player Info:",
            f"Health: {self.hp}",
            f"Attack: {self.attack}",
            f"Inventory: {', '.join(self.inventory)}"
        ]
