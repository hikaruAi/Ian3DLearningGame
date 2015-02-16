from HPanda.HPlayer import HPlayer
from HPanda.HCameras import ThirdPersonCamera
from HJoystick import HJoyKeySensor, mappingDict
from panda3d.core import Vec3

from HPanda.HState import HState, HStateManager


class Ian(HPlayer):
    def __init__(self, scene, x=0, y=0, z=0):
        animations = {"iddle": "3d/Ian-iddle",
                      "jump": "3d/Ian-jump",
                      "run": "3d/Ian-run",
                      "saludo": "3d/Ian-saludo"}
        HPlayer.__init__(self, scene.name + "_Ian", scene, "3d/Ian", "3d/ianCollision", animations, margin=.01)
        self.setPos(scene.render, x, y, z)
        self.camera = ThirdPersonCamera(self.scene, self.actor, .3, x, y + 2, z + .7, speed=3)
        self.setEvents()
        self.setStates()
        self.walkSpeed = 50
        self.runFactor = 1
        # base.taskMgr.add(self._onFrameTask,self.name+"_onFrameTask")

    def setStates(self):
        self.stateManager = HStateManager(self.scene.Base, self.name + "_stateManager")
        self.iddle_state = HState("iddle", self._iddle_onInit, self._iddle_onFrame, self._iddle_onExit,
                                  self._iddle_condition)
        self.stateManager.addState(self.iddle_state)
        self.run_state = HState("run", self._run_onInit, self._run_onFrame, self._run_onExit, self._run_condition)
        self.stateManager.addState(self.run_state)
        self.jump_state = HState("jump", self._jump_onInit, self._jump_onFrame, self._jump_onExit, self._jump_condition)
        self.stateManager.addState(self.jump_state)
        self.stateManager.setState("iddle")

    # Jump
    def _jump_onInit(self):
        self.actor.play("jump")
        self.stopMov()

    def _jump_onFrame(self):
        frame = int(self.actor.getCurrentFrame("jump"))
        if frame == 15:
            self.body.setMaxJumpHeight(2)
            self.body.setJumpSpeed(4)
            self.body.doJump()
        if int(self.actor.getNumFrames("jump") == frame) and self.body.isOnGround():
            self.stateManager("iddle")
        elif self.body.isOnGround():
            self.stateManager("iddle")

    def _jump_onExit(self):
        self.actor.stop("jump")

    def _jump_condition(self):
        return self.body.isOnGround()

    # Run
    def _run_onInit(self):
        self.actor.loop("run")

    def _run_onFrame(self):
        self.body.setLinearMovement(Vec3(0, -self.walkSpeed * self.runFactor, 0) * globalClock.getDt(), True)
        self.actor.setPlayRate(self.runFactor, "run")

    def _run_onExit(self):
        self.stopMov()
        self.actor.stop("run")

    def _run_condition(self):
        return self.body.isOnGround()

    # #IDDLE
    def _iddle_onInit(self):
        self.actor.loop("iddle")
        self.stopMov()

    def _iddle_onFrame(self):
        #self.stopMov()
        pass

    def _iddle_onExit(self):
        self.actor.stop("iddle")

    def _iddle_condition(self):
        return self.body.isOnGround()

    def setEvents(self):
        mapping = dict(mappingDict)
        self.joystickSensor = HJoyKeySensor(mapping, 0)
        base.accept(self.joystickSensor.axisDownEventName + "1", self._onAxis1Down)
        base.accept(self.joystickSensor.axisUpEventName + "1", self._onAxis1Up)
        base.accept(self.joystickSensor.axisEventName + "1", self._onAxis1Frame)
        base.accept(self.joystickSensor.buttonDownEventName+"0",self._onButton0Down)

    def _onButton0Down(self):
        self.stateManager("jump")

    def _onAxis1Frame(self, v):
        if v != 0: self.runFactor = v

    def _onAxis1Up(self):
        self.stateManager("iddle")

    def _onAxis1Down(self, v):
        self.runFactor = v
        self.stateManager("run")

    ##
    def stopMov(self):
        self.body.setLinearMovement(Vec3(), True)