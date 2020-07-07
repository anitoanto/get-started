import pygame
import random
import sys
from pygame.locals import *

grid_max = 600
grid_size = 20


def gameover(window, x, y, score, pdir, fpos):
    gm_msg = pygame.font.SysFont('Arial', 32).render(
        "GAME OVER", True, (255, 0, 0))
    window.blit(gm_msg, (10, grid_max - 50))
    pygame.display.update()
    pygame.time.wait(2000)
    x = [grid_max / 2, grid_max / 2, grid_max / 2]
    y = [(grid_max / 2) - grid_size, grid_max / 2, (grid_max / 2) + grid_size]
    fpos = (random.randint(0, (grid_max / grid_size) - 1) * grid_size,
            random.randint(0, (grid_max / grid_size) - 1) * grid_size)
    score = 0
    pdir = 1
    return x, y, score, pdir, fpos


def main():
    x = [grid_max / 2, grid_max / 2, grid_max / 2]
    y = [(grid_max / 2) - grid_size, grid_max / 2, (grid_max / 2) + grid_size]
    score = 0
    pdir = 1
    pygame.init()
    window = pygame.display.set_mode((grid_max, grid_max))
    pygame.display.set_caption("snakegame")

    food = pygame.Surface((grid_size, grid_size))
    food.fill((255, 0, 0))
    fpos = (random.randint(0, (grid_max / grid_size) - 1) * grid_size,
            random.randint(0, (grid_max / grid_size) - 1) * grid_size)

    snk_head = pygame.Surface((grid_size, grid_size))
    snk_head.fill((255, 255, 255))
    snk = pygame.Surface((grid_size, grid_size))
    snk.fill((200, 200, 200))

    clock_signal = pygame.time.Clock()
    while True:
        clock_signal.tick(12)
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit(0)
            elif e.type == KEYDOWN:
                if e.key == K_UP and pdir != 3:
                    pdir = 1
                elif e.key == K_DOWN and pdir != 1:
                    pdir = 3
                elif e.key == K_LEFT and pdir != 2:
                    pdir = 4
                elif e.key == K_RIGHT and pdir != 4:
                    pdir = 2

        x.pop(len(x) - 1)
        x.insert(0, x[0])
        y.pop(len(y) - 1)
        y.insert(0, y[0])

        if pdir == 1:
            y[0] -= grid_size
        elif pdir == 2:
            x[0] += grid_size
        elif pdir == 3:
            y[0] += grid_size
        else:
            x[0] -= grid_size

        if x[0] == fpos[0] and y[0] == fpos[1]:
            x.append(x[len(x) - 1])
            y.append(y[len(y) - 1])
            score += 1
            fpos = (random.randint(0, (grid_max / grid_size) - 1) * grid_size,
                    random.randint(0, (grid_max / grid_size) - 1) * grid_size)

        for i in range(1, len(x)):
            if x[i] == x[0] and y[i] == y[0]:
                x, y, score, pdir, fpos = gameover(
                    window, x, y, score, pdir, fpos)
                break

        if x[0] < -grid_size / 2 or x[0] > grid_max - grid_size / 2 or y[0] < -grid_size / 2 or y[0] > grid_max - grid_size / 2:
            x, y, score, pdir, fpos = gameover(window, x, y, score, pdir, fpos)
        window.fill((30, 30, 30))
        window.blit(snk_head, (x[0], y[0]))
        for i in range(1, len(x)):
            window.blit(snk, (x[i], y[i]))
        window.blit(food, fpos)
        score_dis = pygame.font.SysFont('Arial', 48).render(
            str(score), True, (255, 255, 0))
        window.blit(score_dis, (20, 20))

        pygame.display.update()


if __name__ == '__main__':
    main()
