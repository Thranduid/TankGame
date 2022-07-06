class MainGame():
    
    def __init__(self) -> None:
        pass

    #
    def startGame(self):
        pass

    def endGame(self):
        pass

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