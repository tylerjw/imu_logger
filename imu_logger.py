import serial
import math
from pprint import pprint
import numpy as np 
import matplotlib.pyplot as plt
import pylab

def plot_euler(time, roll, pitch, yaw):
    """
    Plot Euler angles.
    Parameters
    ----------
    roll: array, deg
    yaw: array, deg
    pitch: array, deg
    """
    pylab.figure()
    pylab.subplot(311)
    pylab.plot(time, pitch,'r')
    pylab.xlabel('time (s)')
    pylab.ylabel('$\\theta$, deg')
    pylab.title('Pitch')
    pylab.grid(True)
    
    pylab.subplot(312)
    pylab.plot(time, yaw,'g')
    pylab.xlabel('time (s)')
    pylab.ylabel('$\\psi$,deg')
    pylab.title('Yaw')
    pylab.grid(True)
    
    pylab.subplot(313)
    pylab.plot(time, roll,'b')
    pylab.xlabel('time, s')
    pylab.ylabel('$\\gamma$,deg')
    pylab.title('Roll')
    pylab.grid(True)
    pylab.show()

def main():
	imu = serial.Serial('/dev/tty.usbmodem1412', 115200, timeout=2)
	# print imu.name
	yaw = []
	pitch = []
	roll = []
	time = []
	ts = 0

	while(True):
		try:
			line = imu.readline().strip().split()
			print line
			time.append(ts)
			roll.append(float(line[1]))
			pitch.append(float(line[2]))
			yaw.append(float(line[3]))
			ts += 1.0

		except (KeyboardInterrupt, SystemExit):
			imu.close()
			plot_euler(time, roll, pitch, yaw)
			raise

	imu.close()

if __name__ == '__main__':
	main()
