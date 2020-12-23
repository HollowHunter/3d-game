import pygame
from pygame import gfxdraw
from math import sin, cos, tan, radians, atan2, atan, degrees

file_name = input('имя obj файла, пустая строка - системное имя:')
if file_name == '':
    file_name = 'кактус.obj'

cosd = lambda x: cos(radians(x))
sind = lambda x: sin(radians(x))
tand = lambda x: tan(radians(x))
atand = lambda x: degrees(atan(x))

z_matrix = lambda a: [[cosd(a), -sind(a), 0],
                      [sind(a), cosd(0), 0],
                      [0, 0, 1]]

plots = []  # список вершин
polygons = []
step_x = 5  # Начальный сдвиг
step_y = 0
step_z = 2



cam_angles = (0, 0, 0)
local_cam_angles = (0, 0, 0)
cam_pos = (0, 0, 0)

size = (1000, 800)
scale = 800
dpi = 75
speed = 5e-2


def v_sum(a, b):
    if type(a) in [int, float, complex, str] and type(b) in [int, float, complex, str]:
        return a + b
    res = [v_sum(i, j) for i, j in zip(a, b)]
    if type(a) == tuple:
        return tuple(res)
    else:
        return res


def m_v_sub(vector, matrix):
    res = []
    print(matrix, vector)
    for line in matrix:
        print('   ', line, vector, res)
        res.append(sum([i * j for i, j in zip(line, vector)]))
    return tuple(res)


with open(file_name, 'r', encoding='utf8') as f_read:  # Открытие obj файла
    for elem in f_read.readlines():
        string = elem.split()
        if string[0] == 'v':  # Вытаскиваем корды точек
            plots.append((float(string[1]) + step_x, float(string[3]) + step_z, -float(string[2]) - step_y))
        elif string[0] == 'f':
            pol = []
            # for i in range(1, len(string)):  # Создаём линии по полигонам
            #     if len(string) == 4:
            #         # polygons.append(v_sum(tuple(map(lambda x: int(x) - 1, string[i].split('/'))), (step_x, step_y, -step_z)))
            #         pol.append(int(string[i].split('/')[0]) - 1)
            #     else:
            #         []
            # polygons.append(tuple(pol))
            string = list(map(lambda x: int(x.split('/')[0]) - 1, string[1:]))
            polygons.extend([(string[0], string[i], string[i + 1]) for i in range(1, len(string) - 1)])

# plots = [(5, -1, -1), (5, 1, 1), (5, -1, 1), (5, 1, -1), (7, -1, -1), (7, 1, -1), (7, -1, 1), (7, 1, 1)]
# polygons = [(0, 3, 2), (1, 3, 2), (4, 5, 6), (5, 6, 7)]

print(len(polygons))



def rot(pos, cam, rot_data):
    x, y, z = pos
    x0, y0, z0 = cam
    (cos_a, sin_a), (cos_b, sin_b), (cos_c, sin_c) = tuple(rot_data)

    x -= x0
    y -= y0
    z += z0

    x, y, z = x, cos_a * y - sin_a * z, sin_a * y + cos_a * z

    x, y, z = cos_b * x + sin_b * z, y, cos_b * z - sin_b * x

    x, y, z = cos_c * x - sin_c * y, cos_c * y + sin_c * x, z

    # print(pos, (round(x, 5), round(y, 5), round(z, 5)), (x**2+y**2+z**2)-(pos[0]**2 + pos[1]**2 + pos[2]**2))

    return (round(x, 5), round(y, 5), round(z, 5))


prior = lambda data: sum([i ** 2 for i in data])

pygame.init()

width, height = size
delta_x, delta_y = width / 2, height / 2

screen = pygame.display.set_mode(size)


def calc():
    render_data = []
    cam_angles_data = []
    cam_angles_data.append((cosd(cam_angles[0]), sind(cam_angles[0])))
    cam_angles_data.append((cosd(cam_angles[1]), sind(cam_angles[1])))
    cam_angles_data.append((cosd(cam_angles[2]), sind(cam_angles[2])))
    cam_angles_data = tuple(cam_angles_data)
    rot_plots = []
    pixels = []
    prioritis = []
    for plot in plots:
        plot = rot(plot, cam_pos, cam_angles_data)
        rot_plots.append(plot)
        if plot[0] > 0:
            x, y = plot[1] / plot[0] * scale, plot[2] / plot[0] * scale
            pixels.append((x, y))
        else:
            pixels.append(False)
        prioritis.append(prior(plot))

    for poly in polygons:
        a, b, c = poly
        p_a, p_b, p_c = prioritis[a], prioritis[b], prioritis[c]
        if pixels[a] and pixels[b] and pixels[c]:
            render_data.append(((pixels[a], pixels[b], pixels[c]), min(p_a, p_b, p_c)))

    return map(lambda x: x[0], sorted(render_data, key=lambda x: x[1], reverse=True))


def render(screen, data):
    for poly in data:
        if poly[0] != poly[1] or poly[1] != poly[2] or poly[0] != poly[2]:
            # pygame.draw.polygon(screen, (100, 100, 100), v_sum(poly, [(delta_x, delta_y)] * 3))
            pygame.draw.polygon(screen, (255, 255, 255), v_sum(poly, [(delta_x, delta_y)] * 3), 1)




clock = pygame.time.Clock()
clock.tick()

time_last = 0
time = 0

fps = 120
running = True
pressed_key = []
clock = pygame.time.Clock()
clockfps = pygame.time.Clock()
clock.tick()
for i in range(1000000):
    # screen.fill((255, 255, 255), (50, 50, 1, 1))  # 602 mls
    # screen.set_at((50, 50), (255, 255, 255))  # 500 mls
    pygame.gfxdraw.pixel(screen, 50, 50, (255, 255, 255))

print('test', clock.tick())
while running:
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, width, height))  # Очистку экрана перенёс сюда

    d_t = pygame.time.get_ticks() - time
    time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                cam_pos = v_sum(cam_pos, (0, 0, speed * 1))
            elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                cam_pos = v_sum(cam_pos, (0, 0, -speed * 1))
            elif event.key in (pygame.K_UP, pygame.K_w):
                cam_pos = v_sum(cam_pos, ((speed * cosd(cam_angles[2]) * 1), -speed * sind(cam_angles[2]), 0))
                # print(((1e-5*cosd(cam_angles[2])*d_t), 1e-5*sind(cam_angles[2])*d_t, 0), ((1e-5*cosd(cam_angles[2])*d_t)**2 + (1e-5*sind(cam_angles[2])*d_t)**2)**0.5 - 1e-5*d_t)
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                cam_pos = v_sum(cam_pos, (-(speed * cosd(cam_angles[2]) * 1), speed * sind(cam_angles[2]) * 1, 0))
            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                cam_pos = v_sum(cam_pos, ((speed * sind(cam_angles[2]) * 1), speed * cosd(cam_angles[2]) * 1, 0))
            elif event.key in (pygame.K_LEFT, pygame.K_a):
                cam_pos = v_sum(cam_pos, (-(speed * sind(cam_angles[2]) * 1), -speed * cosd(cam_angles[2]) * 1, 0))
            pressed_key.append(event.key)
        elif event.type == pygame.KEYUP:
            del pressed_key[pressed_key.index(event.key)]

        elif event.type == pygame.MOUSEMOTION:
            if event.buttons == (1, 0, 0) or event.buttons == (0, 1, 0):
                local_cam_angles = v_sum(local_cam_angles, (0, event.rel[1] / scale * dpi, -event.rel[0] / scale * dpi))
                cam_angles = (sind(local_cam_angles[2])*local_cam_angles[1], cosd(local_cam_angles[2])*local_cam_angles[1], local_cam_angles[2])
                print(cam_angles, local_cam_angles)

    for key in pressed_key: # Передвижение при удержании клавиши
        if key == pygame.K_SPACE:
            cam_pos = v_sum(cam_pos, (0, 0, speed * 1))
        elif key == pygame.K_LSHIFT:
            cam_pos = v_sum(cam_pos, (0, 0, -speed * 1))
        elif key in (pygame.K_UP, pygame.K_w):
            cam_pos = v_sum(cam_pos, ((speed * cosd(cam_angles[2]) * 1), -speed * sind(cam_angles[2]), 0))
            # print(((1e-5*cosd(cam_angles[2])*d_t), 1e-5*sind(cam_angles[2])*d_t, 0), ((1e-5*cosd(cam_angles[2])*d_t)**2 + (1e-5*sind(cam_angles[2])*d_t)**2)**0.5 - 1e-5*d_t)
        elif key in (pygame.K_DOWN, pygame.K_s):
            cam_pos = v_sum(cam_pos, (-(speed * cosd(cam_angles[2]) * 1), speed * sind(cam_angles[2]) * 1, 0))
        elif key in (pygame.K_RIGHT, pygame.K_d):
            cam_pos = v_sum(cam_pos, ((speed * sind(cam_angles[2]) * 1), speed * cosd(cam_angles[2]) * 1, 0))
        elif key in (pygame.K_LEFT, pygame.K_a):
            cam_pos = v_sum(cam_pos, (-(speed * sind(cam_angles[2]) * 1), -speed * cosd(cam_angles[2]) * 1, 0))

    pygame.draw.rect(screen, (0, 0, 0), (0, 0, width, height))
    clock.tick()
    render_data = calc()
    print('math:', clock.tick())
    render(screen, render_data)
    print('render:', clock.tick())
    # cam_angles = (0, cam_angles[1]+1, 0)
    clockfps.tick(fps)
    pygame.display.flip()


pygame.quit()
