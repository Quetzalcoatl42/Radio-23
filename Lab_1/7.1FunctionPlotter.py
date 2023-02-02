import numpy as np
import matplotlib.pyplot as plt
data = np.load('DSB600-570.npy') #Insert Data File Name

print(data.size) #Should be 2048

time=np.arange(0,len(data[0])/2.2e6,1/2.2e6) #2.2e6 Sample Rate

plt.plot(time[0:100],data[0][0:100], color='black') #Create Plot ADD X-AXIS & LABELS

plt.title('My title')
plt.xlabel('Seconds [s]')
plt.ylabel('Volts [V]')
plt.title('Waveform of 600-570 KHz DSB Wave')

#Ammedment 1