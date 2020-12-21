class DynamicObject:
    def __init__(self, game, name, map_, center=(0, 0, 0), mass=0):
        self.name = name
        self.plots = map_[0]
        self.polygons = map_[1]
        self.center = center
        self.mass = 0
        self.rotation = (0, 0, 0)
        self.coordinates_on_parent = (0, 0, 0)
        self.game = game
        self.math = game.Math
        self.child_obj = []
        self.mass = 0
        self.update = bool
        self.parent = 'map'

    def set_parent(self, obj):
        self.parent = obj

    def rotate(self, angles):
        self.rotation = self.math.m_sum(self.rotation, angles)
        a, b, c = self.rotation
        a %= 360
        b %= 360
        c %= 360
        self.rotation = (a, b, c)

    def get_local_rotation(self):
        return self.rotation

    def get_coordinates_on_parent(self):
        return self.coordinates_on_parent

    def get_parent(self):
        return self.parent

    def move(self, delta):
        self.coordinates_on_parent = self.math.m_sum(self.coordinates_on_parent, delta)

    def add_child(self, obj):
        self.child_obj.append(obj)
        obj.set_parent(self)

    def set_pos(self, pos):
        self.coordinates_on_parent = pos

    def set_rotation(self, rot):
        self.rotation = rot

    def get_render_data(self):
        plots = self.math.rotate_plots(self.plots, self.math.rotate_data(self.rotation), self.center)
        plots = [self.math.m_sum(plot, self.coordinates_on_parent) for plot in plots]
        data_self = (plots, self.polygons)
        data_child = []
        for obj in self.child_obj:
            for struct in obj.get_render_data():
                (plots, polygons) = struct
                plots = self.math.rotate_plots(plots, self.math.rotate_data(self.rotation), self.center)
                plots = [self.math.m_sum(plot, self.coordinates_on_parent) for plot in plots]
                data_child.append((plots, polygons))
        return [data_self] + data_child

    def connect(self, EventSystem, func):
        self.update = func
        EventSystem.add_object_func(self.update)


class Camera:
    def __init__(self, game, size, scale):
        self.size = size
        self.scale = scale
        self.pos = (0, 0, 0)
        self.angles = (0, 0, 0)
        self.local_angles = (0, 0, 0)
        self.game = game
        self.math = game.Math
        self.parent = 'map'

    def move(self, delta):
        x, y, z = delta
        x, y = self.math.cosd(self.angles[2]) * x + self.math.sind(self.angles[2]) * y, \
               -self.math.sind(self.angles[2]) * x + self.math.cosd(self.angles[2]) * y
        self.pos = self.math.m_sum(self.pos, (x, y, z))

    def rotate(self, angles):
        a, b, c = self.math.m_sum(self.local_angles, angles)
        a1, b1, c1 = a, b, c
        # a %= 360
        # b %= 360
        # c %= 360
        if a != a1 or b != b1 or c != c1:
            print((a, b, c), (a1, b1, c1))
        self.local_angles = [a, b, c]
        self.angles = self.math.local_angles_to_global((a, b, c))

    def set_pos(self, pos):
        self.pos = pos

    def set_rotation(self, rot):
        self.local_angles = rot
        self.angles = self.math.local_angles_to_global(rot)

    def get_rotation(self):
        return self.local_angles

    def get_pos(self):
        return self.pos

    def set_parent(self, obj):
        self.parent = obj
        if obj != 'map':
            print("error!!!\nThis code")
            exit()

    def calc_pre_render(self):
        plots, polygons = self.game.Phisics.get_map()[0]
        # plots, polygons = list, list
        polygons = polygons.copy()
        plots = plots.copy()
        for object in self.game.Phisics.get_map()[1:]:
            for struct in object.get_render_data():
                obj_plots, obj_polygons = struct
                delta = len(plots)
                plots.extend(obj_plots)
                polygons.extend([self.math.m_sum(i, [delta, delta, delta]) for i in obj_polygons])
        rot_data = self.math.rotate_data(self.angles)
        plots = self.math.rotate_plots(plots, rot_data, self.pos, True)
        # ban = [i for i in plots if i[0] <= 0]
        pixels = [(int(plot[1] / plot[0] * self.scale + self.size[0] / 2),
                   int(plot[2] / plot[0] * self.scale + self.size[0] / 2)) if (plot[0] > 1e-5) else (False) for plot in
                  plots]
        return (pixels, polygons)

    def render(self, pre_render):
        self.game.screen.fill([0, 0, 0])
        pixels = pre_render[0]
        for polygon in pre_render[1]:
            if all([pixels[i] for i in polygon]):
                self.game.pygame.draw.polygon(self.game.screen, (255, 255, 255), [pixels[i] for i in polygon], 1)


if __name__ == '__main__':
    sqr1 = DynamicObject('sqr1',
                         [[(0, -0.5, -0.5), (0, -0.5, 0.5), (0, 0.5, 0.5), (0, 0.5, -0.5)], [(0, 1, 2), (0, 3, 2)]])
    sqr1.move((5, 0, 0))
    sqr1.rotate((0, 90, 0))
    sqr2 = DynamicObject('sqr2',
                         [[(0, -0.5, -0.5), (0, -0.5, 0.5), (0, 0.5, 0.5), (0, 0.5, -0.5)], [(0, 1, 2), (0, 3, 2)]])
    sqr1.add_child(sqr2)
    sqr2.move((-1, 0, 0))
    a = sqr1.get_render_data()
    exit()
