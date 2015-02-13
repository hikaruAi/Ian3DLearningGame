from HPanda.HPlayer import HPlayer
from HPanda.HCameras import ThirdPersonCamera
from HJoystick import HJoyKeySensor, mappingDict

class Ian(HPlayer):
    def __init__(self,scene,x=0,y=0,z=0):
        animations={"blank":"3d/Ian-blank"}
        HPlayer.__init__(self,scene.name+"_Ian",scene,"3d/Ian","3d/ianCollision",animations)
        self.setPos(scene.render,x,y,z)
        self.camera=ThirdPersonCamera(self.scene,self,.3,x,y+2,z+.7)
        self.setEvents()
    def setEvents(self):
        mapping=dict(mappingDict)
        self.joystickSensor=HJoyKeySensor(mapping,0)
        base.accept(self.joystickSensor.axisEventName+"1",self.axisHandler)
    def axisHandler(self,axisValue):
        print "Axis Vertical:",axisValue
