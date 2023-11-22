import numpy as np
from PIL import ImageDraw, ImageFont, Image


class Character:
    def __init__(self, width, height):
        self.appearance = 'circle'
        self.state = None
        self.speed = 5
        width = 120
        height = 223
        self.position = np.array([width - 10, height - 10, width + 10, height + 10])
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
        self.outline = "#FFFFFF"
        self.drawplayer = Image.open('/home/jeon7263/game/res/rstand.gif').resize((30, 30))


    def move(self, command = None):
        if command['move'] == False:
            self.state = None
            self.outline = "#FFFFFF" #검정색상 코드!
        
        else:
            self.state = 'move'
            self.outline = "#FF0000" #빨강색상 코드!

            if command['left_pressed']:
                self.position[0] -= self.speed
                self.position[2] -= self.speed
                
            if command['right_pressed']:
                self.position[0] += self.speed
                self.position[2] += self.speed

            if command['up_pressed']:
                self.position[1] -= self.speed
                self.position[3] -= self.speed
                
            if command['down_pressed']:
                self.position[1] += self.speed
                self.position[3] += self.speed

        if self.position[0] < 1 or self.position[2] < 1: #벽 뚫지 못하게 방지
            self.position[0] += self.speed 
            self.position[2] += self.speed 
        elif self.position[0] > 235 or self.position[2] > 235:
            self.position[0] -= self.speed 
            self.position[2] -= self.speed 
        #캐릭터가 양쪽 벽에 닿으면 튕기게
        if self.position[1] < 1 or self.position[3] < 10: #벽 뚫지 못하게 방지
            self.position[1] += self.speed 
            self.position[3] += self.speed 
        elif self.position[1] > 235 or self.position[3] > 235:
            self.position[1] -= self.speed 
            self.position[3] -= self.speed 

        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2]) 