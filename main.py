import numpy as np
from scipy import signal
import pygame as pg

def seed_board(grid_size, chance_of_death):
    return np.random.choice(np.append(np.zeros(chance_of_death), 1), size=(grid_size, grid_size))


def game_of_life_tick(board):
    filter = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ])

    neighbours = signal.convolve2d(board, filter, 'same')
    return np.where(
        ((neighbours == 2) | (neighbours == 3) & (board == 1)) |
        ((neighbours == 2) & (board == 0)),
        1, 0)


def initialise_graphics(grid_size):
    pg.init()
    pg.mouse.set_visible(False)
    screen = pg.display.set_mode(
        [grid_size, grid_size])

    return screen


def render_grid(screen, board, live_cell_colour):
    for y in range(0, len(board[0])):
        for x in range(0, len(board)):
            if board[x][y]:
                screen.set_at((x, y), live_cell_colour)


grid_size = 400
chance_of_death = (grid_size * 2) - 100
live_cell_colour = [32, 32, 42]
dead_cell_colour = [255, 255, 255]
target_fps = 60

board = seed_board(grid_size, chance_of_death)

clock = pg.time.Clock()
screen = initialise_graphics(grid_size)
window_title_prefix = 'Total population size:'
done = False
while not done:

    pg.display.set_caption(
        f'{window_title_prefix} {np.count_nonzero(board)}'.ljust(60))
    pg.display.update()
    for e in pg.event.get():
        if e.type == pg.QUIT or (e.type == pg.KEYUP and e.key == pg.K_ESCAPE):
            done = True
            break

    screen.fill(live_cell_colour)
    render_grid(screen, board, dead_cell_colour)
    board = game_of_life_tick(board)
    clock.tick(target_fps)
