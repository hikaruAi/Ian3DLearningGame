from HPanda.HPlayer import HPlayer
from HPanda.HCameras import ThirdPersonCamera
from HJoystick import HJoyKeySensor, mappingDict
from panda3d.core import Vec3

from HPanda.HState import HState,HStateManager


class Ian(HPlayer):
    def __init__(self, scene, x=0, y=0, z=0):
        animations = {"iddle": "3d/Ian-iddle", "jump":"3d/Ian-jump","run":"3d/Ian-run","saludo":"3d/Ian-saludo"}
        HPlayer.__init__(self, scene.name + "_Ian", scene, "3d/Ian", "3d/ianCollision", animations, margin=.01)
        self.setPos(scene.render, x, y, z)
        self.camera = ThirdPersonCamera(self.scene, self.actor, .3, x, y + 2, z + .7, speed=3)
        self.setEvents()
        self.setStates()
        self.walkSpeed = 50
        # base.taskMgr.add(self._onFrameTask,self.name+"_onFrameTask")

    def setStates(self):
        self.stateManager=HStateManager(self.scene.Base,self.name+"_stateManager")
        self.iddle_state=HState("iddle",self._iddle_onInit,self._iddle_onFrame,self._iddle_onExit,self._iddle_condition)
        self.stateManager.addState(self.iddle_state)
        self.stateManager.setState("iddle")

    def _iddle_onInit(self):
        self.
    def setEvents(self):
        mapping = dict(mappingDict)
        self.joystickSensor = HJoyKeySensor(mapping, 0)