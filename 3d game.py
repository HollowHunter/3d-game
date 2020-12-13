import pygame
from math import sin, cos, tan, radians, atan2
from threading import Thread


file_name = input('имя obj файла, пустая строка - системное имя:')
if file_name == '':
    file_name = 'кактус.obj'

points = []  # список вершин
map_ = []
step_x = 5  # Начальный сдвиг
step_y = 0
step_z = 2

# D:\3 ЛИЧНЫЕ ПАПКИ\Женя\3д моделирование\3д дижок\1.obj
# D:\3 ЛИЧНЫЕ ПАПКИ\Женя\3д моделирование\Домик на интенсиве\home_modle.obj
# D:\3 ЛИЧНЫЕ ПАПКИ\Женя\3д моделирование\чистый сосуд\бошка сосуда.obj
clock = pygame.time.Clock()
clock.tick()
with open(file_name, 'r', encoding='utf8') as f_read:  # Открытие obj файла
    for elem in f_read.readlines():
        string = elem.split()
        if string[0] == 'v':  # Вытаскиваем корды точек
            points.append((float(string[1]) + step_x, float(string[3]) + step_z, -float(string[2]) - step_y))
        elif string[0] == 'f':
            for i in range(1, len(string) - 2):  # Создаём линии по полигонам
                map_.append((points[int(string[i].split('/')[0]) - 1], points[int(string[i + 1].split('/')[0]) - 1]))
            map_.append((points[int(string[1].split('/')[0]) - 1], points[int(string[-1].split('/')[0]) - 1]))
print('load', clock.tick())
print('Колличество вершин', len(points))


# map_ = [((6, 1, -0.5), (5, -1, 0)), ((6, 1, 0), (5, 1, 2)), ((5, -1, 0), (5, -1, 2)), \
#         ((7, 1, 0), (7, -1, 0)), ((7, 1, 0), (7, 1, 2)), ((7, -1, 0), (7, -1, 2)), \
#         ((5, 1, 0), (7, 1, 0)), ((5, -1, 0), (7, -1, 0)), ((5, 1, 2), (7, 1, 2))]

cam_angles = (0, 0, 0)
cam_pos = (0, 0, 0)

size = (640, 480)
scale = 400
dpi = 50
speed = 1e-5


def rot(pos, cam, rot_data):
    x, y, z = pos
    x0, y0, z0 = cam
    (cos_a, sin_a), (cos_b, sin_b), (cos_c, sin_c) = tuple(rot_data)

    x -= x0
    y -= y0
    z += z0

    x, y, z = x, cos_a* y - sin_a * z, sin_a * y + cos_a * z

    x, y, z = cos_b * x + sin_b * z, y, cos_b * z - sin_b * x

    x, y, z = cos_c * x - sin_c * y, cos_c * y + sin_c * x, z

    # print(pos, (round(x, 5), round(y, 5), round(z, 5)), (x**2+y**2+z**2)-(pos[0]**2 + pos[1]**2 + pos[2]**2))

    return (round(x, 5), round(y, 5), round(z, 5))


pygame.init()

width, height = size
delta_x, delta_y = width / 2, height / 2

screen = pygame.display.set_mode(size)


def multiShow(cam_data, min, max):  # Наша многопоточная функция
    global arr_of_plot
    for line in map_[min:max]:
        plot1, plot2 = line
        plot1 = rot(plot1, cam_pos, cam_data)
        plot2 = rot(plot2, cam_pos, cam_data)

        if plot1[0] > 0 and plot2[0] > 0:
            arr_of_plot.append((plot1, plot2))



def render():
    global arr_of_plot
    cam_angles_data = []
    cam_angles_data.append((dcos(cam_angles[0]), dsin(cam_angles[0])))
    cam_angles_data.append((dcos(cam_angles[1]), dsin(cam_angles[1])))
    cam_angles_data.append((dcos(cam_angles[2]), dsin(cam_angles[2])))
    arr_of_river = []  # Объекты потоков
    arr_of_plot = []
    for i in range(multiMathCount):
        if i != multiMathCount - 1:
            variable = Thread(target=multiShow, args=(cam_angles_data,
                                                      one_piece * i, one_piece * (i + 1)),
                              daemon=True)
        else:
            variable = Thread(target=multiShow, args=(cam_angles_data,
                                                      one_piece * i, len(map_)),
                              daemon=True)
        variable.start()
        arr_of_river.append(variable)
    for elem in arr_of_river:  # Остонавливаем потоки
        elem.join()
    for plots in arr_of_plot:  # Рисуем труды потоков
        plot1, plot2 = plots
        x1, y1 = plot1[1] / plot1[0] * scale, plot1[2] / plot1[0] * scale
        x2, y2 = plot2[1] / plot2[0] * scale, plot2[2] / plot2[0] * scale
        pygame.draw.line(screen, (255, 255, 255), (int(x1 + delta_x), int(y1 + delta_y)),
                         (int(x2 + delta_x), int(y2 + delta_y)))


    pygame.display.flip()


def v_sum(a, b):
    if type(a) in [int, float, complex, str] and type(b) in [int, float, complex, str]:
        return a + b
    res = [v_sum(i, j) for i, j in zip(a, b)]
    if type(a) == tuple:
        return tuple(res)
    else:
        return res


dcos = lambda x: cos(radians(x))
dsin = lambda x: sin(radians(x))

time = 0

multiMathCount = 15  # Колличевство потоков
one_piece = len(map_) // multiMathCount  # размер кусочка, который будет обрабатывать поток
arr_of_plot = []  # Здесь будут лежать труды многопоточности


running = True
pygame.draw.rect(screen, (0, 0, 0), (0, 0, width, height))
render()
while running:
    d_t = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            clock.tick()
            if event.key == pygame.K_SPACE:
                cam_pos = v_sum(cam_pos, (0, 0, speed * d_t))
            elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                cam_pos = v_sum(cam_pos, (0, 0, -speed * d_t))
            elif event.key == pygame.K_UP:
                cam_pos = v_sum(cam_pos, ((speed * dcos(cam_angles[2]) * d_t), -speed * dsin(cam_angles[2]) * d_t, 0))
                # print(((1e-5*dcos(cam_angles[2])*d_t), 1e-5*dsin(cam_angles[2])*d_t, 0), ((1e-5*dcos(cam_angles[2])*d_t)**2 + (1e-5*dsin(cam_angles[2])*d_t)**2)**0.5 - 1e-5*d_t)
            elif event.key == pygame.K_DOWN:
                cam_pos = v_sum(cam_pos, (-(speed * dcos(cam_angles[2]) * d_t), speed * dsin(cam_angles[2]) * d_t, 0))
            elif event.key == pygame.K_RIGHT:
                cam_pos = v_sum(cam_pos, ((speed * dsin(cam_angles[2]) * d_t), speed * dcos(cam_angles[2]) * d_t, 0))
            elif event.key == pygame.K_LEFT:
                cam_pos = v_sum(cam_pos, (-(speed * dsin(cam_angles[2]) * d_t), -speed * dcos(cam_angles[2]) * d_t, 0))
            print('math', clock.tick())
            pygame.draw.rect(screen, (0, 0, 0), (0, 0, width, height))
            render()
            print('render', clock.tick())
        elif event.type == pygame.MOUSEMOTION:
            if event.buttons == (0, 1, 0):
                clock.tick()
                cam_angles = v_sum(cam_angles, (0, 0, event.rel[0] / scale * dpi))
                print('math', clock.tick())
                pygame.draw.rect(screen, (0, 0, 0), (0, 0, width, height))
                render()
                print('render', clock.tick())

pygame.quit()
