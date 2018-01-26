from math import pi
import numpy as np
from transforms3d.euler import euler2mat, mat2euler

import urx
import logging


if __name__ == "__main__":
    rob = urx.Robot("192.168.1.196")#("192.168.0.100")
    #rob = urx.Robot("localhost")
    rob.set_tcp((0,0,0,0,0,0))
    rob.set_payload(0.5, (0,0,0))
    try:
        l = 0.05
        v = 0.05
        a = 0.3
        j = rob.getj()
        print("Initial joint configuration is ", j)
        t = rob.get_pose()

        print("Transformation from base to tcp is: ", t)
        print("Translating in x")
        print t.pos[1]#pose_vector; t.orient pour orientation
        pose = t;
        pose.pos[1] = -0.10;
        print("Pause")
        print pose;
        #rob.movel(pose, acc=a, vel=v);
        pose.pos[1] = 0.10;
        #rob.movel(pose, acc=a, vel=v);

      	v= 0.07

      	print pose.orient[0];
      	pose_bis = (pose.pos[0],pose.pos[1],pose.pos[2],2.22,2.22,0)
      	rob.movel(pose_bis, acc=a, vel=v);
      	pose_bis = (pose.pos[0]+0.10,pose.pos[1],pose.pos[2],2.22,2.22,0)
      	rob.movel(pose_bis, v);
      	pose_bis = (pose.pos[0],pose.pos[1]+0.10,pose.pos[2],2.22,2.22,0)
      	rob.movel(pose_bis, acc=a, vel=v);
      	pose_bis = (pose.pos[0]-0.10,pose.pos[1],pose.pos[2],2.22,2.22,0)
      	rob.movel(pose_bis, acc=a, vel=v);
      	pose_bis = (pose.pos[0],pose.pos[1]-0.10,pose.pos[2],2.22,2.22,0)
      	rob.movel(pose_bis, acc=a, vel=v);

        #print "Array"
        #print pose.orient
        #print pose.orient[0]
        #print np.array(pose.orient)
        #euler = mat2euler([pose.orient[0],pose.orient[1],pose.orient[2]])
        #euler_deg = np.degrees(euler)
        #print euler_deg
        #euler vers mat

        #rob.translate((l, 0, 0), acc=a, vel=v)
        #pose = rob.getl()
        #print("robot tcp is at: ", pose)
        #print("moving in z")
        #pose[2] += l
        #rob.movel(pose, acc=a, vel=v)


        #print("Translate in -x and rotate")
        #t.orient.rotate_zb(pi/4)
        #t.pos[0] -= l
        #rob.set_pose(t, vel=v, acc=a)
        #print("Sending robot back to original position")
        #rob.movej(j, acc=0.8, vel=0.2)
    finally:
        rob.close()
