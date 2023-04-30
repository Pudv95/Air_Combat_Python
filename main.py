import math
import pygame
from pygame import mixer
import random

mixer.init()

pygame.display.set_caption("Space Wars")

# background

WIDTH, HEIGHT = 1100, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
bg_img = pygame.image.load("background.jpg")
bg_img = pygame.transform.scale(bg_img, (2000, 1000))
mixer.music.load("background_music.mp3")
mixer.music.play()

# things on the screen

JET1 = pygame.image.load("space_ship11.png")
JET2 = pygame.image.load("space_ship22.png")
BULLET1 = pygame.image.load("bullet _left_to_right.png")
BULLET2 = pygame.image.load("bullet _left_to_right.png")
BULLET1 = pygame.transform.scale(BULLET1, (50, 50))
BULLET2 = pygame.transform.scale(BULLET2, (50, 50))
BULLET2 = pygame.transform.rotate(BULLET2, 180)

FPS = 60


# Coordinates
# JET1X = 50
# JET1Y = 300
#
# JET2X = 950
# JET2Y = 300


def draw_window(jet1, jet2):
    WIN.blit(bg_img, (0, 0))
    WIN.blit(JET1, (jet1.x, jet1.y))
    WIN.blit(JET2, (jet2.x, jet2.y))
    pygame.display.update()


def main():
    jet1 = pygame.Rect(50, 300, 100, 102)
    jet2 = pygame.Rect(950, 300, 100, 102)

    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL:
                    WIN.blit(BULLET1, (jet1.x+25, jet1.y+25))

        key_pressed = pygame.key.get_pressed()

        # JET1
        if key_pressed[pygame.K_w]:
            if jet1.y <= 0:
                pass
            else:
                jet1.y -= 5
        if key_pressed[pygame.K_s]:
            if jet1.y >= 600:
                pass
            else:
                jet1.y += 5
        if key_pressed[pygame.K_a]:
            if jet1.x <= 10:
                pass
            else:
                jet1.x -= 5
        if key_pressed[pygame.K_d]:
            if jet1.x >= 450:
                pass
            else:
                jet1.x += 5

        # JET 2
        if key_pressed[pygame.K_UP]:
            if jet2.y <= 0:
                pass
            else:
                jet2.y -= 5
        if key_pressed[pygame.K_DOWN]:
            if jet2.y >= 600:
                pass
            else:
                jet2.y += 5
        if key_pressed[pygame.K_LEFT]:
            if jet2.x <= 550:
                pass
            else:
                jet2.x -= 5
        if key_pressed[pygame.K_RIGHT]:
            if jet2.x >= 990:
                pass
            else:
                jet2.x += 5

        draw_window(jet1, jet2)

    pygame.quit()


if __name__ == "__main__":
    main()
