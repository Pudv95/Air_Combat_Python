import pygame
from pygame import mixer
import random

mixer.init()

pygame.font.init()

pygame.display.set_caption("Space Wars")


WIDTH, HEIGHT = 1100, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  
bg_img = pygame.image.load("background.png")  
bg_img = pygame.transform.scale(bg_img, (2000, 1000))
mixer.music.load("background_music.mp3")
mixer.music.play()

text_font1 = pygame.font.SysFont("imprintshadow", 30)
text_font2 = pygame.font.SysFont("imprintshadow", 60, bold=True)


JET1 = pygame.image.load("space_ship11.png")
JET2 = pygame.image.load("space_ship22.png")  

FPS = 60

jet1_block = pygame.Rect(50, 300, 80, 80)
jet2_block = pygame.Rect(950, 300, 80, 80)

jet_speed1 = 5
jet_speed2 = 5

def draw_window(jet1, jet2):

    WIN.blit(bg_img, (0, 0))

    WIN.blit(JET1, (jet1.x, jet1.y))
    WIN.blit(JET2, (jet2.x, jet2.y))

    pygame.display.update()
    # -------------------------------------------------------------------------------


def main():

    inside, previous = 0, 0
    answer = False
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)

        key_pressed = pygame.key.get_pressed()

        # for JET1
        if key_pressed[pygame.K_w]:
            if jet1_block.y <= 90:
                pass
            else:
                jet1_block.y -= jet_speed1
        if key_pressed[pygame.K_s]:
            if jet1_block.y >= 600:
                pass
            else:
                jet1_block.y += jet_speed1
        if key_pressed[pygame.K_a]:
            if jet1_block.x <= 10:
                pass
            else:
                jet1_block.x -= jet_speed1
        if key_pressed[pygame.K_d]:
            if jet1_block.x >= 450:
                pass
            else:
                jet1_block.x += jet_speed1

        # for JET 2
        if key_pressed[pygame.K_UP]:
            if jet2_block.y <= 90:
                pass
            else:
                jet2_block.y -= jet_speed2
        if key_pressed[pygame.K_DOWN]:
            if jet2_block.y >= 600:
                pass
            else:
                jet2_block.y += jet_speed2
        if key_pressed[pygame.K_LEFT]:
            if jet2_block.x <= 550:
                pass
            else:
                jet2_block.x -= jet_speed2
        if key_pressed[pygame.K_RIGHT]:
            if jet2_block.x >= 990:
                pass
            else:
                jet2_block.x += jet_speed2

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        winner_text = ""
        reload_text = ""


        if key_pressed[pygame.K_ESCAPE]:
                run = False

        draw_window(jet1_block, jet2_block)

    pygame.quit()


if __name__ == "__main__":
    main()
