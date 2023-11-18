import numpy as np
import random

class Enemy:
    def __init__(self, spawn_position):
        self.appearance = 'circle'
        self.state = 'alive'
        self.position = np.array([spawn_position[0] - 25, spawn_position[1] - 25, spawn_position[0] + 25, spawn_position[1] + 25])
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
        self.outline = "#00FF00"
        self.speed = 5  # Initial speed

    def move(self, other_enemies):
        # Calculate the new position based on the current speed
        new_x = self.position[0] + (np.random.randint(0, 2) * 2 - 1) * self.speed

        # Limit the new position to stay within the screen boundaries
        new_x = max(0, min(new_x, 240 - 50))  # Assuming width of enemy is 50

        # Move only in the upper half of the screen (adjust as needed)
        new_y = max(0, min(self.position[1] + (np.random.randint(0, 2) * 2 - 1) * self.speed, 120 - 50))  # Assuming height of enemy is 50

        # Check for collisions with other enemies and adjust position if necessary
        for other_enemy in other_enemies:
            if self != other_enemy and self.overlap(self.position, other_enemy.position):
                # Adjust the position to avoid overlap
                new_x, new_y = self.avoid_overlap(self.position, other_enemy.position)

        # Update the position
        self.position = np.array([new_x, new_y, new_x + 50, new_y + 50])  # Adjusted for assumed size

        # Update the center
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])

    def overlap(self, ego_position, other_position):
        '''
        Check if two rectangles overlap.
        Coordinates format: [x1, y1, x2, y2]
        '''
        return ego_position[0] < other_position[2] and ego_position[2] > other_position[0] \
               and ego_position[1] < other_position[3] and ego_position[3] > other_position[1]

    def avoid_overlap(self, ego_position, other_position):
        '''
        Adjust the position to avoid overlap with another rectangle.
        '''
        new_x = ego_position[0] + (ego_position[2] - ego_position[0]) * np.sign(ego_position[0] - other_position[0])
        new_y = ego_position[1] + (ego_position[3] - ego_position[1]) * np.sign(ego_position[1] - other_position[1])
        return new_x, new_y