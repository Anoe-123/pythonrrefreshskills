import pygame
import time

pygame.init()

screen = pygame.display.set_mode((200, 400))
pygame.display.set_caption("Traffic Light")

def change_light(light):
    return light + 1

light = 0

while True:

    red = (80, 0, 0)
    amber = (80, 80, 0)
    green = (0, 80, 0)

    if light == 0:
        print("RED")
        red = (255, 0, 0)

    elif light == 1:
        print("RED + AMBER")
        red = (255, 0, 0)
        amber = (255, 191, 0)

    elif light == 2:
        print("GREEN")
        green = (0, 255, 0)

    else:
        print("AMBER")
        amber = (255, 191, 0)
        light = -1

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (100, 100, 100), (50, 25, 100, 300))

    pygame.draw.circle(screen, red, (100, 75), 30)
    pygame.draw.circle(screen, amber, (100, 175), 30)
    pygame.draw.circle(screen, green, (100, 275), 30)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    time.sleep(3)

    light = change_light(light)
