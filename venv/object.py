import pygame
import random
class Object:

    def snake_display(self,snake_pstn,display, snake_color):
        self.snake_pstn = snake_pstn
        self.display = display
        self.snake_color = snake_color

        for pstn in self.snake_pstn:
            pygame.draw.rect(self.display, self.snake_color, pygame.Rect(pstn[0], pstn[1], 10, 10))


    def apple_display(self,apple_img, display, apple_pstn):
        self.apple_img = apple_img
        self.display = display
        self.apple_pstn = apple_pstn
        display.blit(self.apple_img, (self.apple_pstn[0], self.apple_pstn[1]))

class Action:

    def eat_apple(self,apple_pstn, score):
        self.apple_pstn = apple_pstn
        self.score = score
        self.apple_pstn = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
        self.score += 1
        return self.apple_pstn, self.score