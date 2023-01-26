
import numpy as np
import matplotlib.pyplot as plt
data = np.load('f8.npy') #Insert Data File Name

data_fft = np.fft.fft(data) #Fourier Transform

#Test Data
print(data_fft[0][100]) #Should be 2048
print(data_fft.real[0][100]) #Should be 2048
print(data_fft.imag[0][100]) #Should be 2048


#Build Plot

#Frequency=np.arange(?????????????????????????)
time=np.arange(0,2048/2.2e6,1/2.2e6) #3.2e6 Sample Rate CHA
plt.plot(time,data_fft.real[0], label = "Real_FFT") #Create Plot of real axis
plt.plot(time,data_fft.imag[0], label= "Imag_FFT") #Create Plot of real axis


plt.legend()
plt.title('My title')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Volts??? [V]')

plt.show()
