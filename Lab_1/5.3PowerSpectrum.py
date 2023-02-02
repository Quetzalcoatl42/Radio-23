
import numpy as np
import matplotlib.pyplot as plt

data_file='sin700.npy'
data = np.load(data_file) #Insert Data File Name




#Build Plot
data_fft = np.fft.fftshift(abs(np.fft.fft(data))) #Fourier Transform
fft_freq = np.fft.fftshift(np.fft.fftfreq(len(data[0]),1/2.2))


plt.plot(fft_freq,data_fft[0]**2, label = data_file[3:-4] + "KHz Wave", color="black") #FFT

plt.legend()
plt.title('Power Spectrum of ' + data_file[3:-4] + "MHz Wave")
plt.xlabel('Frequency [MHz]')
plt.ylabel('Power propoertional to :[W/Hz]?')

plt.show()
