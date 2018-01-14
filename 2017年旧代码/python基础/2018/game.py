import pygame
#开始
pygame.init()
#display(窗口)类 游戏代码
#set_mode() 方法  初始化我们的显示窗口
#updata()  方法 刷新我们的屏幕
hero_rect = pygame.Rect(217,700,46,57)
screen = pygame.display.set_mode((480,700))
#image.load
#步骤一，加载图片数据
bg = pygame.image.load('/home/tianjing/桌面/nmyj/images/background.png')
#步骤二，绘制图片数据
screen.blit(bg,(0,0))
#步骤三，更新显示
pygame.display.update()

#步骤一，加载图片数据
hero = pygame.image.load('/home/tianjing/桌面/nmyj/images/me1.png')
#步骤二，绘制到屏幕上
screen.blit(hero,(200,570))
#步骤三，更新屏幕显示
pygame.display.update()
zidan = pygame.image.load('/home/tianjing/桌面/nmyj/images/enemy2.png')
#二、绘制到屏幕上
screen.blit(zidan,(240,500))
#三、更新屏幕显示
pygame.display.update()

#游戏时钟
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('退出游戏') 
            pygame.quit()
            exit()
    hero_rect.y -= 1
    if hero_rect.bottom <= 0:
        hero_rect.y = 700
    screen.blit(bg,(0,0))
    screen.blit(hero,hero_rect)
    pygame.display.update()
class GameSprite(pygame.sprite.Sprite) :
    '''精灵类''' 
    def __init__(self,image_name,speed = 1):
        #调用父类的初始化方法
        super().__init__()
        #加载图像
        self.image = self.image.load(image_name)
        #设置尺寸
        self.rect = self.image.get_rect()
        #记录速度
        self.speed = speed
    def update(self,*args):
        #默认再垂直方向移动
        self.rect.y += self.spend




#结束
pygame.quit()


