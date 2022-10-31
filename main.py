import pygame
import random
import config

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption(config.SCREEN_CAPTURE)

clock = pygame.time.Clock()
running = True

points = {}
amount_of_points = 5

for i in range(amount_of_points):
    points[random.randint(0, config.SCREEN_WIDTH)] = random.randint(0, config.SCREEN_HEIGHT)

print(points)

for point in points:
    print(point)
    print(points[point])
    print(00000)


while running:
    clock.tick(config.FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(config.WHITE)
    for point in points:
        present_point = (point, points[point])
        last_point = 0
        screen.set_at(present_point, config.RED)

    pygame.display.flip()

pygame.quit()