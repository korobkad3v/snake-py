import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
import sys
from core.field import Field

class Snake:
    def __init__(self, name: str) -> None:
        self.name = name
        self.direction = KEY_RIGHT

        self.coords = [[0, 0], [0, 1], [0, 2], [0, 3]]


    def set_direction(self, ch):

        if ch == KEY_LEFT and self.direction == KEY_RIGHT:
            return
        if ch == KEY_RIGHT and self.direction == KEY_LEFT:
            return
        if ch == KEY_UP and self.direction == KEY_DOWN:
            return
        if ch == KEY_DOWN and self.direction == KEY_UP:
            return

        self.direction = ch

    def level_up(self):
        a = self.coords[0]
        b = self.coords[1]

        tail = a[:]

        if a[0] < b[0]:
            tail[0]-=1
        elif a[1] < b[1]:
            tail[1]-=1
        elif a[0] > b[0]:
            tail[0]+=1
        elif a[1] > b[1]:
            tail[1]+=1

        tail = self._check_limit(tail)
        self.coords.insert(0, tail)

    def is_alive(self):
        head = self.coords[-1]
        snake_body = self.coords[:-1]
        return head not in snake_body

    def _check_limit(self, point ):
        if point[0] > self.field.height-1:
            point[0] = 0
        elif point[0] < 0:
            point[0] = self.field.height-1
        elif point[1] < 0:
            point[1] = self.field.width-1
        elif point[1] > self.field.width-1:
            point[1] = 0

        return point
    
    def move(self):

        head = self.coords[-1][:]

        if self.direction == KEY_UP:
            head[0]-=1
        elif self.direction == KEY_DOWN:
            head[0]+=1
        elif self.direction ==KEY_RIGHT:
            head[1]+=1
        elif self.direction == KEY_LEFT:
            head[1]-=1

        head = self._check_limit(head)

        del(self.coords[0])
        self.coords.append(head)
        self.field.snake_coords = self.coords

        if not self.is_alive():
            sys.exit()

        if self.field.is_snake_eat_egg():
            curses.beep()
            self.level_up()
            self.field.add_egg()




    def set_field(self, field: Field):
        self.field = field