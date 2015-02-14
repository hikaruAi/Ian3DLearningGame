from HPanda.HScene import HScene
from HPanda.HGameObject import HDynamicObject
from Players import Ian
from panda3d.core import loadPrcFileData

assets="3d/"
windowTitle = "Loading..."
windowX = 640
windowY = 480
perpixelShading = False
showFPS = True
debugPhysics = True
debugView = False
debugLights = False
pauseKey = "p"
filters = False
bulletSteps = 10
pystats=False

# ####Preferences#####
loadPrcFileData("", "win-size " + str(windowX) + " " + str(windowY))
loadPrcFileData("", "window-title " + windowTitle)
loadPrcFileData("", "allow-incomplete-render 1")
# loadPrcFileData("", "bullet-solver-iterations " + str(bulletSteps))
if showFPS:
    loadPrcFileData("", "show-frame-rate-meter #t")
if pystats:
    loadPrcFileData("","want-pstats 1")
    loadPrcFileData("", "task-timer-verbose 1")
    loadPrcFileData("","pstats-tasks 1")


class Scene1(HScene):
    def __init__(self,showBase,name):
        HScene.__init__(self,showBase,physicsDebug=True,name=name)
        self.setPhysics()
        self.loadStatics()
        self.setPlayer()

    def setPlayer(self):
        self.player=Ian(self)
        self.player.reparentTo(self.render)

    def eggToStatic(self, egg, parent, margin=0.01, name="static"):
        global assets
        return HScene.eggToStatic(self,assets+egg,parent,margin,name)

    def loadStatics(self):
        self.piso=HDynamicObject("Piso",self,assets+"piso",assets+"piso",margin=0.05)