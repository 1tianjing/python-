#导入pygame这个包
import pygame

from Plane_sprites import *

class PlaneGame(object):
    """飞机大战主游戏"""
    def __init__(self):
        print('游戏初始化')
        #1、创建游戏窗口 pygame.display.set_mode 传高和宽，返回一个窗口
        #.size 取宽高    .x取x轴的值   .y取y轴的值  
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        #2、创建时钟 pygame.time.Clock  返回一个时钟对象
        self.clock = pygame.time.Clock()
        #3、调用私有方法，在里面创建精灵和精灵组
        self.__create_sprites()
        #设置定时器
        pygame.time.set_timer(CERATE_ENEMY_EVENT,1000)

        pygame.time.set_timer(HERO_FIRE_EVENT,500)
        
    def start_game(self):
        print('开始游戏')
        while True:
            #1、设置帧率
            self.clock.tick(60)


            #2、事件监听
            self.__event_hander()
            #3、碰撞检测
            self.__cheak_collide()
            #4、更新精灵组
            self.__update_sprites()
            #5、更新屏幕显示
            pygame.display.update()

    def __create_sprites(self):
        '''创建精灵和精灵组'''

        #pygame.back_group.Group()   可以创建一个精灵组  
        #背景精灵组
        bg1 = Backgroup('/home/tianjing/桌面/123/images/background.png')
        bg2 = Backgroup('/home/tianjing/桌面/123/images/background.png')



        bg2.rect.y = -bg2.rect.height
        self.back_group = pygame.sprite.Group(bg1,bg2)
        # 敌机精灵组
        self.enemy_group = pygame.sprite.Group()
        # 英雄精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)


    def __event_hander(self):
        '''事件监听的方法'''
        #pygame.event.get()  获取监听事件的列表
        #获取完列表  写一个for循环
        for event in pygame.event.get():
            #当列表里有pygame.QUIT这个值的时候，说明用户点了关闭按钮
            if event.type == pygame.QUIT:
                #调用静态私有方法
                PlaneGame.__game_over()
            elif event.type == CERATE_ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            #elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                #print('向右移动')       
            #另一种方法 返回所有按键的元组，如果某个按键按下


        key_pressed = pygame.key.get_pressed()

        if key_pressed[pygame.K_RIGHT]:
            print('向右边移动')
            self.hero.speed = 2        
        elif key_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
            print('向左边移动')
        else:
            self.hero.speed = 0
        
       
    def __update_sprites(self):
        '''更新精灵组'''
        self.hero_group.update()
        self.hero_group.draw(self.screen)

       
    def __cheak_collide(self):
        '''碰撞检测的方法'''

        # 1. 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)

        # 2. 敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)

        # 判断列表是否有内容
        if len(enemies) > 0:

            # 让英雄牺牲
            self.hero.kill()

            # 结束游戏
            PlaneGame.__game_over()

    def __update_sprites(self):
        '''更新精灵组'''
        for group in [self.back_group,self.enemy_group,self.hero_group,self.hero.bullets]:
            #更新精灵组里面所有精灵的位置
            group.update()
            #绘制到屏幕上
            group.draw(self.screen)

    @ staticmethod
    def __game_over():
        '''游戏结束的方法'''
        print('游戏结束')
        pygame.quit()
        exit()
#测试
if __name__ == "__main__":
    #1、创建游戏对象
        
    game = PlaneGame()
    game.start_game()

