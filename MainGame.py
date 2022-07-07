import sys
import pygame


class Tank():

    def __init__(self, left, top) -> None:

        # tank的四个方向的图片
        self.images = {

            # 从磁盘加载图片
            'U': pygame.image.load('src\plane_U.png'),
            'D': pygame.image.load('src\plane_D.png'),
            'L': pygame.image.load('src\plane_L.png'),
            'R': pygame.image.load('src\plane_R.png')
        }

        # 坦克的方向
        self.direction = 'U'
        # 根据坦克的方向选择加载对应的图片
        self.image = self.images[self.direction]
        # 坦克所在的区域
        self.rect = self.image.get_rect()
        # 指定坦克初始化位置 分别距离x轴和y轴的点 默认值为0，0
        self.rect.left = left
        self.rect.top = top
        self.speed = 2
        self.stop = True

    def move(self):
        # 判断移动的方向
        if self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
                print('top: '+str(self.rect.top)+' left: '+str(self.rect.left))
                print('bottom: '+str(self.rect.bottom) +
                      ' right: '+str(self.rect.right))
            else:
                print('已经达到上边界')
        elif self.direction == 'D':
            if self.rect.top + self.rect.width < MainGame.window.get_width():
                self.rect.top += self.speed
                print('top: '+str(self.rect.top)+' left: '+str(self.rect.left))
                print('bottom: '+str(self.rect.bottom) +
                      ' right: '+str(self.rect.right))
            else:
                print('已经达到下边界')
        elif self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
                print('top: '+str(self.rect.top)+' left: '+str(self.rect.left))
                print('bottom: '+str(self.rect.bottom) +
                      ' right: '+str(self.rect.right))
            else:
                print('已经达到左边界')
        elif self.direction == 'R':
            if self.rect.left + self.rect.height < MainGame.window.get_height():
                self.rect.left += self.speed
                print('top: '+str(self.rect.top)+' left: '+str(self.rect.left))
                print('bottom: '+str(self.rect.bottom) +
                      ' right: '+str(self.rect.right))
            else:
                print('已经达到右边界')
        else:
            print('请使用上下左右键进行控制坦克的移动')

    def shot(self):
        pass

    def display(self):
        # 将tank 加载到表面
        # 重新设置图片
        self.image = self.images[self.direction]
        # 重新加载图片
        MainGame.window.blit(self.image, self.rect)


class MyTank(Tank):
    def __init__(self) -> None:
        super().__init__()


class EnemyTank(Tank):

    def __init__(self) -> None:
        super().__init__()


class Bullet():

    def __init__(self) -> None:
        pass

    def move(self):
        pass

    def display(self):
        pass


class Explode():

    def __init__(self) -> None:
        pass

    def displayExplode(self):
        pass


class Wall():

    def __init__(self) -> None:
        pass

    def displayWall(self):
        pass


class Music():
    def __init__(self) -> None:
        pass

    def playMusic(self):
        pass


class MainGame():

    HEIGHT = 600
    WIDTH = 600
    FPS = 30
    RUNNING = True
    window = None
    Tank_P1 = None

    # 初始化
    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

    # 开始游戏
    def startGame(self):

        # 设置屏幕大小
        MainGame.window = pygame.display.set_mode(
            (MainGame.HEIGHT, MainGame.WIDTH))
        pygame.display.set_caption('坦克大战v1.0')
        MainGame.Tank_P1 = Tank(230, 450)
        while MainGame.RUNNING:

            # 将窗口背景填充为背景色，如不填充会出现移动飞机时出现残影
            MainGame.window.fill(pygame.Color(0, 0, 0))

            # 加载坦克
            MainGame.Tank_P1.display()

            # 监听事件
            self.getEvent()

            # 坦克持续移动
            if not MainGame.Tank_P1.stop and MainGame.Tank_P1:
                MainGame.Tank_P1.move()

            # 判断字体模块是否初始化成功
            if pygame.font.get_init():
                # 字体初始化成功，则将字体小面板绘制在window上
                MainGame.window.blit(self.fontTips(
                    "The number of tanks remaining: %d" % 5), (5, 5))
            else:
                # 字体初始化失败，则terminal输出提示
                print("字体初始化失败！")

            # 刷新屏幕
            pygame.display.update()

    # 获取程序运行期间所有事件

    def getEvent(self):

        # 获取pygame的全部事件队列，get()返回一个List
        eventList = pygame.event.get()

        # 使用for循环遍历事件队列
        for event in eventList:

            # 判断事件的类型是否是退出
            if event.type == pygame.QUIT:

                # 推出则调用类内方法，退出
                self.endGame()

            # 继续判断事件的类型是否是按下按键 如是，则继续判断按下的事件类型
            elif event.type == pygame.KEYDOWN:
               # 判断是否按下键盘的q键
                if event.key == pygame.K_LEFT:
                    print("go Left")
                    MainGame.Tank_P1.direction = 'L'
                    MainGame.Tank_P1.stop = False
                elif event.key == pygame.K_RIGHT:
                    print("go right")
                    MainGame.Tank_P1.direction = 'R'
                    MainGame.Tank_P1.stop = False
                elif event.key == pygame.K_UP:
                    print("go up")
                    MainGame.Tank_P1.direction = 'U'
                    MainGame.Tank_P1.stop = False
                elif event.key == pygame.K_DOWN:
                    print("go down")
                    MainGame.Tank_P1.direction = 'D'
                    MainGame.Tank_P1.stop = False
                elif event.key == pygame.K_SPACE:
                    print("shot")
                else:
                    print("please input again")
            elif event.type == pygame.KEYUP:
                MainGame.Tank_P1.stop = True

    # 剩余坦克的数量和获得的积分的字体

    def fontTips(self, text):

        # 选中一个字体模块
        myFont = pygame.font.SysFont('laoui', 30)

        # 设置字体的位置

        # 绘制一个字体
        fonttips = myFont.render(text, True, pygame.Color(
            240, 248, 255), pygame.Color(0, 0, 0))
        return fonttips

    # 结束游戏

    def endGame(self):

        # 关闭
        MainGame.RUNNING = False
        pygame.quit()
        sys.exit()


MainGame().startGame()
