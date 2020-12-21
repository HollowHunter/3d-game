class Phisics:
    def __init__(self, map_, g):
        self.area = map_
        self.g = g

    def set_map(self, map_):
        self.area = map_

    def add_object(self, obj):
        self.area.append(obj)

    def get_map(self):
        return self.area