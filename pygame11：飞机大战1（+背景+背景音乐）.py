from pygame.locals import *
from random import *
import traceback
import tkinter as tk
import pygame
import math
import sys

def main() :
    pygame.init()   #初始化
    pygame.mixer.init()     #混音器初始化

    clock = pygame.time.Clock()     #设置一个计时器

    """载入音乐文件"""
    #背景音乐
    pygame.mixer.music.load(r"D:\Code\Python\Pygame\pygame11：飞机大战1\sound\game_music.ogg")  #设置背景音乐
    pygame.mixer.music.set_volume(1)  #设置音量

    #游戏音效
    bullet_music = r"D:\Code\Python\Pygame\pygame11：飞机大战1\sound\bullet.wav"  #子弹特效
    button_music = r"D:\Code\Python\Pygame\pygame11：飞机大战1\sound\button.wav"    #按键特效
    enemy1_down_music = r"D:\Code\Python\Pygame\pygame11：飞机大战1\sound\enemy1_down.wav"    #低等敌机被击毁音效
    enemy2_down_music = r"D:\Code\Python\Pygame\pygame11：飞机大战1\sound\enemy2_down.wav"    #中等敌机被击毁音效
    enemy3_down_music = r"D:\Code\Python\Pygame\pygame11：飞机大战1\sound\enemy3_down.wav"    #高等敌机被击毁音效
    enemy3_fly_music = r"D:\Code\Python\Pygame\pygame11：飞机大战1\sound\enemy3_flying.wav"    #高等敌机出现音效
    get_bomb_music = r"D:\Code\Python\Pygame\pygame11：飞机大战1\sound\get_bomb.wav"    #获得全屏炸弹补给音效
    get_bullet_music = r"D:\Code\Python\Pygame\pygame11：飞机大战1\sound\get_bullet.wav"    #获得双倍子弹补给音效
    me_down_music = r"D:\Code\Python\Pygame\pygame11：飞机大战1\sound\me_down.wav"    #自身飞机被击毁（死亡）音效
    supply_music = r"D:\Code\Python\Pygame\pygame11：飞机大战1\sound\supply.wav"    #补给产生音效
    upgrade_music = r"D:\Code\Python\Pygame\pygame11：飞机大战1\sound\upgrade.wav"    #升级音效
    use_bomb_music = r"D:\Code\Python\Pygame\pygame11：飞机大战1\sound\use_bomb.wav"    #使用全屏炸弹音效

    """图片文件路径"""
    again_image = r"D:\Code\Python\Pygame\pygame11：飞机大战1\images\again.png"   #重新开始图片路径
    background_image = r"D:\Code\Python\Pygame\pygame11：飞机大战1\images\background.png"  #背景图的路径
    
    #设置背景
    bg_size = width , height = 430 , 700       #背景大小
    screen = pygame.display.set_mode(bg_size)   #这是背景大小
    background = pygame.image.load(background_image).convert_alpha()       #画背景
    pygame.mixer.music.play(-1)     #播放背景音乐，-1 表示无限循环播放

    while True :
        for event in pygame.event.get() :
            if event.type == QUIT :
                sys.exit()
        
        screen.blit(background,(0,0))   #绘制背景
        

        pygame.display.flip()   #不停的刷新画面，不停的绘画

        clock.tick(60)     #设置帧率


if __name__ == "__main__":
    # 这样做的好处是双击打开时如果出现异常可以报告异常，而不是一闪而过！
    try:
        main()
    except SystemExit: #这是按下 × 的异常，直接忽略
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()