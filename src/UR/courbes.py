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
        v = 0.6#0.05
        a = 0.8
        initPosition_test(rob)
        pos_to=rob.get_pose()

        #pos_via=rob.get_pose()
        #pos_via.pos[0]=pos_via.pos[0]-0.05
        #pos_via.pos[1]=pos_via.pos[1]-0.05
        #pos_to.pos[0]=pos_to.pos[0]-0.02

        #rob.movec(pos_via,pos_to,a,v)

        #Move through lines : (tested by pushing a box)
        current_pose = rob.get_pose()
        current_pose.pos[2]=0.21 #Regle pour la table (0.17)
        moveThroughParametricLine(rob,1, current_pose, a,v)
        current_pose.pos[0]=0.5
        moveThroughParametricLine(rob,8, current_pose, a,v)
        initPosition_test(rob)
        print "Get force from effector : ", rob.get_tcp_force()


        print rob.getj()
        #j1=[-1.4557526747332972, -2.5017550627337855, -0.9440138975726526, -1.2093928495990198, 1.523707389831543, 0.8078206777572632]
        #rob.movej(j1,a,v)
        #j2=[-1.3762038389789026, -2.5017669836627405, -0.9440258185016077, -1.2093451658831995, 1.5236953496932983, 0.8078086972236633]
        #rob.movej(j2,a,v)
        #j3=[-1.306640926991598, -2.5018027464496058, -0.9440496603595179, -1.2093570868121546, 1.523719310760498, 0.8078206777572632]
        #rob.movej(j3,a,v)

    finally:
        rob.close()
