from Math import Math
import pygame

class Renderer:
    def __init__(self, size, phisic_map):
        pygame.init()
        self.delta_x, self.delta_y = size[0]/2, size[1]/2
        self.size = size
        self.screen = pygame.display.set_mode(size, flags=pygame.DOUBLEBUF)
        self.map = phisic_map
        self.cam_pos = (-2, 0, 0)
        self.cam_angles = (0, 0, 0)
        self.local_cam_angles = (0, 0, 0)
        self.math = Math()
        self.pygame = pygame
        self.scale = 500

    def calc_pre_render(self):
        plots, polygons = self.map[0]
        #plots, polygons = list, list
        polygons = polygons.copy()
        plots = plots.copy()
        for object in self.map[1:]:
            for struct in object.get_render_data():
                obj_plots, obj_polygons = struct
                delta = len(plots)
                plots.extend(obj_plots)
                polygons.extend([self.math.m_sum(i, (delta, delta, delta)) for i in obj_polygons])
        return plots, polygons

    def render(self, pre_render):
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, self.size[0], self.size[1]))
        plots, polygons = pre_render
        rot_data = self.math.rotate_data(self.cam_angles)
        plots = self.math.rotate_plots(plots, rot_data, (0, 0, 0), self.cam_pos)
        ban = [i for i, j in enumerate(plots) if j[0]<0]
        pixels = [(plot[1]/plot[0]*self.scale+self.delta_x, plot[2]/plot[0]*self.scale+self.delta_y)if(plot[0] > 0)else(0) for plot in plots]
        for poly in polygons:
            a, b, c = poly
            if a not in ban and b not in ban and c not in ban:
                pygame.draw.polygon(self.screen, (255, 255, 255), (pixels[a], pixels[b], pixels[c]), 1)

    def cam_place(self, coords):
        self.cam_pos = coords

    def cam_rotate(self, angles):
        self.local_cam_angles = self.math.m_sum(self.local_cam_angles, angles)
        a, b, c = self.local_cam_angles
        self.cam_angles = (self.math.cosd(c)*b, self.math.sind(c)*b, c)