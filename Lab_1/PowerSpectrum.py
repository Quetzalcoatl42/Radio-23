
import numpy as np
import matplotlib.pyplot as plt
data = np.load('noise1.npy') #Insert Data File Name

data_fft = abs(np.fft.fft(data)) #Fourier Transform

"""#Test Data
print(data_fft[0][100])
print(data_fft.real[0][100])
print(data_fft.imag[0][100])
"""

#Build Plot
#Frequency=np.arange(?????????????????????????)
time=np.arange(0,2048/2.2e6,1/2.2e6) #3.2e6 Sample Rate CHA


plt.plot(time,data_fft[0]) #FFT

#plt.plot(time,data_fft[0]**2) #Power Spectrum



plt.legend()
plt.title('My title')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Volts??? [V]')

plt.show()
