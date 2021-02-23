import sys
sys.path.append('./py_lib')
sys.path.append('./c_lib')
from Game import Game
from Load_funct import load
from Math import v_sum, cosd, sind, tand
import random



game = Game()

pygame = game.pygame

game.init_screen((1180, 1050), fps=60)

'''
0/0/0 1/1/0 3/2/0 2/3/0
2/4/1 3/5/1 7/6/1 6/7/1
6/8/2 7/9/2 5/10/2 4/11/2
4/12/3 5/13/3 1/14/3 0/15/3
2/16/4 6/17/4 4/12/4 0/15/4
7/18/5 3/19/5 1/20/5 5/21/5
'''

b = '''
[[0.75205, 0.749493], [0.75205, 0.999493], [0.50205, 0.999493], [0.50205, 0.749493], 
[1.00086, 0.749268], [1.00086, 0.999268], [0.75086, 0.999268], [0.75086, 0.749268], 
[0.249605, 0.753175], [0.249605, 1.000762], [0.002019, 1.000762], [0.002019, 0.753175], 
[0.500984, 0.75], [0.500984, 1.0], [0.250984, 1.0], [0.250984, 0.75], [0.250977, 0.5], 
[0.500977, 0.5], [-0.000504, 0.500775], [0.249496, 0.500775], [0.249496, 0.750775], 
[-0.000504, 0.750775]]
'''

print(game.add_texture('Objects/cube_texture.png'))
print(game.add_texture('Objects/fragat_text.png'))
print(game.add_texture('Objects/asteroid.png'))
print(game.add_texture('Objects/fighter_tex.png'))
test_obj_0 = game.Object.DynamicObject(game, load('Objects/fregat.obj'), 1)
k = 0.5
ast1 = game.Object.DynamicObject(game, load('Objects/ast1.obj', k), 2)
ast2 = game.Object.DynamicObject(game, load('Objects/ast2.obj', k), 2)
ast3 = game.Object.DynamicObject(game, load('Objects/ast3.obj', k), 2)
ast4 = game.Object.DynamicObject(game, load('Objects/ast4.obj', k), 2)
ast5 = game.Object.DynamicObject(game, load('Objects/ast3.obj', k), 2)
ast6 = game.Object.DynamicObject(game, load('Objects/ast1.obj', k), 2)
ast7 = game.Object.DynamicObject(game, load('Objects/ast1.obj', k), 2)
ast8 = game.Object.DynamicObject(game, load('Objects/ast2.obj', k), 2)
ast9 = game.Object.DynamicObject(game, load('Objects/ast3.obj', k), 2)
# ast10 = game.Object.DynamicObject(game, load('Objects/ast4.obj', k), 2)
# ast11 = game.Object.DynamicObject(game, load('Objects/ast3.obj', k), 2)
# ast12 = game.Object.DynamicObject(game, load('Objects/ast1.obj', k), 2)

fighter1 = game.Object.DynamicObject(game, load('Objects/fighter.obj', k), 3)
fighter2 = game.Object.DynamicObject(game, load('Objects/fighter.obj', k), 3)


plain = game.Object.DynamicObject(game, load('Objects/plain.obj', k), 0)

# test_obj_0 = game.Object.DynamicObject(game)
# test_obj_0.set_plots([[1, 1, 1], [1, -1, 1], [1, 1, -1], [1, -1, -1],
#                       [-1, 1, 1], [-1, -1, 1], [-1, 1, -1], [-1, -1, -1]])
#
# test_obj_0.set_polygons([[0, 1, 2], [0, 2, 3], [2, 3, 7], [2, 7, 6],
#                          [6, 7, 5], [6, 5, 4], [4, 5, 1], [4, 1, 0],
#                          [2, 6, 4], [2, 4, 0], [7, 3, 1], [7, 1, 5]])
#
# test_obj_0.set_tex_id(0)
# test_obj_0.set_tex_plots([[0.75205, 0.749493], [0.75205, 0.999493], [0.50205, 0.999493], [0.50205, 0.749493],
#                           [1.00086, 0.749268], [1.00086, 0.999268], [0.75086, 0.999268], [0.75086, 0.749268],
#                           [0.249605, 0.753175], [0.249605, 1.000762], [0.002019, 1.000762], [0.002019, 0.753175],
#                           [0.500984, 0.75], [0.500984, 1.0], [0.250984, 1.0], [0.250984, 0.75], [0.250977, 0.5],
#                           [0.500977, 0.5], [-0.000504, 0.500775], [0.249496, 0.500775], [0.249496, 0.750775],
#                           [0.0, 0.750775]])
#
# test_obj_0.set_tex_surfaces([[0, 1, 2], [0, 2, 3], [4, 5, 6], [4, 6, 7],
#                              [8, 9, 10], [8, 10, 11], [12, 13, 14], [12, 14, 15],
#                              [16, 17, 12], [16, 12, 15], [18, 19, 20], [18, 20, 21]])






# def move_cam_up(event):
#     cam1.cam1_v = game.Math.m_sum(cam1.cam1_v, (0, 0, cam1.delta_v))
# def move_cam_down(event):
#     cam1.cam1_v = game.Math.m_sum(cam1.cam1_v, (0, 0, -cam1.delta_v))
# def move_cam_left(event):
#     cam1.cam1_v = game.Math.m_sum(cam1.cam1_v, (0, -cam1.delta_v, 0))
# def move_cam_right(event):
#     cam1.cam1_v = game.Math.m_sum(cam1.cam1_v, (0, cam1.delta_v, 0))
# def move_cam_forward(event):
#     cam1.cam1_v = game.Math.m_sum(cam1.cam1_v, (cam1.delta_v, 0, 0))
# def move_cam_backward(event):
#     cam1.cam1_v = game.Math.m_sum(cam1.cam1_v, (-cam1.delta_v, 0, 0))
#
# def move_up(event):
#     global speed_ship
#     speed_ship = game.Math.m_sum(speed_ship, (0, 0, -SPEED_SHIP))
# def move_down(event):
#     global speed_ship
#     speed_ship = game.Math.m_sum(speed_ship, (0, 0, SPEED_SHIP))
# def move_left(event):
#     global speed_ship
#     speed_ship = game.Math.m_sum(speed_ship, (-SPEED_SHIP, 0, 0))
# def move_right(event):
#     global speed_ship
#     speed_ship = game.Math.m_sum(speed_ship, (SPEED_SHIP, 0, 0))
# def move_forward(event):
#     global speed_ship
#     speed_ship = game.Math.m_sum(speed_ship, (0, SPEED_SHIP, 0))
# def move_backward(event):
#     global speed_ship
#     speed_ship = game.Math.m_sum(speed_ship, (0, -SPEED_SHIP, 0))
#
#
# def move_up_stop(event):
#     global speed_ship
#     speed_ship = game.Math.m_sum(speed_ship, (0, 0, SPEED_SHIP))
# def move_down_stop(event):
#     global speed_ship
#     speed_ship = game.Math.m_sum(speed_ship, (0, 0, -SPEED_SHIP))
# def move_left_stop(event):
#     global speed_ship
#     speed_ship = game.Math.m_sum(speed_ship, (SPEED_SHIP, 0, 0))
# def move_right_stop(event):
#     global speed_ship
#     speed_ship = game.Math.m_sum(speed_ship, (-SPEED_SHIP, 0, 0))
# def move_forward_stop(event):
#     global speed_ship
#     speed_ship = game.Math.m_sum(speed_ship, (0, -SPEED_SHIP, 0))
# def move_backward_stop(event):
#     global speed_ship
#     speed_ship = game.Math.m_sum(speed_ship, (0, SPEED_SHIP, 0))


# game.EventSystem.add_key_down_func(game.pygame.K_s, move_backward)
# game.EventSystem.add_key_down_func(game.pygame.K_w, move_forward)
# game.EventSystem.add_key_down_func(game.pygame.K_d, move_right)
# game.EventSystem.add_key_down_func(game.pygame.K_a, move_left)
#
# game.EventSystem.add_key_up_func(game.pygame.K_s, move_backward_stop)
# game.EventSystem.add_key_up_func(game.pygame.K_w, move_forward_stop)
# game.EventSystem.add_key_up_func(game.pygame.K_d, move_right_stop)
# game.EventSystem.add_key_up_func(game.pygame.K_a, move_left_stop)
#
# game.EventSystem.add_key_down_func(game.pygame.K_LSHIFT, move_down)
# game.EventSystem.add_key_down_func(game.pygame.K_RSHIFT, move_down)
# game.EventSystem.add_key_down_func(game.pygame.K_SPACE, move_up)
#
# game.EventSystem.add_key_up_func(game.pygame.K_LSHIFT, move_down_stop)
# game.EventSystem.add_key_up_func(game.pygame.K_RSHIFT, move_down_stop)
# game.EventSystem.add_key_up_func(game.pygame.K_SPACE, move_up_stop)
#
#
# game.EventSystem.add_key_down_func(game.pygame.K_UP, move_cam_forward)
# game.EventSystem.add_key_down_func(game.pygame.K_DOWN, move_cam_backward)
# game.EventSystem.add_key_down_func(game.pygame.K_RIGHT, move_cam_right)
# game.EventSystem.add_key_down_func(game.pygame.K_LEFT, move_cam_left)


SPEED_SHIP = 0.1
speed_ship = (0, 0, 0)

# SDAW

test_obj_0.init()
test_obj_0.move((3, 0, 0))
test_obj_0.recalc_pos()

game.Physics.add_object_to_map(test_obj_0)
for elem in [fighter1, fighter2, ast1, ast2, ast3, ast4, ast6, ast5, ast7, ast8, ast9]:
    rang = 120
    elem.init()
    elem.move((random.randint(-rang, rang) / 10, random.randint(-rang, rang) / 10, random.randint(-rang, rang) / 10))
    game.Physics.add_object_to_map(elem)

ast1.set_pos((1, 3, 0))

fighter1.rotate((random.randint(0, 360), random.randint(0, 360), random.randint(0, 360)))
fighter1.recalc_pos()
fighter2.rotate((random.randint(0, 360), random.randint(0, 360), random.randint(0, 360)))
fighter2.recalc_pos()


cam1 = game.Object.Camera(game)
cam1.init()
cam_pos = (-9, 0, 0)
cam_angles = (0, 0, 0)

cam1.set_pos(cam_pos)
cam1.set_rot(cam_angles)

game.Physics.add_object_to_map(cam1)

game.lib.print_map(game.map)
print()
game.lib.print_obj(test_obj_0.c_part)

def test_refresh(self):
    for elem in [ast1, ast2, ast3, ast4, ast5, ast6, ast7, ast8, ast9]:
        elem.rotate((0.5, 0.3, 0.2))
        elem.recalc_pos()

    # self.rotate((0.5, 0.3, 0.2))
    # cam.move((0.01, 0, 0))


test_obj_0.connect(test_refresh)

speed = 0.2
pressed_key = []
running = True
print(v_sum((0,0,0), (1, 2, 3)))
while running:
    cam1.render(600)
    print('')
    game.Physics.calc_collisions()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                cam_pos = v_sum(cam_pos, (0, 0, -speed * 1))
                print('up')
            elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                cam_pos = v_sum(cam_pos, (0, 0, speed * 1))
            elif event.key in (pygame.K_UP, pygame.K_w):
                # print(cam_pos, ((speed * cosd(cam_angles[2]) * 1), -speed * sind(cam_angles[2]), 0))
                cam_pos = v_sum(cam_pos, ((speed * cosd(cam_angles[2]) * 1), -speed * sind(cam_angles[2]), 0))
                # print(((1e-5*cosd(cam_angles[2])*d_t), 1e-5*sind(cam_angles[2])*d_t, 0), ((1e-5*cosd(cam_angles[2])*d_t)**2 + (1e-5*sind(cam_angles[2])*d_t)**2)**0.5 - 1e-5*d_t)
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                cam_pos = v_sum(cam_pos, (-(speed * cosd(cam_angles[2]) * 1), speed * sind(cam_angles[2]) * 1, 0))
            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                cam_pos = v_sum(cam_pos, ((speed * sind(cam_angles[2]) * 1), speed * cosd(cam_angles[2]) * 1, 0))
            elif event.key in (pygame.K_LEFT, pygame.K_a):
                cam_pos = v_sum(cam_pos, (-(speed * sind(cam_angles[2]) * 1), -speed * cosd(cam_angles[2]) * 1, 0))
            elif event.type == pygame.K_x:
                cam_pos = (0, 0, 0)
            pressed_key.append(event.key)
        elif event.type == pygame.KEYUP:
            del pressed_key[pressed_key.index(event.key)]

        elif event.type == pygame.MOUSEMOTION:
            if event.buttons == (1, 0, 0) or event.buttons == (0, 1, 0):
                # local_cam_angles = v_sum(local_cam_angles, (0, event.rel[1] / scale * dpi, -event.rel[0] / scale * dpi))
                # cam_angles = (sind(local_cam_angles[2])*local_cam_angles[1], cosd(local_cam_angles[2])*local_cam_angles[1], local_cam_angles[2])
                # print(cam_angles, local_cam_angles)
                print(cam_angles)
                cam_angles = (0, (cam_angles[1] + event.rel[1] * speed) % 360 * 0, (cam_angles[2] + -event.rel[0] * speed) % 360)

    for key in pressed_key: # Передвижение при удержании клавиши
        if key == pygame.K_SPACE:
            cam_pos = v_sum(cam_pos, (0, 0, -speed * 1))
        elif key == pygame.K_LSHIFT:
            cam_pos = v_sum(cam_pos, (0, 0, speed * 1))
        elif key in (pygame.K_UP, pygame.K_w):
            cam_pos = v_sum(cam_pos, ((speed * cosd(cam_angles[2]) * 1), -speed * sind(cam_angles[2]), 0))
            # print(((1e-5*cosd(cam_angles[2])*d_t), 1e-5*sind(cam_angles[2])*d_t, 0), ((1e-5*cosd(cam_angles[2])*d_t)**2 + (1e-5*sind(cam_angles[2])*d_t)**2)**0.5 - 1e-5*d_t)
        elif key in (pygame.K_DOWN, pygame.K_s):
            cam_pos = v_sum(cam_pos, (-(speed * cosd(cam_angles[2]) * 1), speed * sind(cam_angles[2]) * 1, 0))
        elif key in (pygame.K_RIGHT, pygame.K_d):
            cam_pos = v_sum(cam_pos, ((speed * sind(cam_angles[2]) * 1), speed * cosd(cam_angles[2]) * 1, 0))
        elif key in (pygame.K_LEFT, pygame.K_a):
            cam_pos = v_sum(cam_pos, (-(speed * sind(cam_angles[2]) * 1), -speed * cosd(cam_angles[2]) * 1, 0))
    cam1.set_pos(cam_pos)
    cam1.set_rot(cam_angles)
    # print('.')
    game.EventSystem.refresh()
