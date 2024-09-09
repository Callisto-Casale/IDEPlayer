from controller import Controller
from map import Map
from player import Player

player = Player()

world = Map(width=10, height=10, viewport_width=8, viewport_height=8, player=player)
controller = Controller(world, player)
controller.start()