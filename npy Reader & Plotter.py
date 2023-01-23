import numpy as np
import matplotlib.pyplot as plt
data = np.load('g705.npy') #Insert Data File Name

print(data.size) #Should be 2048

time=np.arange(0,2048/3.2e6,1/3.2e6) #3.2e6 Sample Rate

plt.plot(time,data[0]) #Create Plot ADD X-AXIS & LABELS

plt.title('My title')
plt.xlabel('Seconds [s]')
plt.ylabel('Volts??? [V]')

plt.show()
#Ammedment