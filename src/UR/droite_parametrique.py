from math import pi
import numpy as np
from transforms3d.euler import euler2mat, mat2euler

import urx
import logging

def initPosition(rob):
    j_init=[-2.6236677805529993, -2.213935677205221, -1.566683594380514, -0.8541472593890589, 1.5490251779556274, 0.5212509036064148]
    rob.movej(j_init,acc=a,vel=v)
    print rob.get_pose()
    return 1

def initPosition_test(rob):
    j_init = [-1.4503806273089808, -1.965510670338766, -0.8303797880755823, -1.8648479620562952, 1.5238507986068726, 0.8078446388244629]
    rob.movej(j_init,acc=a,vel=v)
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
        j_photo=[-2.583017889653341, -2.0957582632647913, -1.32068378130068, -0.39827186266054326, -0.14723378816713506, -0.6676643530475062]
        v = 0.1#0.05
        a = 0.1
        #initPosition_test(rob)

        rob.movej(j_photo,v*10,a*10)
        initPosition(rob)
        current_pose = rob.get_pose()
        current_pose.pos[1]=current_pose.pos[1]+0.7
        moveThroughParametricLine(rob,1, current_pose, a,v)
        initPosition_test(rob)
        # Robot en
        #<Transform:
        #<Orientation:
        #array([[ 0.90711834,  0.42026867,  0.0225957 ],
        #       [ 0.41473778, -0.88346468, -0.2179053 ],
        #       [-0.07161627,  0.20703719, -0.97570831]])>
        #<Vector: (-0.59372, 0.34843, 0.12286)>
        #>

    finally:
        rob.close()
