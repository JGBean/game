import numpy as np
import random

class Enemy:
    def __init__(self, spawn_position):
        self.appearance = 'circle'
        self.state = 'alive'
        self.radius = 25
        self.position = np.array([spawn_position[0] - self.radius, spawn_position[1] - self.radius, spawn_position[0] + self.radius, spawn_position[1] + self.radius])
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
        self.outline = "#00FF00"
        self.speed = 1
    
    def move(self):
        # Calculate a random offset in the range of -5 to 5 for both x and y
        offset_x = np.random.uniform(-5, 5)
        offset_y = np.random.uniform(-5, 5)

        # Calculate the new x and y positions
        new_x = self.center[0] + offset_x
        new_y = self.center[1] + offset_y

        # Check if the new position is outside the screen boundaries
        if new_x - self.radius < 0:
            new_x = self.radius
        elif new_x + self.radius > 240:
            new_x = 240 - self.radius

        if new_y - self.radius < 0:
            new_y = self.radius
        elif new_y + self.radius > 240:
            new_y = 240 - self.radius

        # Update the enemy's position
        self.position = np.array([new_x - self.radius, new_y - self.radius, new_x + self.radius, new_y + self.radius])
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
