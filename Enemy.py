import numpy as np
from PIL import ImageDraw, ImageFont, Image
import random
from Snow import Snow
import time
class Enemy:
    def __init__(self, spawn_position):
        self.state = 'alive'
        self.position = np.array([spawn_position[0], spawn_position[1]])
        self.center = self.position + np.array([10, 10])
        self.speed = 8
        self.hp = 2
        self.last_snow_time = 0
        self.drawmob = Image.open('/home/jeon7263/game/game/res/gstand.png').resize((20, 20))
        self.drawslow = Image.open('/home/jeon7263/game/game/res/ghit.png').resize((20,20))
        self.drawdie = Image.open('/home/jeon7263/game/game/res/gdead.png').resize((20,20))
        

    def move(self):
        self.position[1] += random.randint(-self.speed, self.speed)
        self.position[0] += random.randint(-self.speed, self.speed)

        if self.position[0] <= 5:
            self.position[0] = 5
        elif self.position[0] >= 235: 
            self.position[0] = 235

        if self.position[1] <= 5:
            self.position[1] = 5
        elif self.position[1] >= 120: 
            self.position[1] = 120

        self.center = self.position + np.array([10, 10])
    
    def throw_snow(self):
        current_time = time.time()
        if current_time - self.last_snow_time >= random.uniform(1,3):
            self.last_snow_time = current_time
            snow = Snow(self.center, 'down')
            return snow
        
        else: None