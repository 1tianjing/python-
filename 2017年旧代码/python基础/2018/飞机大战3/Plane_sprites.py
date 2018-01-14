import pygame


#游戏屏幕的大小
SCREEN_RECT = pygame.Rect(0,0,480,700)

class GameSprite(pygame.sprite.Sprite):
    """基类"""
    def __init__(self,image_url,speed = 1):
        #调用父类的初始化方法
        super().__init__()
        self.image_url = pygame.image.load(image_url)
        self.speed = speed
        self.rect = self.image_url.get_rect()

    def update(self):
        self.rect.y += self.speed


class Hero(GameSprite):
    '''英雄类'''
    def __init__(self,image_url,speed = 0):
        super().__init__(image_url,speed)


    def update(self):
        pass


class Background(GameSprite):
    '''背景类'''
    def __init__(self,image_url,speed = 1):
        super().__init(image_url,speed)
  

    def update(self):
        pass















