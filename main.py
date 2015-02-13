from HPanda.HGame import HGame
from Scenes import Scene1

#Globals
assets="3d/"

class MainGame(HGame):
    def __init__(self):
        HGame.__init__(self,title="Ian 3D learning game",posY=50, posX=50)
    def setup(self):
        self.currentScene=Scene1(self,"Scene1")

Game=MainGame()
Game.run()