from Game import Game


grid_plots = []
n = 20
[[grid_plots.append([x*2, y*2, 0]) for y in range(-n, n)] for x in range(-n, n)]
grid_polygons = []
[[grid_polygons.extend([[x+2*n*y, x+2*n*y+1, x+2*n*(y+1)], [x+2*n*y, x+2*n*y+1, x+2*n*(y+1)+1]]) for x in range(n*2-1)] for y in range(n*2-1)]
grid = (grid_plots, grid_polygons)

game = Game()

game.init()
game.init_phisics()
game.init_screen((800, 600), 'main.py')

game.Phisics.set_map([grid])

cam1 = game.Object.Camera(game, game.screen_size, 600)
game.add_camera(cam1)
cam1.set_pos((-1, -1, 2))





def sqr1_script():
    sqr1.rotate((1, 1, 1))


game.EventSystem1 = game.EventSystem(game)

sqr1 = game.Object.DynamicObject(game, 'sqr1', [[(0, -0.5, -0.5), (0, -0.5, 0.5), (0, 0.5, 0.5), (0, 0.5, -0.5)],
                                                [(0, 1, 2), (0, 3, 2)]])
game.add_object(sqr1)
sqr1.connect(game.EventSystem1, sqr1_script)
sqr1.move((5, 0, 0))

sqr2 = game.Object.DynamicObject(game, 'sqr2', [[(0, -0.5, -0.5), (0, -0.5, 0.5), (0, 0.5, 0.5), (0, 0.5, -0.5)],
                                                [(0, 1, 2), (0, 3, 2)]])
sqr1.add_child(sqr2)
sqr2.move((1, 0, 0))

cam1.cam1_v = (0, 0, 0)
cam1.delta_v = 0.2


def move_cam_up(event):
    cam1.cam1_v = game.Math.m_sum(cam1.cam1_v, (0, 0, cam1.delta_v))


def move_cam_down(event):
    cam1.cam1_v = game.Math.m_sum(cam1.cam1_v, (0, 0, -cam1.delta_v))


def move_cam_left(event):
    cam1.cam1_v = game.Math.m_sum(cam1.cam1_v, (0, -cam1.delta_v, 0))


def move_cam_right(event):
    cam1.cam1_v = game.Math.m_sum(cam1.cam1_v, (0, cam1.delta_v, 0))


def move_cam_forward(event):
    cam1.cam1_v = game.Math.m_sum(cam1.cam1_v, (cam1.delta_v, 0, 0))


def move_cam_backward(event):
    cam1.cam1_v = game.Math.m_sum(cam1.cam1_v, (-cam1.delta_v, 0, 0))


game.EventSystem1.add_key_down_func(game.pygame.K_s, move_cam_backward)
game.EventSystem1.add_key_down_func(game.pygame.K_w, move_cam_forward)
game.EventSystem1.add_key_down_func(game.pygame.K_d, move_cam_right)
game.EventSystem1.add_key_down_func(game.pygame.K_a, move_cam_left)

game.EventSystem1.add_key_down_func(game.pygame.K_UP, move_cam_forward)
game.EventSystem1.add_key_down_func(game.pygame.K_DOWN, move_cam_backward)
game.EventSystem1.add_key_down_func(game.pygame.K_RIGHT, move_cam_right)
game.EventSystem1.add_key_down_func(game.pygame.K_LEFT, move_cam_left)

game.EventSystem1.add_key_down_func(game.pygame.K_LSHIFT, move_cam_down)
game.EventSystem1.add_key_down_func(game.pygame.K_RSHIFT, move_cam_down)
game.EventSystem1.add_key_down_func(game.pygame.K_SPACE, move_cam_up)


def key_up(event):
    if event.key in [game.pygame.K_SPACE, game.pygame.K_LSHIFT, game.pygame.K_RSHIFT]:
        cam1.cam1_v = (cam1.cam1_v[0], cam1.cam1_v[1], 0)
    elif event.key in [game.pygame.K_w, game.pygame.K_s, game.pygame.K_UP, game.pygame.K_DOWN]:
        cam1.cam1_v = (0, cam1.cam1_v[1], cam1.cam1_v[2])
    elif event.key in [game.pygame.K_a, game.pygame.K_s, game.pygame.K_LEFT, game.pygame.K_RIGHT]:
        cam1.cam1_v = (cam1.cam1_v[0], 0, cam1.cam1_v[2])


game.EventSystem1.connect(game.pygame.KEYUP, key_up)


def move_cam1():
    cam1.move(cam1.cam1_v)


game.EventSystem1.add_object_func(move_cam1)

cam1.dpi = 100


def rotate_cam1(event):
    if event.buttons == (1, 0, 0):
        # print(event.dict)
        cam1.rotate((0, event.rel[1] / cam1.scale * cam1.dpi, -event.rel[0] / cam1.scale * cam1.dpi))


game.EventSystem1.connect(game.pygame.MOUSEMOTION, rotate_cam1)

cactus = game.Object.DynamicObject(game, 'cactus1', game.Loader.ObjectLoader.load('Objects/кактус1.obj'))
game.add_object(cactus)


def rot_cactus():
    cactus.rotate((0, 0, 0.5))


cactus.connect(game.EventSystem1, rot_cactus)

# game.EventSystem1.add_object_func(sqr1_script)

clock = game.pygame.time.Clock()

time_counter = game.pygame.time.Clock()

while True:
    time_counter.tick()
    game.EventSystem1.refresh()
    print('EventSystem1:', time_counter.tick(), end='\t')
    prerender = cam1.calc_pre_render()
    print('PreRender:', time_counter.tick(), end='\t')
    cam1.render(prerender)
    print('Render:', time_counter.tick(), end='\t')
    game.pygame.display.flip()
    print('Display:', time_counter.tick(), end='\t')
    clock.tick(40)
    print('wait:', time_counter.tick(), end='\n\n')
    # print('.', end='')
