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
import pygame

def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)

def main():
    count = 0
    paused = False
    pick_up_snow = False
    fnt = ImageFont.truetype("/home/jeon7263/game/game/res/hi.ttf", 15)
    fnt1 = ImageFont.truetype("/home/jeon7263/game/game/res/hi.ttf", 25)
    fnt2 = ImageFont.truetype("/home/jeon7263/game/game/res/hi.ttf", 20)
    enemy_path = '/home/jeon7263/game/game/res/gstand.png'
    enemyslow_path = '/home/jeon7263/game/game/res/ghit.png'
    enemydie_path = '/home/jeon7263/game/game/res/gdead.png'
    player_path = '/home/jeon7263/game/game/res/rstand.png'
    playerslow_path = '/home/jeon7263/game/game/res/rplayerhit.png'
    playerdead_path = '/home/jeon7263/game/game/res/rdead.png'
    playersnow_path = '/home/jeon7263/game/game/res/rplayersnow.png'
    background_path = '/home/jeon7263/game/game/res/background.gif'
    snow_path = '/home/jeon7263/game/game/res/snow.png'
    lose_path = '/home/jeon7263/game/game/res/lose.gif'
    win_path = '/home/jeon7263/game/game/res/win.png'
    joystick = Joystick()
    character = Character(joystick.width, joystick.height)
    joystick.button_B_prev = False
    image = Image.new("RGB", (joystick.width, joystick.height))
    draw = ImageDraw.Draw(image)
    start = Image.open("/home/jeon7263/game/game/res/start.jpeg").resize((240, 240))
    backgroundImage = Image.open(background_path).resize((240, 240))
    startdraw = ImageDraw.Draw(start)
    startdraw.text((30,105),'Press A button to start!',(0,0,0), font = fnt)
    playerImage = Image.open(player_path).resize((20,20))
    playerslowImage = Image.open(playerslow_path).resize((20,20))
    playerdeadImage = Image.open(playerdead_path).resize((20,20))
    playersnowImage = Image.open(playersnow_path).resize((20,20))
    enemyImage = Image.open(enemy_path).resize((20,20))
    enemyslowImage = Image.open(enemyslow_path).resize((20,20))
    enemydieImage = Image.open(enemydie_path).resize((20,20))
    snowImage = Image.open(snow_path).resize((10,10))

    stage = 1
    enemy_counts = {1: 4, 2: 6, 3: 8, 4: 10}

    def create_enemies(stage):
        enemies = []
        for i in range(enemy_counts[stage]):
            random_x = random.randint(20, 220)
            random_y = random.randint(20, 100)
            enemies.append(Enemy((random_x, random_y)))
        return enemies

    enemys_list = create_enemies(stage)

    player = Character(joystick.width, joystick.height)
    character_list = [player]
    bullets = []
    snows = []
    pressed = False
    joystick.disp.image(start)

    def stage_clear(stage):
        stage_clear = Image.open(background_path).resize((240,240)).convert("RGB")
        stage_cleardraw = ImageDraw.Draw(stage_clear)
        stage_cleardraw.text((70,110),f'Stage {stage} Clear!',(0,0,0), font = fnt)
        joystick.disp.image(stage_clear)
        time.sleep(3)

    def stage_start(stage):
        stage_start = Image.open(background_path).resize((240,240)).convert("RGB")
        stage_startdraw = ImageDraw.Draw(stage_start)
        stage_startdraw.text((70,110),f'Stage {stage} Start!',(0,0,0), font = fnt)
        joystick.disp.image(stage_start)
        time.sleep(2)

    def Win():
        ending = Image.open(win_path).resize((240, 240))
        endingdraw = ImageDraw.Draw(ending)
        endingdraw.text((70,105),'YOU WIN!',(0,0,0), font = fnt1)
        joystick.disp.image(ending)
        time.sleep(2)
        restart()

    def Lose():
        ending = Image.open(lose_path).resize((240,240)).convert("RGB")
        endingdraw = ImageDraw.Draw(ending)
        endingdraw.text((70,105),'YOU LOSE!',(0,0,0), font = fnt1)
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
            if not pick_up_snow:
                count = count + 1
                pick_up_snow = True
        else: 
            if pick_up_snow and count > 1:
                command = {'move': True, 'up_pressed': True , 'down_pressed': False, 'left_pressed': False, 'right_pressed': False}
                bullet = Bullet(player.center, command)
                bullets.append(bullet)
                count = 0

                pygame.mixer.init()
                pygame.mixer.music.load("/home/jeon7263/game/game/res/throw.wav")
                pygame.mixer.music.play(0)
            pick_up_snow = False

        if not joystick.button_B.value and joystick.button_B_prev:
            paused = not paused
            if paused:
                pause_image = image.copy() 
                pausedraw = ImageDraw.Draw(pause_image)
                pausedraw.text((100,90),'pause!',(0,0,0), font = fnt2)
                pausedraw.text((20,125), 'Press B to restart the game.',(0,0,0), font = fnt)
                joystick.disp.image(pause_image)
            else:
                joystick.disp.image(image)

        joystick.button_B_prev = joystick.button_B.value

        if paused:
            continue           

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
                random_snow = random.randint(1,30)
                if(random_snow == 1):
                    snow = enemy.throw_snow()
                    if snow:
                        snows.append(snow)

            if enemy.hp == 1:
                image.paste(enemy.drawslow,(enemy.position[0], enemy.position[1]))
                enemy.speed  = 3
                enemy.move()
                random_snow = random.randint(1,30)
                if(random_snow == 1):
                    snow = enemy.throw_snow()
                    if snow:
                        snows.append(snow)

            if enemy.hp == 0 and enemy.state != 'dead':
                enemy.state = 'dead'
                image.paste(enemy.drawdie,(enemy.position[0], enemy.position[1]))
                pygame.mixer.init()
                pygame.mixer.music.load("/home/jeon7263/game/game/res/dead.wav")
                pygame.mixer.music.play(0)              

        for player in character_list:
            if player.hp == 2 and count == 0:
                image.paste(player.drawplayer, (player.position[0], player.position[1]))
                player.move(command)

            if player.hp == 2 and count > 0:
                image.paste(player.drawplayersnow, (player.position[0], player.position[1]))
                player.move(command)

            if player.hp == 1 and count == 0:
                image.paste(player.drawplayerhit, (player.position[0], player.position[1]))
                player.speed = 3
                player.move(command)

            if player.hp == 1 and count > 0:
                image.paste(player.drawplayersnow, (player.position[0], player.position[1]))
                player.speed = 3
                player.move(command)           

            if player.hp == 0:
                image.paste(player.drawplayerdead, (player.position[0], player.position[1]))
                pygame.mixer.init()
                pygame.mixer.music.load("/home/jeon7263/game/game/res/dead.wav")
                pygame.mixer.music.play(0)


        if all(enemy.hp == 0 for enemy in enemys_list):
            stage_clear(stage)
            stage += 1
            if stage > 4:
                Win()

            else:
                enemys_list = create_enemies(stage)
                stage_start(stage)

        if all(character.hp == 0 for character in character_list):
            Lose()

        for bullet in bullets:
            if bullet.state != 'hit':
                bullet_image = Image.open(snow_path).resize((10, 10))
                image.paste(bullet_image, (int(bullet.position[0]), int(bullet.position[1]))) 
       
        
        for snow in snows:
            if snow.state != 'hit' and snow.position[1] < 245:
                snow_image = Image.open(snow_path).resize((10, 10))
                image.paste(snow_image, (int(snow.position[0]), int(snow.position[1]))) 
        joystick.disp.image(image)      

if __name__ == '__main__':
    main()
