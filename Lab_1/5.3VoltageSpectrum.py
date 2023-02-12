import numpy as np
import matplotlib.pyplot as plt


gs=['sin700.npy', 'sin1300.npy']
for g in gs:

    data = np.load(g) #Insert Data File Name
    #Build Plot
    data_fft = np.fft.fftshift(np.fft.fft(data)) #Fourier Transform
    fft_freq = np.fft.fftshift(np.fft.fftfreq(2048,1/2.2))
    
    
    #Note [1:] code represents clipping the first data point (which provides weird results)
    plt.plot(fft_freq,data_fft.imag[0], label= g[3:-4] + "KHz Imag FFT") #Create Plot of real axis
    plt.plot(fft_freq,data_fft.real[0], label = g[3:-4] + "KHz Real FFT") #Create Plot of real axis



plt.legend()
plt.grid(linestyle=":")
plt.title('Voltage Spectrum of 700KHz & 1300KHz Wave')
plt.xlabel('Frequency [MHz]')
plt.ylabel('Proportional to Voltage [V]')

plt.show()
