
import numpy as np
import matplotlib.pyplot as plt

data_file='sin1500.npy'
data = np.load(data_file) #Insert Data File Name




#Build Plot
data_fft = abs(np.fft.fft(data)) #Fourier Transform
fft_freq = np.fft.fftshift(np.fft.fftfreq(2048,1/2.2))


plt.plot(fft_freq[1:],data_fft[0][1:]**2, label = data_file[3:-4] + "KHz Wave", color="black") #FFT

plt.legend()
plt.title('Power Spectrum of ' + data_file[3:-4] + "KHz Wave")
plt.xlabel('Frequency [KHz]')
plt.ylabel('Power propoertional to :[W]?')

plt.show()
