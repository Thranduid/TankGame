# 初始化屏幕的长宽和帧率
from cmath import rect
from msvcrt import kbhit
import sys
import pygame




class MainGame():

    HEIGHT = 600
    WIDTH = 600
    FPS = 30
    RUNNING = True
    window = None

    
    #初始化
    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

    #开始游戏
    def startGame(self):
        
         # 设置屏幕大小
        MainGame.window = pygame.display.set_mode((MainGame.HEIGHT, MainGame.WIDTH))
        pygame.display.set_caption('坦克大战v1.0')
        while MainGame.RUNNING:
            
            #判断字体模块是否初始化成功
            if pygame.font.get_init():
                # 字体初始化成功，则将字体小面板绘制在window上
                MainGame.window.blit(self.fontTips("The number of tanks remaining: %d"%5),(5,5))
            else:
                # 字体初始化失败，则terminal输出提示
                print("字体初始化失败！")
            
            # 监听事件
            self.getEvent()

            # 刷新屏幕
            pygame.display.update()


    # 获取程序运行期间所有事件
    def getEvent(self):
        
        #获取pygame的全部事件队列，get()返回一个List
        eventList = pygame.event.get()

        #使用for循环遍历事件队列
        for event in eventList:

            #判断事件的类型是否是退出
            if event.type == pygame.QUIT:

                #推出则调用类内方法，退出
                self.endGame()
            
            #继续判断事件的类型是否是按下按键 如是，则继续判断按下的事件类型
            elif event.type == pygame.KEYDOWN:
               
               #判断是否按下键盘的q键
                if event.key == pygame.K_LEFT:
                    print("go Left")
                elif event.key == pygame.K_RIGHT:
                    print("go right")
                elif event.key == pygame.K_UP:
                    print("go up")
                elif event.key == pygame.K_DOWN:
                    print("go down")
                elif event.key == pygame.K_SPACE:
                    print("shot")
                else:
                    print("please input again")
    
    # 剩余坦克的数量和获得的积分的字体
    def fontTips(self, text):

        #选中一个字体模块
        myFont = pygame.font.SysFont('laoui',30)

        #设置字体的位置

        #绘制一个字体
        fonttips = myFont.render(text,True,pygame.Color(240, 248, 255),pygame.Color(0, 0, 0))
        return fonttips
        

    
    #结束游戏
    def endGame(self):
        
        #关闭
        MainGame.RUNNING = False
        pygame.quit()
        sys.exit()
    
        

class Tank():
    
    def __init__(self) -> None:
        pass

    def move(self):
        pass

    def shot(self):
        pass

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


MainGame().startGame()
