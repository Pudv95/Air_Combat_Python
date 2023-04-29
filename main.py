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
BULLET = pygame.image.load("bullet _left_to_right.png")


FPS = 60

# for generating display
def draw_window():
    WIN.blit(bg_img, (0, 0))
    WIN.blit(JET1, (50, 300))
    WIN.blit(JET2, (950, 300))
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()
