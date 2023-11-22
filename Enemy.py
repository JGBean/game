import numpy as np
from PIL import ImageDraw, ImageFont, Image
import random

class Enemy:
    def __init__(self, spawn_position):
        self.appearance = 'circle'
        self.state = 'alive'
        self.position = np.array([spawn_position[0] - 20, spawn_position[1] - 20, spawn_position[0] + 10, spawn_position[1] + 10])
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
        self.outline = "#00FF00"
        self.speed = 5
        self.drawmob = Image.open('/home/jeon7263/game/res/gstand.gif').resize((30, 30))


    

    def move(self):
        # Generate a random direction vector
        direction = np.random.uniform(-1, 1, 2)
        direction /= np.linalg.norm(direction)  # Normalize the direction vector

        # Update the position based on the random direction
        self.position[0] += direction[0] * self.speed
        self.position[1] += direction[1] * self.speed
        self.position[2] += direction[0] * self.speed
        self.position[3] += direction[1] * self.speed

        # Ensure the object stays within the screen boundaries
        self.position[0] = max(1, min(self.position[0], 230))
        self.position[1] = max(1, min(self.position[1], 230))
        self.position[2] = max(10, min(self.position[2], 240))
        self.position[3] = max(10, min(self.position[3], 240))

        # Bounce back when hitting the walls
        if self.position[0] <= 1 or self.position[2] >= 230:
            direction[0] *= -1
        if self.position[1] <= 1 or self.position[3] >= 230:
            direction[1] *= -1