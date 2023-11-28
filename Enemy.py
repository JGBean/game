import numpy as np
from PIL import ImageDraw, ImageFont, Image
import random
from Snow import Snow
import time
class Enemy:
    def __init__(self, spawn_position):
        self.appearance = 'circle'
        self.state = 'alive'
        self.position = np.array([spawn_position[0] - 10, spawn_position[1] - 10, spawn_position[0] + 10, spawn_position[1] + 10])
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
        self.outline = "#00FF00"
        self.speed = 6
        self.hp = 2
        self.last_snow_time = 0
        self.drawmob = Image.open('/home/jeon7263/game/game/res/gstand.png').resize((20, 20))
        self.drawslow = Image.open('/home/jeon7263/game/game/res/ghit.png').resize((20,20))
        self.drawdie = Image.open('/home/jeon7263/game/game/res/gdead.png').resize((20,20))
        

    def move(self):
    # Randomly change the position within the speed limits
        self.position[1] += random.randint(-self.speed, self.speed)
        self.position[3] += random.randint(-self.speed, self.speed)
        self.position[2] += random.randint(-self.speed, self.speed)
        self.position[0] += random.randint(-self.speed, self.speed)


    # Check if the object hits the walls and adjust the position accordingly
        if self.position[0] <= 1:
            self.position[0] = 1
            self.position[2] += random.randint(0, self.speed)
        elif self.position[2] >= 230:
            self.position[2] = 230
            self.position[0] -= random.randint(0, self.speed)

        if self.position[1] <= 1:
            self.position[1] = 1
            self.position[3] += random.randint(0, self.speed)
        elif self.position[3] >= 230:
            self.position[3] = 230
            self.position[1] -= random.randint(0, self.speed)

    # Ensure the object stays within the screen boundaries
        self.position[0] = max(1, min(self.position[0], 230))
        self.position[1] = max(1, min(self.position[1], 230))
        self.position[2] = max(10, min(self.position[2], 240))
        self.position[3] = max(10, min(self.position[3], 240))

    # Calculate the center based on the updated position
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])

    def move2(self):
    # Randomly change the position within the speed limits
        self.position[1] += random.randint(-self.speed/2, self.speed/2)
        self.position[3] += random.randint(-self.speed/2, self.speed/2)
        self.position[2] += random.randint(-self.speed/2, self.speed/2)
        self.position[0] += random.randint(-self.speed/2, self.speed/2)
  

    # Check if the object hits the walls and adjust the position accordingly
        if self.position[0] <= 1:
            self.position[0] = 1
            self.position[2] += random.randint(0, self.speed/2)
        elif self.position[2] >= 230:
            self.position[2] = 230
            self.position[0] -= random.randint(0, self.speed/2)

        if self.position[1] <= 1:
            self.position[1] = 1
            self.position[3] += random.randint(0, self.speed/2)
        elif self.position[3] >= 230:
            self.position[3] = 230
            self.position[1] -= random.randint(0, self.speed/2)

   
        self.position[0] = max(1, min(self.position[0], 230))
        self.position[1] = max(1, min(self.position[1], 120))
        self.position[2] = max(10, min(self.position[2], 240))
        self.position[3] = max(10, min(self.position[3], 240))

  
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
    
    def throw_snow(self):
        current_time = time.time()
        if current_time - self.last_snow_time >= random.uniform(2,4):
            self.last_snow_time = current_time
            snow = Snow(self.center, 'down')  # 눈 객체 생성
            return snow
        else:
            return None
    
        
