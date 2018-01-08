from math import pi
import numpy as np
from transforms3d.euler import euler2mat, mat2euler
import urx
import logging

if __name__ == "__main__":
    rob = urx.Robot("192.168.1.196")
    rob.set_tcp((0,0,0,0,0,0))
    rob.set_payload(0.5, (0,0,0))
    try:
	print rob.x  # returns current x
	#rob.rx -= 0.1  # rotate tool around X axis
	#rob.z_t += 0.01  # move robot in tool z axis for +1cm

	#csys = rob.new_csys_from_xpy() #  generate a new csys from 3 points: X, origin, Y
	#rob.set_csys(csys)
    finally:
        rob.close()
