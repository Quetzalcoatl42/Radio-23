import numpy as np
import matplotlib.pyplot as plt



"""

#Print Information
print (data_file)
print ("Length Noise: ", len(noise))
print ("Mean: ", np.mean(data))
print ("Variance: ", np.var(data))
print ("Standard deviation: ", np.std(data))
"""

gs=['noise2048block1.npy','noise2048block4.npy', 'noise2048block16.npy','noise2048block50.npy']
for g in gs:

    data = np.load(g) #Insert Data File Name
    data=data-np.mean(data)
    noise=data
    
    #Build Plot
    data_fft = np.fft.fftshift((abs(np.fft.fft(data)))**2) #Fourier Transform #??? #FIXED BY ARON
    fft_freq = np.fft.fftshift(np.fft.fftfreq(len(noise[0]),1/2.2)) #!!! #FIXED BY ARON

    #Average of data
    data_fft=np.mean(data_fft,axis=0)

    #Plot data
    plt.plot(fft_freq,data_fft, label =g[14:-4] + " Block Average") #FFT
    plt.legend()


#Plotting

plt.xlabel('Frequency [MHz]')
plt.ylabel('Frequency Counts')
plt.ylim(10e-4, 10e1)
plt.title('Power Spectrum of Various Block Sizes')
plt.grid()
plt.yscale("log") #!!!

plt.show()
