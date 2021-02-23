class BaseObject:
    def __init__(self, game):
        """Creates base object structure"""
        self.c_part = None
        self.c_plots = bytes()
        self.plots_len = 0
        self.c_polygons = bytes()
        self.poly_len = 0
        self.istextures = 0
        self.tex_id = 0
        self.tex_plots = bytes()
        self.tex_plots_len = 0
        self.c_surfaces = bytes()
        self.iscamera = 0
        self.game = game
        self.c_lib = game.lib
        self.converter = game.Converter
        self.refresh_func = []



    def init(self):
        # create_object(plots_len, plots_in, poly_len, polygons_in, istextured, tex_id, tex_plots_len, tex_plots_in, iscamera)
        self.c_part = self.game.lib.create_object(self.plots_len, self.c_plots,
                                                  self.poly_len, self.c_polygons,
                                                  self.istextures, self.tex_id,
                                                  self.tex_plots_len, self.tex_plots, self.c_surfaces,
                                                  self.iscamera)
    def recalc_pos(self):
        self.game.lib.recalc_object(self.c_part)

    def move(self, delta):
        self.c_lib.move_object(self.c_part, delta[0], delta[1], delta[2])

    def rotate(self, ang):
        self.c_lib.rotate_object(self.c_part, ang[0], ang[1], ang[2])

    def set_pos(self, pos):
        self.c_lib.place_object(self.c_part, pos[0], pos[1], pos[2])

    def set_rot(self, rot):
        self.c_lib.set_rot_object(self.c_part, rot[0], rot[1], rot[2])

    def refresh(self):
        [i(self) for i in self.refresh_func]

    def connect(self, func):
        self.refresh_func.append(func)


class DynamicObject(BaseObject):
    def __init__(self, game, parametrs=[[], [], [], []], texture_id=0):
        super(DynamicObject, self).__init__(game)
        # print(*parametrs, sep='\n')
        self.set_plots(parametrs[0])
        self.set_polygons(parametrs[1])
        self.set_tex_plots(parametrs[2])
        self.set_tex_surfaces(parametrs[3])

        self.set_tex_id(texture_id)

    def set_plots(self, plots=[]):
        if plots:
            self.c_plots = self.converter.to_float_array(self.converter.convert_2d(plots))
            self.plots_len = len(plots)

    def set_polygons(self, polygons=[]):
        if polygons is None:
            polygons = []
        if polygons:
            self.c_polygons = self.converter.to_int_array(self.converter.convert_2d(polygons))
        self.poly_len = len(polygons)

    def set_tex_id(self, id=0):
        self.tex_id = id
        self.istextures = 1

    def set_tex_plots(self, plots=[]):
        if plots:
            self.tex_plots = self.converter.to_float_array(self.converter.convert_2d(plots))
            self.c_surfaces = self.c_polygons
            self.tex_plots_len = len(plots)

    def set_tex_surfaces(self, surfaces=[]):
        self.c_surfaces = self.converter.to_int_array(self.converter.convert_2d(surfaces))


class Camera(BaseObject):
    def __init__(self, game):
        super(Camera, self).__init__(game)
        self.iscamera = 1

    def get_img(self, size_x, size_y, scale):
        # render_plots(map_in, cam_in, size_x, size_y, scale)
        c_res = self.c_lib.render_plots(self.game.map, self.c_part, size_x, size_y, scale)
        res = self.game.ffi.unpack(c_res, size_x * size_y * 3)
        self.c_lib.free_mem(c_res)
        return self.game.pygame.image.fromstring(res, (size_x, size_y), 'RGB')

    def render(self, scale):
        self.game.screen.blit(self.get_img(self.game.screen_size[0], self.game.screen_size[1], scale), (0, 0))
        self.game.pygame.display.flip()
