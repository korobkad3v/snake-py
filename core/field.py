from typing import Dict, List, Any
from core.egg import Egg
import random as r

class Field:
    def __init__(self, width: int, height: int, char_table: Dict[str, Any], egg: Egg) -> None:
        self.width = width
        self.height = height
        self.char_table = char_table
        self.egg = egg


        self.snake_coords = []
        self._generate_field()
        self.add_egg()

    def _generate_field(self) -> None:
        self.field = [[ "f" for j in range(self.width)] for i in range(self.height)]

    def _clear_field(self) -> None:        
        self.field = [[j if j!= "s" and j!= "h" else "f" for j in i] for i in self.field]

    def add_egg(self) -> None:
        while(True):
            egg = Egg(coords=(r.randint(0, self.height-1), r.randint(0, self.width - 1)))

            if egg.coords not in self.snake_coords:
                self.egg = egg
                self.field[egg.coords[0]][egg.coords[1]] = "e"
                break

    def get_egg_pos(self) -> List[int]:
        for i in range(self.height):
            for j in range(self.width):
                if i == self.egg.coords[0] and j == self.egg.coords[1]:
                    return [i, j]
                
        return [-1, -1]
    
    def is_snake_eat_egg(self) -> bool:
        egg_pos = self.get_egg_pos()
        head = self.snake_coords[-1]
        return egg_pos == head
    
    def render(self, screen) -> None:
        self._clear_field()

        for i, j in self.snake_coords:
            self.field[i][j] = "s"

        head = self.snake_coords[-1]
        self.field[head[0]][head[1]] = "h"

        for i in range(self.height): 
            row = ''
            for j in range(self.width):  
                element = self.field[i][j]
                row += self.char_table.get(element, ' ') 

            screen.addstr(i, 0, row)