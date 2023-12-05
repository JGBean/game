import numpy as np
from PIL import ImageDraw, ImageFont, Image
import random
from Snow import Snow

class Enemy:
    def __init__(self, spawn_position):
        self.state = 'alive'
        self.position = np.array([spawn_position[0], spawn_position[1]])
        self.center = self.position + np.array([10, 10])
        self.speed = 6
        self.hp = 2
        self.drawmob = Image.open('/home/jeon7263/game/game/res/gstand.png').resize((20, 20))
        self.drawslow = Image.open('/home/jeon7263/game/game/res/ghit.png').resize((20,20))
        self.drawdie = Image.open('/home/jeon7263/game/game/res/gdead.png').resize((20,20))
        

    def move(self):
        self.position[1] += random.randint(-self.speed, self.speed)
        self.position[0] += random.randint(-self.speed, self.speed)

        if self.position[0] <= 15: # 화면 벗어남 방지
            self.position[0] = 15
        elif self.position[0] >= 225: 
            self.position[0] = 225

        if self.position[1] <= 15:
            self.position[1] = 15
        elif self.position[1] >= 115: 
            self.position[1] = 115

        self.center = self.position + np.array([10, 10]) # 중앙점 갱신
    
    def throw_snow(self): # 적이 눈을 던질 수 있도록 함
        snow = Snow(self.center, 'down')
        return snow
