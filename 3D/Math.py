from math import sin, cos, tan, radians
from numba import jit


class Math:
    cosd = lambda self, a: cos(radians(a))
    sind = lambda self, a: sin(radians(a))
    tand = lambda self, a: tan(radians(a))

    def m_sum(self, matrix_a, matrix_b):
        if type(matrix_a) in [int, float, complex, str] and type(matrix_b) in [int, float, complex, str]:
            return matrix_a + matrix_b
        elif type(matrix_a) in [int, float, complex, str] and type(matrix_b) not in [int, float, complex, str]:
            print('error: mat_a size != mat_b size\n', matrix_a, '\n', matrix_b)
            exit(1)
        elif type(matrix_a) not in [int, float, complex, str] and type(matrix_b) in [int, float, complex, str]:
            print('error: mat_a size != mat_b size\n', matrix_a, '\n', matrix_b)

        res = []
        for a, b in zip(matrix_a, matrix_b):
            res.append(self.m_sum(a, b))

        return tuple(res) if type(matrix_a) == tuple else res

    def rotate_plots(self, plots, rot_data, center=(0, 0, 0), to_zero=False):
        (cos_a, sin_a), (cos_b, sin_b), (cos_c, sin_c) = rot_data
        x0, y0, z0 = center
        res = []
        for plot in plots:
            x, y, z = plot
            x -= x0
            y -= y0
            z += z0

            x, y, z = x, cos_a * y - sin_a * z, sin_a * y + cos_a * z
            x, y, z = cos_b * x + sin_b * z, y, cos_b * z - sin_b * x
            x, y, z = cos_c * x - sin_c * y, cos_c * y + sin_c * x, z

            if to_zero:
                res.append((x, y, z))
            else:
                res.append(self.m_sum((x, y, z), (x0, y0, z0)))
        return (res) if (type(res) == list) else (tuple(res))

    def rotate_polygons(self, polygons, rot_data, center):
        res = []
        for polygon in polygons:
            res.append(self.rotate_plots(polygon, rot_data, center))
        return (res) if (type(res) == list) else (tuple(res))

    def rotate_data(self, angles):
        a, b, c = angles
        return (self.cosd(a), self.sind(a)), (self.cosd(b), self.sind(b)), (self.cosd(c), self.sind(c))

    def local_angles_to_global(self, angles):
        a, b, c = angles
        sin_c = self.sind(c)
        cos_c = self.cosd(c)
        return sin_c * b + cos_c * a, cos_c * b + sin_c * a, c
