#!/usr/bin/python
# -*- coding: utf-8 -*-

DIRECTIONS = ('N', 'NE', "E", "SE", "S", "SW", "W", "NW")


def check(matrix, win_val):

    N = len(matrix)

    for row in range(N):
        for col in range(N):
            if matrix[row][col] != 0:
                for direction in DIRECTIONS:
                    if __check_direction(matrix, row, col, direction, 1) >= win_val:
                        return True
    
    return False

def __check_direction(matrix, row, col, direction, length):

    new_pos = __get_new_pos(col, row, direction)
    try:
        if matrix[row][col] == matrix[new_pos[1]][new_pos[0]]:
            return __check_direction(matrix, new_pos[1], new_pos[0], direction, length+1)
    except IndexError:
        pass
    
    return length



def __get_new_pos(x, y, direction):
    if direction == 'N':
        return (x, y-1)
    elif direction == 'NE':
        return (x+1, y-1)
    elif direction == 'E':
        return (x+1, y)
    elif direction == 'SE':
        return (x+1, y+1)
    elif direction == 'S':
        return (x, y+1)
    elif direction == 'SW':
        return (x-1, y+1)
    elif direction == 'W':
        return (x-1, y)
    elif direction == 'NW':
        return (x-1, y-1)
