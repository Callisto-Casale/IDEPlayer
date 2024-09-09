from controller import Controller
from map import Map

world = Map(10, 10, 8, 8)
controller = Controller(world, None)
controller.start()