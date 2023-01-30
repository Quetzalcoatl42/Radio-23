
import numpy as np
import matplotlib.pyplot as plt

gs=['sin300.npy','sin500.npy','sin700.npy','sin900.npy', 'sin1100.npy', 'sin1300.npy', 'sin1500.npy']
for g in gs:

    data = np.load(g) #Insert Data File Name
    #Build Plot
    data_fft = (np.fft.fft(data)) #Fourier Transform
    fft_freq = np.fft.fftshift(np.fft.fftfreq(2048,1/2.2))

     
    
    
    plt.plot(fft_freq,data_fft[0], label = g[3:-4] + "KHz Wave") #FFT
    
    

plt.legend()
plt.grid()
plt.title('Superimposed Measured Sin Wave Fourier Transforms')
plt.xlabel('Frequency [KHz]')
plt.ylabel('Volts [V]')

plt.show()
