import numpy as np
import matplotlib.pyplot as plt
data = np.load('data3n_fft.npy') #Insert Data File Name

print(data.size) #Should be 2048

plt.plot(data[0]) #Create Plot

plt.title('My title')
plt.xlabel('categories')
plt.ylabel('values')

plt.show()
#Ammedment