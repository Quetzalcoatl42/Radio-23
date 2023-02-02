import numpy as np
import matplotlib.pyplot as plt

data_file='sin700.npy'
data = np.load(data_file) #Insert Data File Name




#Build Plot
data_fft = np.fft.fftshift(np.fft.fft(data)) #Fourier Transform
fft_freq = np.fft.fftshift(np.fft.fftfreq(2048,1/2.2))


#Note [1:] code represents clipping the first data point (which provides weird results)
plt.plot(fft_freq,data_fft.real[0], label = "Real FFT") #Create Plot of real axis
plt.plot(fft_freq,data_fft.imag[0], label= "Imag FFT") #Create Plot of real axis


plt.legend()
plt.title('Voltage Spectrum of ' + data_file[3:-4] + "KHz Wave")
plt.xlabel('Frequency [MHz]')
plt.ylabel('Voltage [V]???')

plt.show()
