import pygame
from pygame import mixer
import random

mixer.init()  # mixer initialize

pygame.font.init()

pygame.display.set_caption("Space Wars")

# background

WIDTH, HEIGHT = 1100, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # generating window
bg_img = pygame.image.load("background.png")  # background image
bg_img = pygame.transform.scale(bg_img, (2000, 1000))
mixer.music.load("background_music.mp3")
mixer.music.play()
# bulletSound = mixer.Sound("bullet_sound.mp3")
# powerupSound = mixer.Sound("power_up_sound.mp3")
# hitSound = mixer.Sound("explosion.mp3")

# ------
# initialing font style
text_font1 = pygame.font.SysFont("imprintshadow", 30)
text_font2 = pygame.font.SysFont("imprintshadow", 60, bold=True)
# ------

# things on screen

JET1 = pygame.image.load("space_ship11.png")  # jet1_block image
JET2 = pygame.image.load("space_ship22.png")  # jet2_block image
# bull_img1 = pygame.image.load("bullet _left_to_right.png")  # bullet1 image
# bull_img2 = pygame.image.load("bullet _left_to_right.png")
# BULLET1_img = pygame.transform.scale(bull_img1, (60, 60))
# BULLET2 = pygame.transform.scale(bull_img2, (50, 50))
# BULLET2_img = pygame.transform.rotate(BULLET2, 180)  # final bullet2 image
# Health_Power_up = pygame.image.load("Increase_health.png")
# Bullet_Power_up = pygame.image.load("Power_Doubler.png")
# Speed_Power_up = pygame.image.load("speed_boost.png")
# Speed_Power_up = pygame.transform.scale(Speed_Power_up, (120, 70))
# Health_Power_up = pygame.transform.scale(Health_Power_up, (50, 50))  # final health powerup
# Bullet_Power_up = pygame.transform.scale(Bullet_Power_up, (50, 50))  # final bullet powerup
# explosion_img = pygame.image.load("explosion.png")
# explosion_img = pygame.transform.scale(explosion_img, (20, 20))

FPS = 60

# jet blocks
jet1_block = pygame.Rect(50, 300, 80, 80)
jet2_block = pygame.Rect(950, 300, 80, 80)
# powerup_block = pygame.Rect(-100, -100, 50, 50)

# # score
# p1Score = 0
# p2Score = 0

# # list of bullets
# bullet_list1 = []
# bullet_list2 = []

# # maximum nuber of bullets
# max_bull_num_jet1 = 5
# max_bull_num_jet2 = 5

# speed of jets
jet_speed1 = 5
jet_speed2 = 5

# health of jets
# jet1_health = 300
# jet2_health = 300
# max_health = 300


# firring bullets
# def fire_bullets():
#     global jet1_health
#     global jet2_health
#     global hitSound

#     # for bullet1 movement
#     for item1 in bullet_list1:
#         item1.x += 7
#         if item1.x > 1090 or jet2_block.colliderect(item1):
#             if jet2_block.colliderect(item1):
#                 hitSound.play()
#                 if jet2_health > 0:
#                     jet2_health -= 10
#             bullet_list1.remove(item1)

#     # for bullet2 movement
#     for item2 in bullet_list2:
#         item2.x -= 7
#         if item2.x < 0 or jet1_block.colliderect(item2):
#             if jet1_block.colliderect(item2):
#                 hitSound.play()
#                 if jet1_health > 0:
#                     jet1_health -= 10
#             bullet_list2.remove(item2)


# ----------------------------------------------------------------------------------------------------------------------------------------------
# building every thing on screen
# def draw_window(jet1, jet2, listb1, listb2, health1, health2, hcolor1, hcolor2, winstr, ans, power_up, powerup_block,
#                 reload, score):
def draw_window(jet1, jet2):
    # global max_health

    # drawing background image
    WIN.blit(bg_img, (0, 0))
    # ------------------------------------------------------------------------------------------------------

    # generating and drawing Player name
    # text1 = text_font1.render("Player1", True, (255, 255, 255))
    # WIN.blit(text1, (20, 2))

    # text2 = text_font1.render("Player2", True, (255, 255, 255))
    # WIN.blit(text2, (970, 2))
    # ------------------------------------------------------------------------------------------------------

    # drawing and firing bullets
    # for itemb1 in listb1:
    #     WIN.blit(BULLET1_img, (itemb1.x, itemb1.y - 20))
    # for itemb2 in listb2:
    #     WIN.blit(BULLET2_img, (itemb2.x, itemb2.y - 20))
    # -------------------------------------------------------------------------------------------------------
    # drawing jets
    WIN.blit(JET1, (jet1.x, jet1.y))
    WIN.blit(JET2, (jet2.x, jet2.y))
    # ------------------------------------------------------------------------------------------------------
    # powerups
    # WIN.blit(power_up, (powerup_block.x, powerup_block.y))
    # ------------------------------------------------------------------------------------------------------

    # drawing and managing health bars
    # Player1
    # pygame.draw.rect(WIN, hcolor1, (10, 45, health1, 20), border_radius=5)
    # pygame.draw.rect(WIN, (255, 255, 255), (10, 45, max_health, 20), 4, 5)

    # # Player2
    # pygame.draw.rect(WIN, hcolor2, (790, 45, health2, 20), border_radius=5)
    # pygame.draw.rect(WIN, (255, 255, 255), (790, 45, max_health, 20), 4, 5)
    # -------------------------------------------------------------------------------

    # declaring winner
    # if ans:
    #     winText = text_font2.render(winstr, True, (255, 255, 255))
    #     reload_text = text_font2.render(reload, True, (225, 225, 225))
    #     WIN.blit(reload_text, (100, 500))
    #     WIN.blit(winText, (500, 600))
    # score_text = text_font2.render(score, True, (225, 225, 225))
    # WIN.blit(score_text, (500, 50))

    # # updating display
    pygame.display.update()
    # -------------------------------------------------------------------------------


def main():
    # global variables
    # global bullet_list1
    # global bullet_list2
    # global jet1_health
    # global jet2_health
    # global max_bull_num_jet1
    # global max_bull_num_jet2
    # global jet_speed1
    # global jet_speed2
    # global p1Score
    # global p2Score
    # global bulletSound

    # local variables
    # R1, G1, B1 = 0, 225, 0
    # R2, G2, B2 = 0, 225, 0
    inside, previous = 0, 0
    answer = False
    run = True
    # power_up = Speed_Power_up
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        # current_time = pygame.time.get_ticks()
        # if current_time - previous > 15000:
        #     power_up = random.choice([Health_Power_up, Bullet_Power_up, Speed_Power_up])
        #     max_bull_num_jet2 = 5
        #     max_bull_num_jet1 = 5
        #     jet_speed2 = 5
        #     jet_speed1 = 5
        #     powerup_block.x = random.randint(10, 990)
        #     powerup_block.y = random.randint(20, 600)
        #     previous = current_time
        # if powerup_block.x != -100:
        #     inside += 1
        # if inside > 180:
        #     powerup_block.x = -100
        #     powerup_block.y = -100
        #     inside = 0
        # if jet1_block.colliderect(powerup_block) or jet2_block.colliderect(powerup_block):
        #     powerupSound.play()
        #     if jet1_block.colliderect(powerup_block):
        #         if power_up == Health_Power_up:
        #             if jet1_health + 40 > 300:
        #                 jet1_health = 300
        #             else:
        #                 jet1_health += 40
        #         elif power_up == Bullet_Power_up:
        #             max_bull_num_jet1 += 2
        #         else:
        #             jet_speed1 += 2

        #     else:
        #         if power_up == Health_Power_up:
        #             if jet2_health + 40 > 300:
        #                 jet2_health = 300
        #             else:
        #                 jet2_health += 40
        #         elif power_up == Bullet_Power_up:
        #             max_bull_num_jet2 += 2
        #         else:
        #             jet_speed2 += 2

        #     powerup_block.x = -100
        #     powerup_block.y = -100
        #     inside = 0

        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         run = False
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_LCTRL and len(bullet_list1) < max_bull_num_jet1:
        #             bulletSound.play()
        #             bullet1_X = jet1_block.x + 45
        #             bullet1_Y = jet1_block.y + 45
        #             bullet1_block = pygame.Rect(bullet1_X + 25, bullet1_Y, 35, 20)
        #             bullet_list1.append(bullet1_block)
        #         if event.key == pygame.K_RCTRL and len(bullet_list2) < max_bull_num_jet2:
        #             bulletSound.play()
        #             bullet2_X = jet2_block.x + 45
        #             bullet2_Y = jet2_block.y + 45
        #             bullet2_block = pygame.Rect(bullet2_X - 25, bullet2_Y, 35, 20)
        #             bullet_list2.append(bullet2_block)

        # operating keyboard keys
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

        # health bar color change

        # if jet1_health > 150 and R1 <= 225:
        #     R1 = int((9 / 4) * (300 - jet1_health))
        # elif 0 <= jet1_health < 150:
        #     R1 = 225
        #     G1 = int((3 / 2) * jet1_health)

        # if jet2_health > 150 and R2 <= 225:
        #     R2 = int((9 / 4) * (300 - jet2_health))
        # elif 0 <= jet2_health < 150:
        #     R2 = 225
        #     G2 = int((3 / 2) * jet2_health)

        # health1_color = (R1, G1, B1)
        # health2_color = (R2, G2, B2)

        # winner

        winner_text = ""
        reload_text = ""

        # Score_board = str(p1Score) + " - " + str(p2Score)
        # if jet1_health <= 0 or jet2_health <= 0:
        #     previous = current_time
        #     jet_speed1 = 0
        #     jet_speed2 = 0
        #     max_bull_num_jet1 = 0
        #     max_bull_num_jet2 = 0
        #     if jet1_health == 0 and jet2_health == 0:
        #         winner_text = "BOTH PLAYER WON"
        #         answer = True
        #         bullet_list1 = []
        #         bullet_list2 = []
        #         p1Score += 1
        #         p2Score += 1
        #         jet2_health, jet2_health = -1, -1
        #         # run = False
        #     elif jet1_health == 0:
        #         winner_text = "Player-2 WINS!"
        #         answer = True
        #         bullet_list1 = []
        #         bullet_list2 = []
        #         p2Score += 1
        #         jet1_health = -1
        #         # run = False
        #     elif jet2_health == 0:
        #         winner_text = "Player-1 WINS!"
        #         answer = True
        #         bullet_list1 = []
        #         bullet_list2 = []
        #         p1Score += 1
        #         jet2_health = -1
        #     if key_pressed[pygame.K_SPACE]:
        #         jet1_health = 300
        #         jet2_health = 300
        #         winner_text = ""
        #         fire_bullets()
        #         jet1_block.x, jet1_block.y = 50, 300
        #         jet2_block.x, jet2_block.y = 950, 300
        #         jet_speed1 = 5
        #         jet_speed2 = 5
        #         max_bull_num_jet1 = 5
        #         max_bull_num_jet2 = 5
        #         R1, G1, B1 = 0, 225, 0
        #         R2, G2, B2 = 0, 225, 0
        #         previous = current_time+15000

        if key_pressed[pygame.K_ESCAPE]:
                run = False
        #     reload_text = "Press space bar to play again"

            # run = False

        # bullet firing
        # fire_bullets()

        # window and other components generating
        draw_window(jet1_block, jet2_block)

    pygame.quit()


if __name__ == "__main__":
    main()
