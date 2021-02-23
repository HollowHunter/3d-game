class EventSystem:
    def __init__(self, game):
        self.game = game
        self.connects = {game.pygame.QUIT: [game.quit]}
        self.objects = []
        self.FPS = 30
        self.clock = game.pygame.time.Clock()

    def set_fps(self, fps):
        self.FPS = fps

    def connect(self, event_type, func):
        if event_type not in self.connects.keys():
            self.connects[event_type] = [func]
        else:
            self.connects[event_type].append(func)

    def add_obj(self, obj):
        self.objects.append(obj)

    def refresh(self):
        for event in self.game.pygame.event.get():
            if event.type in self.connects.keys():
                [i(event) for i in self.connects[event.type]]

        [i.refresh() for i in self.objects]
        self.clock.tick(self.FPS)