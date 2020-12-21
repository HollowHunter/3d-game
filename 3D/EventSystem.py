#import pygame

class EventSystem:
    def __init__(self, game):
        self.pygame = game.pygame
        self.events = {}
        self.keys_down = {}
        self.keys_up = {}
        self.refresh_func = []
        self.connect(game.pygame.QUIT, game.quit)

    def connect(self, event, function):
        if event in self.events:
            self.events[event].append(function)
        else:
            self.events[event] = [function]

    def add_object_func(self, func):
        self.refresh_func.append(func)

    def add_key_up_func(self, key, func):
        if key in self.keys_up:
            self.keys_up[key].append(func)
        else:
            self.keys_up[key] = [func]

    def add_key_down_func(self, key, func):
        if key in self.keys_down:
            self.keys_down[key].append(func)
        else:
            self.keys_down[key] = [func]

    def refresh(self):
        events = self.pygame.event.get()
        for event in events:
            if event.type in self.events.keys():
                for func in self.events[event.type]:
                    func(event)
            if event.type == self.pygame.KEYDOWN:
                if event.key in self.keys_down.keys():
                    for func in self.keys_down[event.key]:
                        func(event)
            elif event.type == self.pygame.KEYUP:
                if event.key in self.keys_up.keys():
                    for func in self.keys_up[event.key]:
                        func(event)
        for func in self.refresh_func:
            func()