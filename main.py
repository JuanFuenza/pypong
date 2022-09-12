import pygame
from random import randint, random

def collision(object):
    if object.rect.top <= 0:
        object.rect.top = 0
        object.vel *= -1
    if object.rect.bottom >= HEIGHT:
        object.rect.bottom = HEIGHT
        object.vel *= -1

def get_new_ball(ball):
        direction = [-1, 1]
        ball.x_pos = WIDTH // 2
        ball.y_pos = randint(0, HEIGHT - 10)
        ball.vel_x = randint(3, 5) * direction[randint(0,1)]
        ball.acc = random
        ball.vel_y = randint(3, 9)

def score(score, x):
    text = font.render(f"Score: {score}", False, "white")
    text_rect = text.get_rect(center = (x, 10))
    ds.blit(text, text_rect)

class Player():
    def __init__(self, key_up: pygame.key, key_down: pygame.key, x_pos: int):
        self.vel = 0
        self.acc = 0.5
        self.friction = 0.99
        self.max_speed = 25
        self.key_up = key_up
        self.key_down = key_down
        self.x_pos = x_pos
        self.y_pos = HEIGHT//2
        self.color = (randint(50, 255), randint(50, 255), randint(50, 255))
        self.rect = pygame.rect.Rect((self.x_pos, self.y_pos, 16, 120))
        self.rect.center = (self.x_pos, HEIGHT//2)

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[self.key_up]:
            if self.vel > -self.max_speed:
                self.vel -= self.acc

        if key[self.key_down]:
            if self.vel < self.max_speed:
                self.vel += self.acc
        
        self.y_pos += self.vel
        self.vel *= self.friction

        self.rect = pygame.rect.Rect((self.x_pos, self.y_pos, 16, 120))


    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def update(self):
        self.handle_keys()

class Ball():
    def __init__(self):
        self.vel_x = 5
        self.vel_y = 5
        self.acc = 0.5
        self.friction = 1
        self.max_speed = 25
        self.x_pos = WIDTH//2
        self.y_pos = HEIGHT//2
        self.color = (randint(50, 255), randint(50, 255), randint(50, 255))
        self.rect = pygame.rect.Rect((self.x_pos, self.y_pos, 16, 16))
        self.rect.center = (16, 120)

        self.rect = pygame.rect.Rect((self.x_pos, self.y_pos, 16, 16))

    def move(self):
        if self.rect.top <= 0 and self.vel_y < 0:
            self.rect.top = 0
            self.vel_y *= -1
        if self.rect.bottom >= HEIGHT and self.vel_y > 0:
            self.rect.bottom = HEIGHT
            self.vel_y *= -1

        self.x_pos += self.vel_x
        self.y_pos += self.vel_y
        self.vel_y *= self.friction
        self.vel_x *= self.friction

        self.rect = pygame.rect.Rect((int(self.x_pos), int(self.y_pos), 16, 16))
    
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.rect.center), 9)

    def update(self):
        self.move()
    
    def __del__(self):
        print("score")

# init pygame
pygame.init()

# display surface
WIDTH = 800
HEIGHT = 600
ds = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame!")
FPS = 60
clock = pygame.time.Clock()

# fonts
font = pygame.font.Font("assets/fonts/VCR_OSD_MONO_1.001.ttf", 20)

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

# game main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # fill
    ds.fill((0, 0, 0))

    ball.draw(ds)
    ball.update()

    # player
    for p in players:
        p.draw(ds)
        p.update()

        # collision
        collision(p)

        # score
        score(s_1, 50)
        score(s_2, 740)
    
        # ball collision
        collision_tolerance = 20
        if ball.rect.colliderect(p.rect): 
            if int(p.rect.right - ball.rect.left) <= collision_tolerance and ball.vel_x < 0 or int(p.rect.left - ball.rect.right) <= collision_tolerance and ball.vel_x > 0:
                ball.vel_x *= -1
                ball.vel_x = round(ball.vel_x * 1.2)
    
    if ball.rect.x > WIDTH + 100:
        get_new_ball(ball)
        s_1 += 1

    if ball.rect.x < 0 - 100:
        get_new_ball(ball)
        s_2 += 1


    # update
    pygame.display.update()
    clock.tick(FPS)

# pygame end game
pygame.quit()