import numpy as np
from PIL import ImageDraw, ImageFont, Image
class Snow:
    def __init__(self, position):
        self.appearance = 'rectangle'
        self.speed = 10
        self.position = np.array([position[0]-5, position[1]-5, position[0]+5, position[1]+5])
        self.state = None
        self.outline = "#0000FF"
        self.collided = False 
        self.drawsnow = Image.open('/home/jeon7263/game/game/res/snow.png').resize((10,10))

    
    def collision_check(self, characters):
        if not self.collided:  # 이미 충돌한 경우에는 더 이상 확인하지 않음
            for player in characters:
                if player.hp > 0:
                    collision = self.overlap(self.position, player.position)

                    if collision:
                        player.hp = max(0, player.hp - 1)
                        self.state = 'hit'
                        self.collided = True  # 충돌 감지 후에는 더 이상 확인하지 않도록 설정
                        break  # 다른 적들과의 충돌 확인을 중단




    def overlap(self, ego_position, other_position, epsilon=1e-9):
        ego_left, ego_top, ego_right, ego_bottom = ego_position
        other_left, other_top, other_right, other_bottom = other_position

    # 두 물체가 스치거나 겹치는지 여부를 확인
        overlap_x = (ego_left <= other_right + epsilon) and (ego_right >= other_left - epsilon)
        overlap_y = (ego_top <= other_bottom + epsilon) and (ego_bottom >= other_top - epsilon)

        return overlap_x and overlap_y