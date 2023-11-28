import numpy as np
from PIL import ImageDraw, ImageFont, Image

class Snow:
    def __init__(self, position, direction):
        self.speed = 10
        self.position = np.array([position[0] - 5, position[1] - 5, position[0] + 5, position[1] + 5])
        self.direction = direction
        self.state = None
        self.outline = "#0000FF"
        self.collided = False
        self.drawsnow = Image.open('/home/jeon7263/game/game/res/snow.png').resize((10, 10))
        self.collision_range = 10  

    def move(self):
        if self.direction == 'down':
            self.position[1] += self.speed

    def collision_check(self, characters):
        if not self.collided:  # 이미 충돌한 경우에는 더 이상 확인하지 않음
            for character in characters:
                if character.hp > 0:
                    distance = self.calculate_distance(self.position, character.position)
                    if distance <= self.collision_range:
                        character.hp = max(0, character.hp - 1)
                        self.state = 'hit'
                        self.collided = True  # 충돌 감지 후에는 더 이상 확인하지 않도록 설정
                        break  # 다른 캐릭터들과의 충돌 확인을 중단

    def calculate_distance(self, position1, position2):
        x1, y1 = position1[0], position1[1]
        x2, y2 = position2[0], position2[1]
        distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return distance
