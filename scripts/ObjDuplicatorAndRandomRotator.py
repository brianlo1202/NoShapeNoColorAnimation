#make many instances of selected object in cube area, rot in Y axis randomly 
#and rotate in local z axis in random direction
#

#NOT DONE!!!

import maya.cmds as cmds
import random

numDuplicates = 128;
maxYRotation = 60;
sideLenOfBoxBoundary = 4;
framesFor1Rot = 60; #slowest rot
rotSpeed = 0.4


def duplicateOnce(objToDup):

    duplicatedObj = cmds.duplicate(objToDup, rr = True);
    
    randomTranslateX = random.uniform(-sideLenOfBoxBoundary/2.0,sideLenOfBoxBoundary/2.0);
    randomTranslateY = random.uniform(-sideLenOfBoxBoundary/2.0,sideLenOfBoxBoundary/2.0);
    randomTranslateZ = random.uniform(-sideLenOfBoxBoundary/2.0,sideLenOfBoxBoundary/2.0);
        
    cmds.move(randomTranslateX, randomTranslateY, randomTranslateZ, duplicatedObj);
    
    #keyframe 360 in z
    cmds.currentTime( 1, edit=True )
        
    cmds.setKeyframe( duplicatedObj, attribute='rotateX')
    cmds.setKeyframe( duplicatedObj, attribute='rotateY')
    cmds.setKeyframe( duplicatedObj, attribute='rotateZ')
    
    cmds.currentTime( framesFor1Rot, edit=True )
    
    randRotDirection = (random.randrange(2) * 2) - 1 # -1 or 1
    randRotSpeed = rotSpeed * random.uniform(1,2)
        
    cmds.rotate(0, 0, randRotDirection*randRotSpeed*360, duplicatedObj, relative=True);
        
    cmds.setKeyframe( duplicatedObj, attribute='rotateX')
    cmds.setKeyframe( duplicatedObj, attribute='rotateY')
    cmds.setKeyframe( duplicatedObj, attribute='rotateZ')
    
    #make linear tangets and forever
    cmds.selectKey(clear=True);
    
    cmds.selectKey(duplicatedObj, addTo=True, keyframe=True, time = (0,framesFor1Rot), attribute = 'rotateX');
    cmds.selectKey(duplicatedObj, addTo=True, keyframe=True, time = (0,framesFor1Rot), attribute = 'rotateY');
    cmds.selectKey(duplicatedObj, addTo=True, keyframe=True, time = (0,framesFor1Rot), attribute = 'rotateZ');
    
    cmds.keyTangent(itt = 'linear', ott = 'linear');
    cmds.setInfinity(poi = 'cycleRelative');
    
    #parent and rotate in y axis
    group = cmds.group(duplicatedObj, n = "knifeRotator")
    randomRotY = random.uniform(-maxYRotation,maxYRotation);
    cmds.rotate(0, randomRotY, 0, group);

objToDup = cmds.ls( selection=True )[0];

for i in range(numDuplicates):
    duplicateOnce(objToDup)








