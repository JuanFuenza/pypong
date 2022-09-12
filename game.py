import pygame
from settings import *
from classes.player import Player
from classes.ball import Ball
from functions import get_new_ball, score

# init pygame
pygame.init()

# display surface
ds = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame!")
clock = pygame.time.Clock()

# play
play = False

# fonts
font = pygame.font.Font("assets/fonts/VCR_OSD_MONO_1.001.ttf", 20)
game_font = pygame.font.Font("assets/fonts/VCR_OSD_MONO_1.001.ttf", 120)

# texts
start_game = game_font.render("PYPONG", False, "white")
start_game_rect = start_game.get_rect(center = (WIDTH//2, 150))

new_game = font.render("Press space to start", False, "white")
new_game_rect = new_game.get_rect(center = (WIDTH//2, 400))

# keys
# player 1
UP = pygame.K_UP
DOWN = pygame.K_DOWN

# player 2
W = pygame.K_w
S = pygame.K_s

# players
player = Player(W, S, 50)
player_2 = Player(UP, DOWN, 750)

players = [player, player_2]

# ball
ball = Ball()

# score 
s_1 = 0
s_2 = 0

# sounds
bounce_sfx = pygame.mixer.Sound("assets/sfx/bounce.wav")
bounce_sfx.set_volume(0.1)

score_sfx = pygame.mixer.Sound("assets/sfx/score.wav")
score_sfx.set_volume(0.1)

# Init music
pygame.mixer.init()
pygame.mixer.music.load("assets/music/music.mp3")
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(loops=-1)

# game main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not play:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    play = True
                    pygame.mixer.music.set_volume(0.10)
    
    # fill
    ds.fill((0, 0, 0))

    if not play:
        ds.blit(start_game, start_game_rect)
        ds.blit(new_game, new_game_rect)
    else:
        ball.draw(ds)
        ball.update()

        # player
        for p in players:
            p.draw(ds)
            p.update()

            # score
            score(ds, s_1, 50, font)
            score(ds, s_2, 740, font)
        
            # ball collision
            collision_tolerance = 10
            if ball.rect.colliderect(p.rect): 
                if int(p.rect.right - ball.rect.left) <= collision_tolerance and ball.vel_x < 0 or int(p.rect.left - ball.rect.right) <= collision_tolerance and ball.vel_x > 0:
                    ball.vel_x *= -1
                    ball.vel_x = round(ball.vel_x * 1.2)
                    bounce_sfx.play()
        
        if ball.rect.x > WIDTH + 100:
            get_new_ball(ball)
            s_1 += 1
            score_sfx.play()

        if ball.rect.x < 0 - 100:
            get_new_ball(ball)
            s_2 += 1
            score_sfx.play()


    # update
    pygame.display.update()
    clock.tick(FPS)

# pygame end game
pygame.quit()