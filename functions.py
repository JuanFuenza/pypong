from settings import *
from random import random, randint

def get_new_ball(ball):
    """
    Moves the ball to the center and gives a random direction and a random velocity
    Returns: None
    """
    direction = [-1, 1]
    ball.x_pos = WIDTH // 2
    ball.y_pos = randint(0, HEIGHT - 10)
    ball.vel_x = randint(3, 5) * direction[randint(0,1)]
    ball.acc = random
    ball.vel_y = randint(3, 9)

def score(surface, score, x_pos, font):
    """
    Gets the score for the player in a certain position and with a font give by the game
    Returns: None
    """
    text = font.render(f"Score: {score}", False, "white")
    text_rect = text.get_rect(center = (x_pos, 10))
    surface.blit(text, text_rect)

if __name__ == "__main__":
    get_new_ball()
    score()