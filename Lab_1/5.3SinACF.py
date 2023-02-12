import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.ndimage import correlate

gs=['noise2048block1.npy']
for g in gs:

    data = np.load(g) #Insert Data File Name
    sample=np.arange(0,2048,1)
    noise=data
    
    #Build Plot
    data_ps =scipy.ndimage.correlate(data[0], data[0], mode="wrap")
    
    #Plot data
    plt.scatter(range(len(data_ps)), data_ps, label="Auto Correlate Function")


#Plotting
plt.xlabel('Samples')
plt.ylabel('Power proportional to [W/MHz]')

plt.title('ACF Power Spectrum for Various Block Size Averages')
plt.grid()
plt.legend()

plt.show()
