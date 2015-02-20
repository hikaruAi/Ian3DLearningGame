from __future__ import division
from panda3d.core import LODNode, NodePath,VBase4
from random import random, choice

class GrassBlade(NodePath):
    def __init__(self,randomScale=True,randomColor=True,scaleFactor=0.1,baseColor=VBase4(230/255,245/255,175/255,1)):
        NodePath.__init__(self,LODNode("Grass"))
        self.lod0=base.loader.loadModel("3d/grass")
        self.lod0.reparentTo(self)
        self.node().addSwitch(10,0)
        if randomScale:
            self.setScale(.5,.5,scaleFactor+(random()/2))
        else: self.setScale(scaleFactor)
        colors=(baseColor,VBase4(252/255,244/255,88/255,1),VBase4(145/255,179/255,23/255,1),VBase4(44/255,179/255,23/255,1))
        self.lod0.setColorScale(choice(colors))