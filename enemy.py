class Enemy:
    def __init__(self, name, hp, damage, type, level):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.type = type
        self.level = level
        
    def get_name(self):
        return self.name
    
    def get_hp(self):
        return self.hp
    
    def get_damage(self):
        return self.damage
    
    def get_type(self):
        return self.type
    
    def get_level(self):
        return self.level
    
    def get_enemy_info(self):
        return [
            f"Enemy Info:",
            f"Name: {self.name}",
            f"HP: {self.hp}",
            f"Damage: {self.damage}",
            f"Type: {self.type}",
            f"Level: {self.level}"
        ]
        
    def get_enemy_list(self):
        return [
            Enemy("Goblin", 100, 10, "Melee", 1),
        ]