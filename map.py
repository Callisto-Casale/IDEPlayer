from typing import List
import random
import os

class Map:
    def __init__(self, width, height, viewport_width, viewport_height, player):
        self.width = width
        self.height = height
        self.viewport_width = viewport_width
        self.viewport_height = viewport_height
        
        self.player_x = self.width // 2
        self.player_y = self.height // 2
        self.player = player
        
        self.map = self.generate_map()
    
    def get_viewport(self):
        return self.viewport_width, self.viewport_height
    
    def set_viewport(self, width, height):
        self.viewport_width = width
        self.viewport
        
    def get_map(self):
        return self.width, self.height
    
    def set_map(self, width, height):
        self.width = width
        self.height = height
        
    def generate_map(self):
        tiles = [" ", "X", "O"]
        _map =  [[random.choice(tiles) for i in range(self.width)] for j in range(self.height)]

        player_x = self.get_map()[0] // 2
        player_y = self.get_map()[1] // 2
        
        _map[player_y][player_x] = "P"
        
        
        # Add a wall with the ■ character
        for i in range(0, self.width):
            _map[0][i] = "■"
            _map[self.height - 1][i] = "■"
        
        for i in range(0, self.height):
            _map[i][0] = "■"
            _map[i][self.width - 1] = "■"
        
        return _map
    
    def get_player_position(self):
        for y, row in enumerate(self.map):
            for x, cell in enumerate(row):
                if cell == "P":
                    return x, y
    
    def move_player(self, direction):
        x, y = self.get_player_position()
        
        if direction == "w":
            y -= 1
        elif direction == "s":
            y += 1
        elif direction == "a":
            x -= 1
        elif direction == "d":
            x += 1
            
        # Add check, if the player is moving to a valid position and not a wall
        if self.map[y][x] == "■":
            return
        
        if x >= 0 and x < self.width and y >= 0 and y < self.height:
            self.map[y][x] = "P"
            self.map[self.player_y][self.player_x] = " "
            self.player_x = x
            self.player_y = y

    def show_map(self):
        player_info = self.player.get_player_info()  # Get player info to display on the right side
        
        os.system("cls" if os.name == "nt" else "clear")  # Clear the console for a fresh display

        # Get player's position and viewport size
        x, y = self.get_player_position()
        viewport_width, viewport_height = self.get_viewport()

        map_viewport = []  # Store the map lines
        for j in range(y - viewport_height // 2, y + viewport_height // 2):
            line = ""
            for i in range(x - viewport_width // 2, x + viewport_width // 2):
                if 0 <= i < self.width and 0 <= j < self.height:
                    line += self.map[j][i] + " "
                else:
                    line += "  "  # Fill out of bounds with spaces
            map_viewport.append(line)

        # Ensure both the map and player info have the same number of lines
        max_lines = max(len(map_viewport), len(player_info))
        map_viewport += [''] * (max_lines - len(map_viewport))  # Pad map if shorter
        player_info += [''] * (max_lines - len(player_info))  # Pad player info if shorter

        # Print the map with player info side by side
        for map_line, info_line in zip(map_viewport, player_info):
            print(f"{map_line:<{viewport_width * 2}}    {info_line}")



