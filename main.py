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
POWER_BOOST = pygame.image.load("Power_Doubler.png")
POWER_BOOST = pygame.transform.scale(POWER_BOOST, (50, 50))

FPS = 60


# for generating display
def draw_window(jet1, jet2, power):
    WIN.blit(bg_img, (0, 0))
    WIN.blit(POWER_BOOST, (power.x, power.y))
    WIN.blit(JET1, (jet1.x, jet1.y))
    WIN.blit(JET2, (jet2.x, jet2.y))
    pygame.display.update()


# powerups time
previous = 0
inside = 0


def main():
    global previous
    global inside

    jet1 = pygame.Rect(50, 300, 100, 102)
    jet2 = pygame.Rect(950, 300, 100, 102)
    power = pygame.Rect(-100, -100, 20, 20)

    run = True
    clock = pygame.time.Clock()
    while run:

        clock.tick(FPS)
        current_time = pygame.time.get_ticks()
        if current_time - previous > 15000:
            power.x = random.randint(10, 990)
            power.y = random.randint(10, 600)
            previous = current_time
        if power.x != -100:
            inside += 1
        if inside > 180:
            power.x = -100
            power.y = -100
            inside = 0
        if jet1.colliderect(power) or jet2.colliderect(power):
            power.x = -100
            power.y = -100
            inside = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL:
                    WIN.blit(BULLET1, (jet1.x + 25, jet1.y + 25))

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

        draw_window(jet1, jet2, power)

    pygame.quit()


if __name__ == "__main__":
    main()
