import numpy as np
import random

class Enemy:
    def __init__(self, spawn_position):
        self.appearance = 'circle'
        self.state = 'alive'
        self.position = np.array([spawn_position[0] - 25, spawn_position[1] - 25, spawn_position[0] + 25, spawn_position[1] + 25])
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
        self.outline = "#00FF00"
        self.speed = 4  # Initial speed

    def move(self):
        # Calculate the new position based on the current speed
        new_x = self.position[0] + (np.random.randint(0, 2) * 2 - 1) * self.speed

        # Limit the new position to stay within the screen boundaries
        new_x = max(0, min(new_x, 240 - 50))  # Assuming width of enemy is 50

        # Move only in the upper half of the screen (adjust as needed)
        new_y = max(0, min(self.position[1] + (np.random.randint(0, 2) * 2 - 1) * self.speed, 120 - 50))  # Assuming height of enemy is 50

        # Update the position
        self.position = np.array([new_x, new_y, new_x + 50, new_y + 50])  # Adjusted for assumed size

        # Update the center
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])





