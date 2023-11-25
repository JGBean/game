import numpy as np
from PIL import ImageDraw, ImageFont, Image
class Bullet:
    def __init__(self, position, command):
        self.appearance = 'rectangle'
        self.speed = 10
        self.position = np.array([position[0]-5, position[1]-5, position[0]+5, position[1]+5])
        self.direction = {'up' : False, 'down' : False, 'left' : False, 'right' : False}
        self.state = None
        self.outline = "#0000FF"
        self.collided = False 
        self.drawsnow = Image.open('/home/jeon7263/game/game/res/snow.png').resize((10,10))
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
            

    def collision_check(self, enemys):
        if not self.collided:  # 이미 충돌한 경우에는 더 이상 확인하지 않음
            for enemy in enemys:
                if enemy.hp > 0:
                    collision = self.overlap(self.position, enemy.position)

                    if collision:
                        enemy.hp = max(0, enemy.hp - 1)
                        self.state = 'hit'
                        self.collided = True  # 충돌 감지 후에는 더 이상 확인하지 않도록 설정
                        break  # 다른 적들과의 충돌 확인을 중단




    def overlap(self, ego_position, other_position):
        ego_left, ego_top, ego_right, ego_bottom = ego_position
        other_left, other_top, other_right, other_bottom = other_position

    # 두 물체가 스치거나 겹치는지 여부를 확인
        overlap_x = (ego_left <= other_right) and (ego_right >= other_left)
        overlap_y = (ego_top <= other_bottom) and (ego_bottom >= other_top)

        return overlap_x and overlap_y