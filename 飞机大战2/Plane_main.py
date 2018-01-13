import pygame

from Plane_sprites import *

class PlaneGame(object):
    '''飞机大战主程序类'''
    def __init__(self):
        print("游戏初始化")
        #1、创建一个游戏窗口 pygame.display.set_mode  传高和宽
        #.size  取宽高   .x取x轴的值   .y取y轴的值
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        #2、创建时钟  pygame.time.Clock  返回一个时钟对象
        self.clock = pygame.time.Clock()
        #3、调用私有方法   在里面创建精灵和精灵组
        self.__create_sprites()
        #4、设置定时器
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
        """创建精灵和精灵组"""
        bg1 = Backgroup('/home/tianjing/桌面/123/images/background.png')
        bg2 = Backgroup('/home/tianjing/桌面/123/images/background.png')
        bg2.rect.y = -bg2.rect.height
        self.back_group = pygame.sprite.Group(bg1,bg2)
        
        #敌机精灵组
        self.enemy_group = pygame.sprite.Group()
        #英雄精灵组
        self.hero = Hero()
        self.hero2 = Hero()
        self.hero_group = pygame.sprite.Group(self.hero,self.hero2)

    
    def __event_hander(self):
        '''事件监听的方法'''
        for event in pygame.event.get():
            #当列表里面有pygame.QUIT这个值的时候，说明用户点了关闭按钮
            if event.type == pygame.QUIT:
                #调用静态方法
                PlaneGame.__game_over()
            elif event.type == CERATE_ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
                self.hero2.fire()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.hero.fire()
                elif event.type == 271:
                    self.hero2.fire()

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[100]:
            self.hero2.speed = 2
        elif keys_pressed[97]:
            self.hero2.speed = -2
        elif keys_pressed[pygame.K_SPACE]:
            self.hero.fire()
        elif keys_pressed[271]:
            self.hero2.fire()
        else:
            self.hero2.speed = 0
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:   
            self.hero.speed = 0
    def __update_sprites(self):
        """更新精灵组"""
        self.hero_group.update()
        self.hero_group.draw(self.screen)

    
    def __cheak_collide(self):
        '''碰撞检测的方法'''
        #1、子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group, True, True)
        #2、敌机摧毁英雄
        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group, True)
        enemies1 = pygame.sprite.spritecollide(self.hero2,self.enemy_group, True)
        #判断列表是否有内容
        if len(enemies) > 0:
            #让英雄牺牲
            self.hero.kill()
            #结束游戏
            PlaneGame.__game_over()
    def __update_sprites(self):
        '''更新精灵组'''
        for group in [self.back_group,self.enemy_group,self.hero_group,self.hero.bullets]:
            #更新精灵组里面所有精灵的位置
            group.update()
            #绘制到屏幕上
            group.draw(self.screen)
            self.hero_group.update()
            self.hero_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)
    @staticmethod
    def __game_over():
        '''游戏结束的方法'''
        print('游戏结束')
        pygame.quit()
        exit()
#测试
if __name__ == "__main__":
    #创建游戏对象
    game = PlaneGame()
    game.start_game()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   


























