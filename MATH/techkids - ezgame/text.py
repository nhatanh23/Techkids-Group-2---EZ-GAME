import pygame
class Text:
    def __init__(self, text, font, color):
        self.color = color
        self.font = font
        self.text = font.render(text, True, self.color)

    def display_text(self, x, y):
        screen.blit(self.text, (x, y))

font_name = ("font/utm-avobold.ttf")

font = pygame.font.Font(font_name, 30)
display_text(30,30)
Text("mn", font, (250,250,250))
