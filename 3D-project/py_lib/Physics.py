#!/usr/bin/python3

class Physics:
    def __init__(self, game):
        self.game = game
        self.pygame = game.pygame
        self.lib = game.lib
        self.ffi = game.ffi
        self.game.map = game.lib.get_map_pointer()
        self.g = 0

    def create_new_map(self):
        if self.game.map:
            print('I can`t delite map now :(')
            pass # Delete old map. Now I can`t do this.
        self.game.map = self.lib.get_map_pointer()

    def add_object_to_map(self, obj):
        self.lib.add_obj_to_map(self.game.map, obj.c_part)
        self.game.EventSystem.add_obj(obj)

    def calc_collisions(self):
        self.lib.collisions(self.game.map)
