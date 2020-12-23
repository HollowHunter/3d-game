import pygame
from random import randrange
from math import ceil




class Ball:
    def __init__(self):
        self.color = (randrange(255), randrange(255), randrange(255))
        self.x = randrange(widht)
        self.y = randrange(height)

    def fly(self, step):
        self.y -= step
        if self.y < -60:
            self.y = height + 30
        elif  self.y > height + 30:
            self.y = -30
        pygame.draw.circle(screen, self.color, (self.x, self.y),  30)


class Btn_group:
    def __init__(self, btn_list):
        self.btn_list = btn_list
        self.is_move = False

    def on_btns(self, number=0):
        for elem in self.btn_list:
            elem.time = 0
            elem.set_points(number)
        self.is_move = True

    def move_btns(self):
        if self.is_move:
            is_ready = []
            for elem in self.btn_list:
                is_ready.append(elem.run())
            if all(is_ready):
                self.is_move = False
        else:
            for elem in self.btn_list:
                elem.draw_btn()

    def get_button(self, pos, is_hold=None):
        for elem in self.btn_list:
            if is_hold != None:
                elem.is_hold = is_hold
            a = elem.is_me(pos)

            if a != None:
                return self.btn_list.index(a)




class Smart_button:
    interpolate = lambda now, end, k: (end - now) * k
    def __init__(self, list_of_points, text='кнопка', speed=0.2, color=(pygame.Color('orange')), delay=0):
        self.text = text
        self.list_of_points = list_of_points
        self.now_start_pos = list_of_points[0][0]
        self.now_end_pos = list_of_points[0][1]
        self.k = speed
        self.color = color
        self.now_pos = list_of_points[0][0]
        self.DELAY = delay
        self.time = 0
        self.x_size = 250
        self.y_size = 50
        self.is_hold = False

        self.SCALE_X = 40
        self.SCALE_Y = 0
        self.deltax = 0
        self.deltay = 0
        self.delta_x_size = 0
        self.delta_y_size = 0
        self.font_size = 30
        self.is_scale = False


    def run(self):
        self.is_scale = False
        if self.time >= self.DELAY and not self.is_scale:
            step_x = Smart_button.interpolate(self.now_pos[0], self.now_end_pos[0], self.k)
            step_y = Smart_button.interpolate(self.now_pos[1], self.now_end_pos[1], self.k)
            if abs(step_x) < 0.05 and abs(step_y) < 0.05:
                self.draw_btn(False)
                self.is_first_step = True
                return True
            self.now_pos[0] += step_x
            self.now_pos[1] += step_y
        self.draw_btn(False)
        self.is_first_step = False
        self.time += 1
        return False

    def draw_btn(self, is_not_moving=True):
        # зум при наведении
        if self.is_scale and is_not_moving:
            if self.now_pos[0] + self.deltax >= self.now_pos[0] - self.SCALE_X:
                self.deltax -= 5
                self.delta_x_size += 10
                self.font_size += 1
                print(1)
            if self.now_pos[1] + self.deltay >= self.now_pos[1] - self.SCALE_Y:
                self.deltay -= 1
                self.delta_y_size += 2
        elif is_not_moving:
            if self.now_pos[0] + self.deltax <= self.now_pos[0]:
                self.deltax += 5
                self.delta_x_size -= 10
                self.font_size -= 1
            if self.now_pos[1] + self.deltay <= self.now_pos[1]:
                self.deltay += 1
                self.delta_y_size -= 2

        x = self.now_pos[0] + self.deltax
        y = self.now_pos[1] + self.deltay
        x_size, y_size = self.x_size + self.delta_x_size, self.y_size + self.delta_y_size,
        tl = (y_size + x, 0 + y)  # top left
        tr = (x_size + x, 0 + y)  # top right
        dr = (x_size - y_size + x, y_size + y)  # down right
        dl = (0 + x, y_size + y)  # down left

        pygame.draw.polygon(screen, self.color, [tl, tr, dr, dl])
        Smart_button.polygon_with_widht((255, 230, 80), [tl, tr, dr, dl], 3)  # отрисовка полигона с толщиой

        font = pygame.font.Font(None, self.font_size)
        text = font.render(self.text, True, (255, 255,255))
        text_x = (x + x_size // 2) - text.get_width() // 2
        text_y = (y + y_size // 2) - text.get_height() // 2
        screen.blit(text, (text_x, text_y))

    def polygon_with_widht(color, points, widht):
        for i in range(0, len(points) - 1):
            pygame.draw.line(screen, color, points[i], points[i + 1], widht)
        pygame.draw.line(screen, color, points[00], points[-1], widht)

    def set_points(self, number):
        self.now_start_pos = self.list_of_points[number][0]
        self.now_end_pos = self.list_of_points[number][1]

    def is_me(self, pos):
        mx, my = pos[0], pos[1]  # mouse_x, mouse_y
        x, y = self.now_pos[0], self.now_pos[1]
        if 0 < mx - x < self.x_size and 0 < my - y < self.y_size and screen.get_at(pos) == self.color or \
                self.y_size < mx - x < self.x_size - self.y_size and 0 < my - y < self.y_size:

            # if not self.is_scale:
            #     self.deltax, self.deltay = self.deltax - self.SCALE_X // 2,  self.deltay - self.SCALE_Y // 2
            #     self.delta_x_size += self.SCALE_X
            #     self.delta_y_size += self.SCALE_Y
            #     self.font_size += 10
            self.is_scale = True

            if self.is_hold:
                self.color = (255, 230, 0)
            else:
                self.color = pygame.Color('orange')
            self.draw_btn()
            return self
        else:
            # if self.is_scale:
            #     self.deltax, self.deltay = self.deltax + self.SCALE_X // 2, self.deltay + self.SCALE_Y // 2
            #     self.delta_x_size -= self.SCALE_X
            #     self.delta_y_size -= self.SCALE_Y
            #     self.font_size -= 10
            self.is_scale = False
        return None








fps = 60
pygame.init()
size = widht, height = 600, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Менюха')

clock = pygame.time.Clock()

is_clicked = False
running = True

buttons = Btn_group([Smart_button((([700, 200], [175, 200]), ([175, 200], [700, 200])), text='Вверх', delay=0),
                     Smart_button((([700, 270], [175, 270]), ([175, 270], [700, 270])), text='Стоп', delay=5),
                     Smart_button((([700, 340], [175, 340]), ([175, 340], [700, 340])), text='Вниз', delay=10),
                     Smart_button((([700, 410], [175, 410]), ([175, 410], [700, 410])), text='Выйти из игры', delay=15)])
balls = [Ball() for _ in range(100)]
step = 2
is_move_btn = False
number = 1
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                number += 1
                number %= 2
                buttons.on_btns(number)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # if event.button == 4:
            #     buttons.on_btns()
            # elif event.button == 5:
            #     buttons.on_btns(1)
            if event.button == 1:
                result = buttons.get_button(event.pos, True)
                if result == 0:
                    step = 2
                elif result == 1:
                    step = 0
                elif result == 2:
                    step = -2
                elif result == 3:
                    running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                print(buttons.get_button(event.pos, False))
        elif event.type == pygame.MOUSEMOTION:
            buttons.get_button(event.pos)

    for elem in balls:
        elem.fly(step)
    buttons.move_btns()

    clock.tick(fps)
    pygame.display.flip()
pygame.quit()