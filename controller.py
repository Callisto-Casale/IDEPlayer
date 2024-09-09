from map import Map

class Controller:
    def __init__(self, map, player):
        self.map = map
        self.player = player
        
        self.map.generate_map()
    
    def move_player(self, direction):
        self.map.move_player(direction)
    
    def show_map(self):
        self.map.show_map()
        
    def start(self):
        self.show_map()
        while True:
            direction = input("Enter direction: ")
            self.move_player(direction)
            self.show_map()


