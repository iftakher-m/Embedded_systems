import matplotlib.pyplot as plt
import numpy as np

def ab(arr,i):
    return slice(sum(arr[0:i]),sum(arr[0:i+1]))
    
PATH = "../build-SITL_Simulator-Desktop_arm_darwin_generic_mach_o_32bit-Debug/"

f = open(PATH + "ekf.txt", "r")

header = f.readline().split(' ')

data = []
for line in f:
	data.append(line.split(' '))

f.close()

#Process header
t_step = float(header[0])
N = len(data)
t_end = t_step*N
idxs = [int(x) for x in header[1:]]

p = np.zeros((N,idxs[0]))
v = np.zeros((N,idxs[1]))
E = np.zeros((N,idxs[2]))
w = np.zeros((N,idxs[3]))

for i,line in enumerate(data):
	E[i,:] = line[ab(idxs,0)]
	w[i,:] = line[ab(idxs,1)]
	p[i,:] = line[ab(idxs,2)]
	v[i,:] = line[ab(idxs,3)]
#print(len(E),len(T))
T = np.linspace(0,t_end,N)

fig, ax = plt.subplots()
ax.plot(T,E[:,0],T,E[:,1],T,E[:,2])

fig, ax = plt.subplots()
ax.plot(T,w[:,0],T,w[:,1],T,w[:,2])

fig, ax = plt.subplots()
ax.plot(T,p[:,0],T,p[:,1],T,p[:,2])

fig, ax = plt.subplots()
ax.plot(T,v[:,0],T,v[:,1],T,v[:,2])


plt.show()
