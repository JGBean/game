import numpy as np
from PIL import ImageDraw, ImageFont, Image

class Bullet:
    def __init__(self, position, command):
        self.appearance = 'rectangle'
        self.speed = 10
        self.position = np.array([position[0] - 5, position[1] - 5, position[0] + 5, position[1] + 5])
        self.direction = {'up': False, 'down': False, 'left': False, 'right': False}
        self.state = None
        self.outline = "#0000FF"
        self.collided = False
        self.collision_range = 10
        self.drawsnow = Image.open('/home/jeon7263/game/game/res/snow.png').resize((10, 10))
        
        if command['up_pressed']:
            self.direction['up'] = True
        if command['down_pressed']:
            self.direction['down'] = True
        if command['right_pressed']:
            self.direction['right'] = True
        if command['left_pressed']:
            self.direction['left'] = True

    def move(self):
        if self.direction['up']:
            self.position[1] -= self.speed
            self.position[3] -= self.speed

        if self.direction['down']:
            self.position[1] += self.speed
            self.position[3] += self.speed

        if self.direction['left']:
            self.position[0] -= self.speed
            self.position[2] -= self.speed

        if self.direction['right']:
            self.position[0] += self.speed
            self.position[2] += self.speed

    def collision_check(self, enemies):
        if not self.collided:  # 이미 충돌한 경우에는 더 이상 확인하지 않음
            for enemy in enemies:
                if enemy.hp > 0:
                    distance = self.calculate_distance(self.position, enemy.position)
                    if distance <= self.collision_range:
                        enemy.hp = max(0, enemy.hp - 1)
                        self.state = 'hit'
                        self.collided = True  # 충돌 감지 후에는 더 이상 확인하지 않도록 설정
                        break  # 다른 적들과의 충돌 확인을 중단

    def calculate_distance(self, position1, position2):
        x1, y1 = position1[0], position1[1]
        x2, y2 = position2[0], position2[1]
        distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return distance
