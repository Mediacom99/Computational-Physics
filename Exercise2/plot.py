import matplotlib.pyplot as plt 
import numpy as np

 

x = np.genfromtxt("data.txt", delimiter=',',dtype=int, usecols=1)
y = np.genfromtxt("data.txt", delimiter=',',dtype=float, usecols=0) 


#yver = np.zeros(len(y), dtype=float);
#TICKS = np.zeros(950, dtype=float)
#counter = 0.005
#for i in range(len(TICKS)):
#	TICKS[i]+=counter
#	counter+=0.005
#for i in range(len(yver)):
#	yver[i] = np.absolute(y[i] - np.pi*np.pi/6.0)

#print(x)
#print(yver)



plt.style.use('_mpl-gallery')


fig, ax = plt.subplots()
plt.tight_layout() #fai in modo che il grafico si centri bene nella figura
fig.set_size_inches(30/2.54, 30/2.54)


ax.scatter(x,y, s=12, c="purple")


ax.set_xlabel("n of " + r'$\phi_{1}^n$')
ax.set_ylabel(r'$\Delta_n = |\chi_n - \phi_{1}^n|$')
ax.set_title("Esercizio 2, precisione singola")
ax.set_xticks(x)
#ax.set_xscale('log')

#ax.plot(x, yver)
ax.set(xlim=(np.amin(x), np.amax(x)), ylim=(np.amin(x),np.amax(y) + np.amax(y)/4))

plt.show()