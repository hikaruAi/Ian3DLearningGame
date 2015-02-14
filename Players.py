from HPanda.HPlayer import HPlayer
from HPanda.HCameras import ThirdPersonCamera
from HJoystick import HJoyKeySensor, mappingDict
from panda3d.core import Vec3

class Ian(HPlayer):
    def __init__(self,scene,x=0,y=0,z=0):
        animations={"blank":"3d/Ian-blank"}
        HPlayer.__init__(self,scene.name+"_Ian",scene,"3d/Ian","3d/ianCollision",animations)
        self.setPos(scene.render,x,y,z)
        self.camera=ThirdPersonCamera(self.scene,self.actor,.3,x,y+2,z+.7)
        self.setEvents()
        #base.taskMgr.add(self._onFrameTask,self.name+"_onFrameTask")
    def _onFrameTask(self,t):
        self.body.setLinearMovement(Vec3(),True)
        return t.cont
    def setEvents(self):
        mapping=dict(mappingDict)
        self.joystickSensor=HJoyKeySensor(mapping,0)
        base.accept(self.joystickSensor.axisEventName+"1",self.axisHandler)
    def axisHandler(self,axisValue):
        dt=globalClock.getDt()
        if self.body.isOnGround():
            if axisValue>0:
                self.body.setLinearMovement(Vec3(0,-50,0)*dt,True)
            if axisValue==0:
                self.body.setLinearMovement(Vec3(),True)