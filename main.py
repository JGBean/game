from PIL import Image, ImageDraw, ImageFont
import time
import random
import numpy as np
from Enemy import Enemy
from Bullet import Bullet
from Character import Character
from Joystick import Joystick

def main():
    rand = random.randint(20, 50)
    fnt = ImageFont.truetype("/home/jeon7263/game/res/hi.ttf", 20)
    enemy_path = '/home/jeon7263/game/res/gstand.gif'
    player_path = '/home/jeon7263/game/res/rstand.gif'
    background_path = '/home/jeon7263/game/res/background.gif'

    joystick = Joystick()
    character = Character(joystick.width, joystick.height)

    image = Image.new("RGB", (joystick.width, joystick.height))
    draw = ImageDraw.Draw(image)
    start = Image.open("/home/jeon7263/game/res/start.jpeg").resize((240,240))
    backgroundImage = Image.open(background_path).resize((240, 240))
    playerImage = Image.open(player_path).resize((40, 40))
    enemyImage = Image.open(enemy_path).resize((40, 40))

    joystick.disp.image(image)

    player = Character(joystick.width, joystick.height)
    positionXIndex = [rand, rand+40, rand+80, rand+120]

    enemy1 = Enemy((positionXIndex[0], -20))
    enemy2 = Enemy((positionXIndex[1], -20))
    enemy3 = Enemy((positionXIndex[2], -20))
    enemy4 = Enemy((positionXIndex[3], -20))

    enemys_list = [enemy1, enemy2, enemy3, enemy4]
    bullets = []

    while True:
        command = {'move': False, 'up_pressed': False , 'down_pressed': False, 'left_pressed': False, 'right_pressed': False}
        
        if not joystick.button_U.value:  # up pressed
            command['up_pressed'] = True
            command['move'] = True

        if not joystick.button_D.value:  # down pressed
            command['down_pressed'] = True
            command['move'] = True

        if not joystick.button_L.value:  # left pressed
            command['left_pressed'] = True
            command['move'] = True

        if not joystick.button_R.value:  # right pressed
            command['right_pressed'] = True
            command['move'] = True

        if not joystick.button_A.value: # A pressed
            bullet = Bullet(character.center, command)
            bullets.append(bullet)

        player.move(command)

        for bullet in bullets:
            bullet.collision_check(enemys_list)
            bullet.move()
        
        image.paste(backgroundImage, (0,0))
        # draw.ellipse(tuple(player.position), outline = player.outline, fill = (0, 255, 0))
        image.paste(player.drawplayer, (player.position[0], player.position[1]))

        for enemy in enemys_list:
            # randomIndex = random.sample(positionXIndex, 4)

            image.paste(enemy.drawmob, (enemy.position[0], enemy.position[1]))
            enemy.move()

        for bullet in bullets:
            if bullet.state != 'hit':
                draw.rectangle(tuple(bullet.position), outline = bullet.outline, fill = (0, 0, 255))                
        joystick.disp.image(image)        

if __name__ == '__main__':
    main()