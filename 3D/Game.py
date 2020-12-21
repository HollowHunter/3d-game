import pygame
from Math import Math
import Object
from Phisics import Phisics
from EventSystem import EventSystem
import Loader
import os

class Game:
    def __init__(self):
        self.Math = Math()
        self.Object = Object
        self.pygame = pygame
        self.EventSystem = EventSystem
        self.cameras = []
        self.Loader = Loader

    def init(self):
        self.pygame.init()
        print("Hello!\nOther inits: init_screen, init_phisics\nGood Luck!")

    def init_screen(self, size, window_name):
        self.screen = self.pygame.display.set_mode(size, flags=pygame.DOUBLEBUF)
        self.screen_size = size

    def init_phisics(self, map_=[([], [])], g=10):
        self.Phisics = Phisics(map_, g)

    def add_object(self, obj):
#        self.EventSystem.add_object_func(obj.update)
        self.Phisics.add_object(obj)

    def add_camera(self, obj):
        self.cameras.append(obj)

    def quit(self, event):
        self.pygame.quit()
        exit(0)