import pygame
import random

size = width, height = 400, 300
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

running = True
drawing = False
x1 = 0
y1 = 0
y2 = 0
r, g, b = (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))
list_color = []
list_coords = []
#screen2 = pygame.Surface(screen.get_size())

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x1, y1 = event.pos
            list_coords.append((x1, y1))
            r, g, b = (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))
            list_color.append((r, g, b))
            drawing = True

    #screen.blit(screen2, (0, 0))

    if drawing:
        screen.fill((0, 0, 0))
        for i in range(0, len(list_coords)):
            y = list_coords[i][1]
            if list_coords[i][1] < 290:
                y += 1
                list_coords[i] = (list_coords[i][0], int(y))

            pygame.draw.circle(screen, (list_color[i]), (list_coords[i]), 10)
            #screen2.blit(screen, (0, 0))
        pygame.display.flip()
        clock.tick(100)

pygame.quit()
