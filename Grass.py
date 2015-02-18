from __future__ import division
from panda3d.core import LODNode, NodePath,VBase4
from random import random

import colorsys

class GrassBlade(NodePath):
    def __init__(self,randomScale=True,randomColor=True,scaleFactor=0.4,baseColor=VBase4(230/255,245/255,175/255,1)):
        NodePath.__init__(self,LODNode("Grass"))
        self.lod0=base.loader.loadModel("3d/grass")
        self.lod0.reparentTo(self)
        self.node().addSwitch(9999,0)
        if randomScale:
            self.setScale(scaleFactor+(random()/5))
        else: self.setScale(scaleFactor)
        color=baseColor
        if randomColor:
            hsvT=colorsys.rgb_to_hsv(color.getX(),color.getY(),color.getZ())
            hsv=list(hsvT)
            hsv[1]=hsv[1]+random()/4
            #hsv[0]=hsv[0]-random()/5
            hsv=colorsys.hsv_to_rgb(hsv[0],hsv[1],hsv[2])
            color=VBase4(hsv[0],hsv[1],hsv[2],1)
        self.lod0.setColorScale(color)