import pygame

pygame.init()
pygame.display.set_caption("Welcome to our game")
screen = pygame.display.set_mode((800, 600))

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

            if self.count >= 10:
                self.bomb_index = (self.bomb_index +1 ) % len(self.bomb)
                self.count = 0
        else:
            screen.blit(self.bomb[0], [x, y])

bomb_anim = BombAnim(bomb_images)



done = False
BACK_GROUND = (148, 198, 153)
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                bomb_anim.state = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                bomb_anim.state = False




    screen.fill(BACK_GROUND)
    bomb_anim.run(screen, 10, 10)
    clock.tick(60)
    pygame.display.flip()