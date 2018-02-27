#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint

class snakeLib:

    field = None
    field_dimension = 30

    snake = None
    snake_direction = 'R'
    snake_alive = True

    apples = []

    def __init__(self):
        self.field = [[0] * int(self.field_dimension) for i in range(int(self.field_dimension))]

        self.field[15][14] = 'S'
        self.field[15][15] = 'S'
        self.field[15][16] = 'S'

        self.snake = [(15, 14), (15, 15), (15, 16)]

    def move(self, direction = None):
        # direction  U - up
        #            D - down
        #            L - left
        #            R - right
        #         None - same direction

        if direction is None:
                direction = self.snake_direction
        
        if self.snake_alive:
            if self.__direction_is_valid(direction):
                new_pos = self.__calc_head_new_pos(direction)
                if self.__next_position_valid(new_pos):
                    self.__step_with(new_pos, direction)
                else:
                    self.snake_alive = False
    
    def get_field(self):
        return self.field
    
    def get_snake_head(self):
        return self.snake[-1]

    def get_snake_length(self):
        return len(self.snake)

    def random_apple(self):
        apple_pos = self.__generate_new_apple_pos()
        self.apples.append(tuple(apple_pos))
        self.field[apple_pos[0]][apple_pos[1]] = "A"

    def remove_old_apple(self):
        old_apple = self.apples.pop(0)
        self.field[old_apple[0]][old_apple[1]] = 0

    def get_apples_number(self):
        return len(self.apples)

    def is_alive(self):
        return self.snake_alive

    def __direction_is_valid(self, direction):
        if direction == "U" and self.snake_direction == "D":
            return False
        elif direction == "D" and self.snake_direction == "U":
            return False
        elif direction == "L" and self.snake_direction == "R":
            return False
        elif direction == "R" and self.snake_direction == "L":
            return False

        return True

    def __calc_head_new_pos(self, direction):

        new_pos = [0, 0]

        if direction == "U":
            new_pos[0] -= 1
        elif direction == "D":
            new_pos[0] += 1
        elif direction == "L":
            new_pos[1] -= 1
        elif direction == "R":
            new_pos[1] += 1

        return new_pos

    def __next_position_valid(self, new):
        next_pos = list(self.snake[-1])
        next_pos[0] += new[0]
        next_pos[1] += new[1]

        return next_pos[0] >= 0 and next_pos[0] < self.field_dimension and next_pos[1] >= 0 and next_pos[1] < self.field_dimension
           
    def __step_with(self, pos, direction):
        
        next_pos = list(self.snake[-1])
        next_pos[0] += pos[0]
        next_pos[1] += pos[1]

        if not self.__position_is_snake(next_pos):
            self.snake.append(tuple(next_pos))
            self.snake_direction = direction

            if self.__position_is_apple(next_pos):
                self.apples.remove(tuple(next_pos))
            else:
                self.__remove_snake_from(self.snake.pop(0))

            self.__appear_snake_at(next_pos)

        else:
            self.snake_alive = False

    def __position_is_snake(self, position):
        return self.field[position[0]][position[1]] == "S"
    
    def __position_is_apple(self, position):
        return self.field[position[0]][position[1]] == "A"
    
    def __position_is_clear(self, position):
        return self.field[position[0]][position[1]] == 0

    def __remove_snake_from(self, position):
        self.field[position[0]][position[1]] = 0

    def __appear_snake_at(self, position):
        self.field[position[0]][position[1]] = "S"

    def __generate_new_apple_pos(self):

        position_is_good = False
        pos = []

        while not position_is_good:
            row = randint(0,self.field_dimension-1)
            col = randint(0,self.field_dimension-1)

            pos = [row, col]
            position_is_good = self.__position_is_clear(pos)

        return pos
