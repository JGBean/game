import numpy as np
from PIL import ImageDraw, ImageFont, Image
import pygame # 소리 넣는데 사용

class Snow:
    def __init__(self, position, direction):
        self.speed = 10
        self.position = position.copy()
        self.direction = direction
        self.state = None
        self.collided = False
        self.drawsnow = Image.open('/home/jeon7263/game/game/res/snow.png').resize((10, 10))
        self.collision_range = 13 # 캐릭터와의 거리가 13이하면 충돌  

    def move(self):
        if self.direction == 'down':
            self.position[1] += self.speed

    def collision_check(self, characters):
        if not self.collided: 
            for character in characters:
                if character.hp > 0:
                    distance = self.calculate_distance(self.position, character.position) # 눈과 캐릭터 사이의 거리 구하기
                    if distance <= self.collision_range:
                        character.hp = character.hp - 1
                        self.state = 'hit'
                        self.collided = True  
                        pygame.mixer.init()
                        pygame.mixer.music.load("/home/jeon7263/game/game/res/hit.wav")
                        pygame.mixer.music.play(0)
                        break 

    def calculate_distance(self, position1, position2): # 점과 점 사이의 거리 구하기 공식
        x1, y1 = position1[0] + 5, position1[1] + 5
        x2, y2 = position2[0] + 10, position2[1] + 10
        distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return distance