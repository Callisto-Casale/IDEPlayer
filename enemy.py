import json
import random

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
        with open("enemy_list.json", "r") as file:
            enemies = json.load(file)
        
        return enemies
    
    def get_specific_enemy(self):
        enemies = self.get_enemy_list()
        
        for enemy in enemies:
            if enemy["name"] == self.name:
                return enemy
    
    def get_level_enemy(self, type: str):
        enemies = self.get_enemy_list()
        
        return enemies["enemies"][type]
            
    def get_random_enemy(self, type):
        enemies = self.get_level_enemy(type)
        
        return random.choice(enemies)
    
    def get_random_level_enemy(self, level):
        enemies = self.get_enemy_list()
        
        tmp_list = []
        
        for _type in enemies["enemies"]:
            for enemy in enemies["enemies"][_type]:
                if enemy["level"] == level or enemy["level"] == level - 1 or enemy["level"] == level + 1:
                    tmp_list.append(enemy)
        
        return random.choice(tmp_list)

