import pygame
import random, time


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

score_image = pygame.image.load("techkids - ezgame/image/score-01.png")
score_number_image = [
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

true_image = pygame.image.load("techkids - ezgame/image/True_False/True-01.png")
false_image = pygame.image.load("techkids - ezgame/image/True_False/False-01.png")

BACK_GROUND = pygame.image.load("techkids - ezgame/image/background-01.png")
game_lose_background = pygame.image.load("techkids - ezgame/image/end game/end game-01.png")
replay_button = pygame.image.load("techkids - ezgame/image/end game/replay-01.png")

lose = False

def play_sound(file_name):
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play(0)

class BombAnim:
    def __init__(self, bomb):
        self.bomb = bomb
        self.count = 0
        self.bomb_index = 0
        self.state = True


    def run(self, screen, x, y):
        if self.state:
            screen.blit(self.bomb[self.bomb_index], (x, y))
            self.count += 1
            #play_sound("Explosion.wav")
        else:
            screen.blit(self.bomb[0], [x, y])

bomb_anim = BombAnim(bomb_images)

clock = pygame.time.Clock()
time_variable = pygame.time.get_ticks() - 1500
time_changebomb = pygame.time.get_ticks() - 1500
time_win = pygame.time.get_ticks() - 6000

def score_count(score,i,j):
    font_name = ("font/utm-avobold.ttf")
    font = pygame.font.Font(font_name, 30)

    text = font.render("Score: "+ str(score), True, (255,255,0))
    screen.blit(text, (i, j))

def check_win_lose(c, x, score):
    if event.type == pygame.KEYDOWN:
        #if pygame.time.get_ticks() - time_win <= 5000:
        if event.key == pygame.K_t or event.key == pygame.K_LEFT:
            screen.blit((true_image), (50, 250))
            if c == x:
                score += 1
                print("win")
                score_count(score, 400, 50)
                scene = 0
            else:
                print("lose")
                scene = 1
        if event.key == pygame.K_r or event.key == pygame.K_RIGHT:
            screen.blit((false_image), (230, 250))
            if c == x:
                print("lose")
                scene = 1
            else:
                score += 1
                print("win")
                score_count(score, 400, 50)
                scene = 0

        #else:
            #scene = 1

        return score, scene


# def replay():
#     if event.type == pygame.KEYDOWN:
#         if event.key == pygame.K_UP:
#             done = False





# a = random.randint(0, 10)
# b = random.randint(0, 10)
# d = random.randint(0, 20)
# operation = [a + b, a - b]
# x = random.choice(operation)
# number_list = [d, x]
# c = random.choice(number_list)
# time_variable = pygame.time.get_ticks()
#
# Number_Image_a = number_images[a]
# Number_Image_b = number_images[b]
# Number_Image_c = number_images[c]

score = 0

done = False
result = False
scene = 0

while not done:
    if scene == 0:
        screen.blit((BACK_GROUND), (0, 0))

        if pygame.time.get_ticks() - time_variable >= 1000:
            a = random.randint(0, 10)
            b = random.randint(0, 10)
            d = random.randint(0, 20)
            operation = [a + b, a - b]
            x = random.choice(operation)
            number_list = [d, x]
            c = random.choice(number_list)
            time_variable = pygame.time.get_ticks()

            Number_Image_a = number_images[a]
            Number_Image_b = number_images[b]
            Number_Image_c = number_images[c]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif check_win_lose(c, x, score):
                # done = False
                [score, scene] = check_win_lose(c, x, score)
                print(scene)
                print(score)

        if pygame.time.get_ticks() - time_changebomb >= (1000/17):
            print(pygame.time.get_ticks())
            bomb_anim.bomb_index = (bomb_anim.bomb_index + 1) % len(bomb_anim.bomb)
            time_changebomb = pygame.time.get_ticks()

        screen.blit((Number_Image_a), (100,0))
        screen.blit((Number_Image_b), (290, 0))
        screen.blit((Number_Image_c), (500, 0))
        screen.blit((true_image),(50,230))
        screen.blit((false_image),(230,230))
        screen.blit((equal_image),(400, 0))
        bomb_anim.run(screen, -180, -150)
        score_count(score, 400, 50)


        if x == operation[0]:
            screen.blit((operation_image[0]), (220, -10))
        elif x == operation[1]:
            screen.blit((operation_image[1]), (220, -10))

    if scene == 1:
        screen.blit(game_lose_background, (0, 0))
        score_count(score, 300, 220)
        screen.blit(replay_button, (250, 150))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    screen.blit(replay_button, (250, 120))
                    done = False
                    scene = 0
                    score = 0
                elif event.key == pygame.K_DOWN:
                    done = True



    # clock.tick(360)
    pygame.display.flip()