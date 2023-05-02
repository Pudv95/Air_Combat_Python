import math
import pygame
from pygame import mixer
import random
import os

global jet1_health
mixer.init() # mixer initialize

pygame.font.init()

pygame.display.set_caption("Space Wars")

# background

WIDTH, HEIGHT = 1100, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # generating window
bg_img = pygame.image.load(os.path.join("Atari_breakout","background.jpg") )# backgrounf image
bg_img = pygame.transform.scale(bg_img, (2000, 1000)) 
mixer.music.load(os.path.join("Atari_breakout","background_music.mp3"))
mixer.music.play()

#------
#initialing font style
text_font1 = pygame.font.SysFont("Arial" , 40)
text_font2 = pygame.font.SysFont("Gismo" , 60 ,bold = True)
# ------

#things on screen

JET1 = pygame.image.load(os.path.join("Atari_breakout","space_ship11.png")) # jet1_block image
JET2 = pygame.image.load(os.path.join("Atari_breakout","space_ship22.png")) # jet2_block image
bull_img1 = pygame.image.load(os.path.join("Atari_breakout","bullet _left_to_right.png")) # bullet1 image 
bull_img2 = pygame.image.load(os.path.join("Atari_breakout","bullet _left_to_right.png"))
BULLET1_img = pygame.transform.scale(bull_img1, (60, 60))
BULLET2 = pygame.transform.scale(bull_img2, (50, 50))
BULLET2_img = pygame.transform.rotate(BULLET2, 180) # final bullet2 image 

FPS = 60

# jet blocks
jet1_block = pygame.Rect(50, 300, 80, 102)
jet2_block = pygame.Rect(950, 300, 100, 102)
bullet1_block = pygame.Rect(-200 , -200 , 60 ,60)
# bullet1
# bullet1_X = -200
# bullet1_Y = -200
# bullet1_update_X = bullet1_X;
# bullet1_state = "ready"

bullet_list1 = []
bullet_list2 = []
# bullet_count = 0 
max_bull_num = 5
# Coordinates
# JET1X = 50
# JET1Y = 300
#
# JET2X = 950
# JET2Y = 300

# def draw_bullet(bulletX_cor):
jet1_health = 300
health1_color = (0,255,0)
jet2_health = 300
health2_color = (0,255,0)
max_health =  300

def fire_bullets(cord):
    global jet1_health
    global jet2_health

    #for bullet1 movement
    for item1 in bullet_list1:
        item1.x += 7
        if item1.x > 1090 or jet2_block.colliderect(item1):
            if jet2_block.colliderect(item1):
                if jet2_health > 0:
                    jet2_health -= 10
            bullet_list1.remove(item1)

    #for bullet2 movement
    for item2 in bullet_list2:
        item2.x -= 7
        if item2.x < 0 or jet1_block.colliderect(item2):
            if jet1_block.colliderect(item2):
                if jet1_health >0 :
                    jet1_health -= 10
            bullet_list2.remove(item2) 


def draw_window(jet1, jet2 , listb1 ,listb2 , health1 , health2 , hcolor1 , hcolor2 ,winstr ,ans):
    global max_health

    #drawing background image
    WIN.blit(bg_img, (0, 0))
    #----------------------------------------------------------------------------

    #generating and drawing Player name
    text1 = text_font1.render("Player1" , True ,(255 , 255 , 255))
    WIN.blit(text1, (10 , 2))
    
    text2 = text_font1.render("Player2" , True , (255 , 255 , 255)) 
    WIN.blit(text2 ,(970 , 2))
    #-----------------------------------------------------------------------------

    # bullet1_block = pygame.Rect(bullet1_cord_X , bullet1_cord_Y , 60 ,60)

    #drawing and firing bullets
    for itemb1 in listb1:
       WIN.blit(BULLET1_img , (itemb1.x+ 20 , itemb1.y + 20))
    for itemb2 in listb2:
        WIN.blit(BULLET2_img ,(itemb2.x ,itemb2.y + 20))
    #------------------------------------------------------------------------------

    #drawing jets
    WIN.blit(JET1, (jet1.x, jet1.y))
    WIN.blit(JET2, (jet2.x, jet2.y))
    #------------------------------------------------------------------------------

    # drawing and managing health bars
    #Player1

    pygame.draw.rect(WIN , hcolor1 , (10 , 45 , health1 , 20),border_radius = 5)
    pygame.draw.rect(WIN , (255 , 255 , 255) , (10 , 45 , max_health , 20) , 4 , 5)

    #Player2
    pygame.draw.rect(WIN , hcolor2 , (790 , 45 , health2 ,20) ,border_radius = 5)
    pygame.draw.rect(WIN , (255, 255 , 255) , (790 , 45 , max_health , 20) , 4 , 5)
    #-------------------------------------------------------------------------------
    if ans == True:
        winText = text_font2.render(winstr , True ,(255,255,255))
        WIN.blit(winText ,(400 ,350))
    # updating display
    pygame.display.update()
    #-------------------------------------------------------------------------------

def main():
    
    global bullet1_state
    global bullet1_X
    global bullet1_Y
    global health1_color
    global health2_color
    global bullet_list1
    global bullet_list2
    answer = False
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(bullet_list1) < max_bull_num:
                    bullet1_state = "fire"
                    # bullet1_state = "fire"
                    bullet1_X = jet1_block.x
                    bullet1_Y = jet1_block.y
                    bullet1_block = pygame.Rect(bullet1_X , bullet1_Y , 40 , 40)
                    bullet_list1.append(bullet1_block)
                if event.key == pygame.K_RCTRL and len(bullet_list2) < max_bull_num:
                    bullet2_X = jet2_block.x
                    bullet2_Y = jet2_block.y
                    bullet2_block = pygame.Rect(bullet2_X , bullet2_Y , 40 , 40)
                    bullet_list2.append(bullet2_block)
        
        # if bullet1_state == "fire":
        #     bullet1_X += 7
        #     bullet1_block.x = bullet1_X
        #     bullet1_block.y = bullet1_Y

            
            # if bullet1_X > 1090 or bullet1_block.colliderect(jet2_block):
            #     bullet1_block.x = jet1_block.x
            #     bullet1_X = -200
            #     bullet1_Y = -200
            #     bullet1_state = "ready"
            
        # operating keyboard keys
        key_pressed = pygame.key.get_pressed()

        # for JET1
        if key_pressed[pygame.K_w]:
            if jet1_block.y <= 50:
                pass
            else:
                jet1_block.y -= 5
        if key_pressed[pygame.K_s]:
            if jet1_block.y >= 600:
                pass
            else:
                jet1_block.y += 5
        if key_pressed[pygame.K_a]:
            if jet1_block.x <= 10:
                pass
            else:
                jet1_block.x -= 5
        if key_pressed[pygame.K_d]:
            if jet1_block.x >= 450:
                pass
            else:
                jet1_block.x += 5

        # for JET 2
        if key_pressed[pygame.K_UP]:
            if jet2_block.y <= 50:
                pass
            else:
                jet2_block.y -= 5
        if key_pressed[pygame.K_DOWN]:
            if jet2_block.y >= 600:
                pass
            else:
                jet2_block.y += 5
        if key_pressed[pygame.K_LEFT]:
            if jet2_block.x <= 550:
                pass
            else:
                jet2_block.x -= 5
        if key_pressed[pygame.K_RIGHT]:
            if jet2_block.x >= 990:
                pass
            else:
                jet2_block.x += 5
        
        # if key_pressed[pygame.K_LCTRL]:
        #     bullet1_state = "fire"
        #     bullet1_X = jet1_block.x
        #     bullet1_Y = jet1_block.y
        #     bullet1_block = pygame.Rect(bullet1_X , bullet1_Y , 60 ,60)
        #     bullet_list1.append(bullet1_block)

            # draw_bullet(jet1_block)
        # print(bullet_list1)

        # health bar color change

        if jet1_health <= 100 :
            health1_color = (255,0,0)
        if jet2_health <= 100:
            health2_color = (255,0,0)
        
        #winner

        winner_text =""
        if jet1_health == 0 and jet2_health == 0:
            winner_text = "BOTH Player WINS"
            answer = True
            bullet_list1 = []
            # run = False
        elif jet1_health == 0:
            winner_text = "Player2 WINS!"
            answer = True
            bullet_list1 = []
            bullet_list2 = []
            # run = False
        elif jet2_health == 0:
            winner_text = "Player1 WINS!"
            answer = True
            # run = False

        #bullet firing
        fire_bullets(bullet_list1)

        #window and other components generating
        draw_window(jet1_block, jet2_block , bullet_list1 ,bullet_list2 , jet1_health , jet2_health ,health1_color , health2_color ,winner_text ,answer)

    pygame.quit()


if __name__ == "__main__":
    main()
