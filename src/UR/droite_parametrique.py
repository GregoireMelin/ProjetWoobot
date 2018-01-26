from math import pi
import numpy as np
from transforms3d.euler import euler2mat, mat2euler

import urx
import logging

def initPosition_test(rob):
    j_init = [-1.4503806273089808, -1.965510670338766, -0.8303797880755823, -1.8648479620562952, 1.5238507986068726, 0.8078446388244629]
    rob.movej(j_init,acc=a*5,vel=v*100)
    print rob.get_pose()
    return 1

def getJointParameters(rob):
    j = rob.getj()
    print "-- Angles des jointures en rad --"
    print "Base = ",j[0]
    print "Epaule = ", j[1]
    print "Coude = ", j[2]
    print "Poignet 1 = ", j[3]
    print "Poignet 2 = ", j[4]
    print "Poignet 3 = ", j[5]
    return j
# step : number of translation
def moveThroughParametricLine(rob,step, finalPosition, acceleration,velocity):
    # -- Defining line with parametric equation
    initPose = rob.get_pose()
    initPosition = initPose.pos
    coefficients = finalPosition.pos.copy() #il faut cloner le tableau
    coefficients[0]=(coefficients[0]-initPosition[0])/step
    coefficients[1]=(coefficients[1]-initPosition[1])/step
    coefficients[2]=(coefficients[2]-initPosition[2])/step
    print ""
    print ""
    # Affichage de l equation de la droite parametrique
    print "PARAMETRIC LINE EQUATION"
    print " x(t) = ",initPosition[0]," + ",coefficients[0]," *t"
    print " y(t) = ",initPosition[1]," + ",coefficients[1]," *t"
    print " z(t) = ",initPosition[2]," + ",coefficients[2],"*t"

    currentPosition=initPose

    print "------------"
    print "Initial Position : X = ",currentPosition.pos[0]," Y = ",currentPosition.pos[1]," Z = ",currentPosition.pos[2]
    print "------------"
    print ""
    print ""
    # -- Moving the robot

    for i in range(step):
        print "TRANSLATION ",i+1
        currentPosition.pos[0]=coefficients[0]+currentPosition.pos[0]#i*coef + initPosition
        currentPosition.pos[1]= coefficients[1]+currentPosition.pos[1]
        currentPosition.pos[2]=coefficients[2]+currentPosition.pos[2]
        print "Current Position : X = ",currentPosition.pos[0]," Y = ",currentPosition.pos[1]," Z = ",currentPosition.pos[2]
        rob.movel(currentPosition,acc=acceleration,vel=velocity)
    print ""
    print ""
    print "------------"
    print "Final Position :"
    print " X = ",currentPosition.pos[0]
    print "  expected : ",finalPosition.pos[0]
    print " Y = ",currentPosition.pos[1]
    print "  expected : ",finalPosition.pos[1]
    print " Z = ",currentPosition.pos[2]
    print "  expected : ",finalPosition.pos[2]
    print "------------"

    return 1


if __name__ == "__main__":
    #Initialisation des variables
    rob = urx.Robot("192.168.1.196")
    rob.set_tcp((0,0,0,0,0,0))
    rob.set_payload(0.5, (0,0,0))

    try:
        l = 0.05
        v = 0.2 #0.05
        a = 0.3
        initPosition_test(rob)
        #getJointParameters(rob)


        #Move through lines : (tested by pushing a box)
        #current_pose = rob.get_pose()
        #current_pose.pos[2]=0.02
        #moveThroughParametricLine(rob,1, current_pose, a,v)
        #current_pose.pos[0]=0.2
        #moveThroughParametricLine(rob,1, current_pose, a,v)

        current_pose = rob.get_pose()
        current_pose.pos[0]=0.3
        current_pose.pos[1]=0.1
        current_pose.pos[2]=0.4

        rob.movep(current_pose,a,v, 10)
        a = rob.get_pose()
        print a.pos




    finally:
        rob.close()
