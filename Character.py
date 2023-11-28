import numpy as np
from PIL import ImageDraw, ImageFont, Image


class Character:
    def __init__(self, width, height):
        self.state = None
        self.speed = 6
        self.hp = 2
        width = 120
        height = 223
        self.position = np.array([width - 10, height - 10, width + 10, height + 10])
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
        self.drawplayer = Image.open('/home/jeon7263/game/game/res/rstand.png').resize((20, 20))
        self.drawplayerhit = Image.open('/home/jeon7263/game/game/res/rplayerhit.png').resize((20,20))
        self.drawplayerdead = Image.open('/home/jeon7263/game/game/res/rdead.png').resize((20,20))

    def move(self, command):
        if command['up_pressed']:
            self.position[1] -= self.speed
            self.position[3] -= self.speed

        if command['down_pressed']:
            self.position[1] += self.speed
            self.position[3] += self.speed

        if command['left_pressed']:
            self.position[0] -= self.speed
            self.position[2] -= self.speed
            
        if command['right_pressed']:
            self.position[0] += self.speed
            self.position[2] += self.speed
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])

        if self.position[0] < 1 or self.position[2] < 1:
            self.position[0] += self.speed
            self.position[2] += self.speed
        elif self.position[0] > 235 or self.position[2] > 235:
            self.position[0] -= self.speed
            self.position[2] -= self.speed

        if self.position[1] < 1 or self.position[3] < 10:
            self.position[1] += self.speed
            self.position[3] += self.speed
        elif self.position[1] > 235 or self.position[3] > 235:
            self.position[1] -= self.speed
            self.position[3] -= self.speed

        # Update the center after the character has moved
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])

    def move2(self, command):
        if command['up_pressed']:
            self.position[1] -= self.speed/2
            self.position[3] -= self.speed/2

        if command['down_pressed']:
            self.position[1] += self.speed/2
            self.position[3] += self.speed/2

        if command['left_pressed']:
            self.position[0] -= self.speed/2
            self.position[2] -= self.speed/2
            
        if command['right_pressed']:
            self.position[0] += self.speed/2
            self.position[2] += self.speed/2
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])

        if self.position[0] < 1 or self.position[2] < 1:
            self.position[0] += self.speed
            self.position[2] += self.speed
        elif self.position[0] > 235 or self.position[2] > 235:
            self.position[0] -= self.speed
            self.position[2] -= self.speed

        if self.position[1] < 1 or self.position[3] < 10:
            self.position[1] += self.speed
            self.position[3] += self.speed
        elif self.position[1] > 235 or self.position[3] > 235:
            self.position[1] -= self.speed
            self.position[3] -= self.speed

        # Update the center after the character has moved
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])