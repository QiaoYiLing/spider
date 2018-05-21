import time
import random
from pylibftdi import Device
from arm import Arm


class Control:
    def __init__(self):
        self.arm = Arm(2)
        self.pos_ini=[
            2000,2500,500,2500 , 1500,1500,1500,1500 , 1500,1500,1500,1500,   1000,2500,500,2500 , 1500,1500,1500,1500 , 1500,1500,1500,1500
        ]
        pass

    def straight(self):
        pass

    def ini(self):
        for i in range(12):
        	self.arm.set_position(i,1500)
        	self.arm.set_position(i+16,1500)

        	# another initial pose
            #self.arm.set_position(i,self.pos_ini[i])
            #self.arm.set_position(i+16,self.pos_ini[i+12])

if __name__ == '__main__':
    con = Control()
    con.ini()

    try:

        import sys
        while True:
            cmd = sys.stdin.readline()
            axis = int(cmd.split(' ')[0])
            pos = int(cmd.split(' ')[1])
            con.arm.set_position(axis, pos, 200)


            # if c == 'a':
            #     a[0] += 50
            #     con.arm.set_position(axis, pos, 200)
            # elif c == 'z':
            #     a[0] -= 50
            #     con.arm.set_position(num, a[0], 200)

    except KeyboardInterrupt as e:
        pass

