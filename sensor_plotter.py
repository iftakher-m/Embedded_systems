import matplotlib.pyplot as plt
import numpy as np

def ab(arr,i):
    return slice(sum(arr[0:i]),sum(arr[0:i+1]))

PATH = "../build-SITL_Simulator-Desktop_arm_darwin_generic_mach_o_32bit-Debug/"
f = open(PATH + "sensors.txt", "r")

header = f.readline().split(' ')

data = []
for line in f:
	data.append(line.strip().split(' '))
	#print(line)

f.close()
#Process header
t_step = float(header[0])
N = len(data)
t_end = t_step*N
idxs = [int(x) for x in header[1:]]

acc  = np.zeros((N,idxs[0]))
gyro = np.zeros((N,idxs[1]))
gps  = np.zeros((N,idxs[2]))
yaw  = np.zeros((N,idxs[3]))

for i,line in enumerate(data):
	acc[i,:]  = line[ab(idxs,0)]
	gyro[i,:] = line[ab(idxs,1)]
	gps[i,:]  = line[ab(idxs,2)]
	yaw[i,:]  = line[ab(idxs,3)]

T = np.linspace(0,t_end,N)

fig, ax = plt.subplots()
ax.plot(T,acc[:,0],T,acc[:,1],T,acc[:,2])

fig, ax = plt.subplots()
ax.plot(T,gyro[:,0],T,gyro[:,1],T,gyro[:,2])

fig, ax = plt.subplots()
ax.plot(T,gps[:,0],T,gps[:,1],T,gps[:,2])

fig, ax = plt.subplots()
ax.plot(T,yaw[:,0])

plt.show()
