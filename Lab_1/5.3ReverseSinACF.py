# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 21:42:26 2023

@author: 05pat
"""

import numpy as np
import matplotlib.pyplot as plt


gs=['noise2048block1.npy']
for g in gs:

    data = np.load(g) #Insert Data File Name
    noise=data
    
    #Build Plot
    
    data_fft = ((abs(np.fft.fft(data)))**2) #Fourier Transform #??? **2 & abs
    idata_ffot=np.fft.fftshift(np.fft.ifft(data_fft))
    


    #Plot data
    plt.scatter(range(len(idata_ffot[0])), idata_ffot[0], label="Inverse Power Spectrum")



#Plotting

plt.xlabel('Frequency [MHz]')
plt.ylabel('Power proportional to [W/MHz]')
plt.title('ACF Power Spectrum for Various Block Size Averages')
plt.grid()
plt.show()
