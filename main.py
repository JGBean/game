from PIL import Image, ImageDraw, ImageFont
import time
import random
import os
import sys
import numpy as np
from Enemy import Enemy
from Bullet import Bullet
from Character import Character
from Joystick import Joystick
from Snow import Snow

def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)

def main():
    rand = random.randint(20, 50)
    count = 0
    fnt = ImageFont.truetype("/home/jeon7263/game/game/res/hi.ttf", 15)
    enemy_path = '/home/jeon7263/game/game/res/gstand.png'
    enemyslow_path = '/home/jeon7263/game/game/res/ghit.png'
    enemydie_path = '/home/jeon7263/game/game/res/gdead.png'
    player_path = '/home/jeon7263/game/game/res/rstand.png'
    playerslow_path = '/home/jeon7263/game/game/res/rplayerhit.png'
    playerdead_path = '/home/jeon7263/game/game/res/rdead.png'
    background_path = '/home/jeon7263/game/game/res/background.gif'
    snow_path = '/home/jeon7263/game/game/res/snow.png'
    lose_path = '/home/jeon7263/game/game/res/lose.gif'
    win_path = '/home/jeon7263/game/game/res/win.png'
    joystick = Joystick()
    character = Character(joystick.width, joystick.height)

    image = Image.new("RGB", (joystick.width, joystick.height))
    draw = ImageDraw.Draw(image)
    start = Image.open("/home/jeon7263/game/game/res/start.jpeg").resize((240, 240))
    backgroundImage = Image.open(background_path).resize((240, 240))
    startdraw = ImageDraw.Draw(start)
    startdraw.text((25,90),'Press A button to start!',(0,0,0), font = fnt)
    playerImage = Image.open(player_path).resize((20,20))
    playerslowImage = Image.open(playerslow_path).resize((20,20))
    playerdeadImage = Image.open(playerdead_path).resize((20,20))
    enemyImage = Image.open(enemy_path).resize((20,20))
    enemyslowImage = Image.open(enemyslow_path).resize((20,20))
    enemydieImage = Image.open(enemydie_path).resize((20,20))
    snowImage = Image.open(snow_path).resize((10,10))

    player = Character(joystick.width, joystick.height)
    positionXIndex = [rand, rand+40, rand+80, rand+120]
    enemy1 = Enemy((positionXIndex[0], -20))
    enemy2 = Enemy((positionXIndex[1], -20))
    enemy3 = Enemy((positionXIndex[2], -20))
    enemy4 = Enemy((positionXIndex[3], -20))

    enemys_list = [enemy1, enemy2, enemy3, enemy4]
    character_list = [player]
    bullets = []
    snows = []
    pressed = False
    joystick.disp.image(start)

    def Win():
        ending = Image.open(win_path).resize((240, 240))
        endingdraw = ImageDraw.Draw(ending)
        endingdraw.text((90,110),'YOU WIN!',(0,0,0), font = fnt)
        joystick.disp.image(ending)
        time.sleep(3)
        restart()

    def Lose():
        ending = Image.open(lose_path).resize((240,240)).convert("RGB")
        endingdraw = ImageDraw.Draw(ending)
        endingdraw.text((75,110),'YOU LOSE!',(0,0,0), font = fnt)
        joystick.disp.image(ending)
        time.sleep(3)
        restart()

    joystick.button_A_prev = False

    while True:  
        if not joystick.button_A.value:
            pressed=True
        elif joystick.button_A.value and pressed:
            pressed=False
            break

    while True:
        command = {'move': False, 'up_pressed': False , 'down_pressed': False, 'left_pressed': False, 'right_pressed': False}
        
        if not joystick.button_U.value:
            command['up_pressed'] = True
            command['move'] = True

        if not joystick.button_D.value:  
            command['down_pressed'] = True
            command['move'] = True

        if not joystick.button_L.value: 
            command['left_pressed'] = True
            command['move'] = True

        if not joystick.button_R.value:
            command['right_pressed'] = True
            command['move'] = True

        if not joystick.button_A.value:
            count = count + 1
        
        if not joystick.button_B.value and count > 0 and (not joystick.button_R.value or not joystick.button_L.value or not joystick.button_U.value or not joystick.button_D.value):
            bullet = Bullet(player.center, command)
            bullets.append(bullet)
            count = 0
            

        for bullet in bullets:
            bullet.collision_check(enemys_list.copy())
            bullet.move()
    
        for snow in snows:
            snow.collision_check(character_list.copy())
            snow.move()

        image.paste(backgroundImage, (0,0))

        for enemy in enemys_list:
            if enemy.hp == 2:
                image.paste(enemy.drawmob, (enemy.position[0], enemy.position[1]))
                enemy.move()
                snow = enemy.throw_snow()
                if snow:
                    snows.append(snow)

            if enemy.hp == 1:
                image.paste(enemy.drawslow,(enemy.position[0], enemy.position[1]))
                enemy.move2()
                snow = enemy.throw_snow()

                if snow:
                    snows.append(snow)

            if enemy.hp == 0:
                image.paste(enemy.drawdie,(enemy.position[0], enemy.position[1]))

        for player in character_list:
            if player.hp == 2:
                image.paste(player.drawplayer, (player.position[0], player.position[1]))
                player.move(command)
        
            if player.hp == 1:
                image.paste(player.drawplayerhit, (player.position[0], player.position[1]))
                player.move2(command)

            if player.hp == 0:
                image.paste(player.drawplayerdead, (player.position[0], player.position[1]))

        if all(enemy.hp == 0 for enemy in enemys_list):
            Win()

        if all(character.hp == 0 for character in character_list):
            Lose()

        for bullet in bullets:
            if bullet.state != 'hit':
                bullet_image = Image.open(snow_path).resize((10, 10))
                image.paste(bullet_image, (int(bullet.position[0]), int(bullet.position[1]))) 
       
        
        for snow in snows:
            if snow.state != 'hit':
                snow_image = Image.open(snow_path).resize((10, 10))
                image.paste(snow_image, (int(snow.position[0]), int(snow.position[1]))) 
        joystick.disp.image(image)      

if __name__ == '__main__':
    main()
