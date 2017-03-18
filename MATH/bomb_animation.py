import pygame
import random, time


pygame.init()
pygame.display.set_caption("Welcome to our game")
screen = pygame.display.set_mode((800, 600))

done = False

bomb_images = [
    pygame.image.load("techkids - ezgame/image/bom/bom 1-01.png"),
    pygame.image.load("techkids - ezgame/image/bom/bom 2-01.png"),
    pygame.image.load("techkids - ezgame/image/bom/bom 3-01.png"),
    pygame.image.load("techkids - ezgame/image/bom/bom 4-01.png"),
    pygame.image.load("techkids - ezgame/image/bom/bom 5-01.png"),
    pygame.image.load("techkids - ezgame/image/bom/bom 6-01.png"),
    pygame.image.load("techkids - ezgame/image/bom/bom 7-01.png"),
    pygame.image.load("techkids - ezgame/image/bom/bom 8-01.png"),
    pygame.image.load("techkids - ezgame/image/bom/bom 9-01.png"),
    pygame.image.load("techkids - ezgame/image/bom/bom 10-01.png"),
    pygame.image.load("techkids - ezgame/image/bom/bom 11-01.png"),
    pygame.image.load("techkids - ezgame/image/bom/bom 12-01.png"),
    pygame.image.load("techkids - ezgame/image/bom/bom 13-01.png"),
    pygame.image.load("techkids - ezgame/image/bom/bom 14-01.png")
]

number_images = [
    pygame.image.load("techkids - ezgame/image/a, b/0-01.png"),
    pygame.image.load("techkids - ezgame/image/a, b/1-01.png"),
    pygame.image.load("techkids - ezgame/image/a, b/2-01.png"),
    pygame.image.load("techkids - ezgame/image/a, b/3-01.png"),
    pygame.image.load("techkids - ezgame/image/a, b/4-01.png"),
    pygame.image.load("techkids - ezgame/image/a, b/5-01.png"),
    pygame.image.load("techkids - ezgame/image/a, b/6-01.png"),
    pygame.image.load("techkids - ezgame/image/a, b/7-01.png"),
    pygame.image.load("techkids - ezgame/image/a, b/8-01.png"),
    pygame.image.load("techkids - ezgame/image/a, b/9-01.png"),
    pygame.image.load("techkids - ezgame/image/a, b/10-01.png"),
    pygame.image.load("techkids - ezgame/image/a, b/11-01.png"),
    pygame.image.load("techkids - ezgame/image/a, b/12-01.png"),
    pygame.image.load("techkids - ezgame/image/a, b/13-01.png"),
    pygame.image.load("techkids - ezgame/image/a, b/14-01.png"),
    pygame.image.load("techkids - ezgame/image/a, b/15-01.png"),
    pygame.image.load("techkids - ezgame/image/a, b/16-01.png"),
    pygame.image.load("techkids - ezgame/image/a, b/17-01.png"),
    pygame.image.load("techkids - ezgame/image/a, b/18-01.png"),
    pygame.image.load("techkids - ezgame/image/a, b/19-01.png"),
    pygame.image.load("techkids - ezgame/image/a, b/20-01.png"),
]

operation_image = [
    pygame.image.load("techkids - ezgame/image/operation/plus-01.png"),
    pygame.image.load("techkids - ezgame/image/operation/minus-01.png")
]

equal_image = pygame.image.load("techkids - ezgame/image/operation/equal-01.png")


true_image = pygame.image.load("techkids - ezgame/image/True_False/True-01.png")
false_image = pygame.image.load("techkids - ezgame/image/True_False/False-01.png")

BACK_GROUND = pygame.image.load("techkids - ezgame/image/background-01.png")
Number_Image = pygame.image.load("techkids - ezgame/image/a, b/1-01.png")

def play_sound(file_name):
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play(0)

class BombAnim:
    def __init__(self, bomb):
        self.bomb = bomb
        self.count = 0
        self.bomb_index = 0
        self.state = False

    def run(self, screen, x, y):
        if self.state:
            screen.blit(self.bomb[self.bomb_index], (x, y))
            self.count += 1
            #play_sound("Explosion.wav")

            if self.count >= 4.5:
                self.bomb_index = (self.bomb_index +1 ) % len(self.bomb)
                self.count = 0
        else:
            screen.blit(self.bomb[0], [x, y])

bomb_anim = BombAnim(bomb_images)

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        bomb_anim.state = True




    # screen.fill()
    screen.blit((BACK_GROUND),(0,0))
    screen.blit((Number_Image),(140,0))
    screen.blit((true_image),(50,230))
    screen.blit((false_image),(230,230))
    # screen.blit((operation_image),(300,0))
    screen.blit((equal_image),(400, 0))
    bomb_anim.run(screen, -180,-150)
    # clock.tick(360)
    pygame.display.flip()