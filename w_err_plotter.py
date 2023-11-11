import matplotlib.pyplot as plt
import numpy as np

def ab(arr,i):
    return slice(sum(arr[0:i]),sum(arr[0:i+1]))

PATH = "../build-SITL_Simulator-Desktop_arm_darwin_generic_mach_o_32bit-Debug/"
f = open(PATH + "state.txt", "r")

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

w = np.zeros((N,idxs[0]))

for i,line in enumerate(data):
	
	w[i,:] = line[ab(idxs,0)]

    
#print(len(E),len(T))
T = np.linspace(0,t_end,N)

fig, ax = plt.subplots()
ax.plot(T,w[:,0],T,w[:,1],T,w[:,2])


plt.show()
