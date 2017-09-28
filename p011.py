"""Largest product in a grid"""
import itertools
from core import product


def create_grid():
    with open('data_p011') as f:
        dat = f.read().strip().split('\n')
    dat = [[int(x) for x in ls.split(' ')] for ls in dat]
    grid = dat
    leny = len(grid)
    lenx = len(grid[0])
    return {'lenx': lenx, 'leny': leny, 'grid': grid}


def right_diagonals(grid, length=4):
    xmax = grid['lenx'] - length
    ymax = grid['leny'] - length
    grid = grid['grid']
    return ((grid[j + n][i + n] for n in range(length))
            for i, j in itertools.product(range(xmax), range(ymax)))


def left_diagonals(grid, length=4):
    grid['grid'] = [list(reversed(line)) for line in grid['grid']]
    return right_diagonals(grid, length)


def verticals(grid, length=4):
    xmax = grid['lenx']
    ymax = grid['leny'] - length
    grid = grid['grid']
    return ((grid[j + n][i] for n in range(length))
            for i, j in itertools.product(range(xmax), range(ymax)))


def horizontals(grid, length=4):
    xmax = grid['lenx'] - length
    ymax = grid['leny']
    grid = grid['grid']
    return ((grid[j][i + n] for n in range(length))
            for i, j in itertools.product(range(xmax), range(ymax)))


grid = create_grid()

vp = max(product(ls) for ls in verticals(grid))
hp = max(product(ls) for ls in horizontals(grid))
rdp = max(product(ls) for ls in right_diagonals(grid))
ldp = max(product(ls) for ls in left_diagonals(grid))
print(vp, hp, rdp, ldp)
