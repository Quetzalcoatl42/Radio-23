
import numpy as np
import matplotlib.pyplot as plt

gs=['g710.npy','g708.npy','g706.npy','g705.npy', 'g704.npy']
for g in gs:

    data = np.load(g) #Insert Data File Name
    
    data_fft = abs(np.fft.fft(data)) #Fourier Transform
    
    #Test Data
    print(data_fft[0][100])
    print(data_fft.real[0][100])
    print(data_fft.imag[0][100])
    
    
    #Build Plot
    #Frequency=np.arange(?????????????????????????)
    time=np.arange(0,2048/2.2e6,1/2.2e6) #3.2e6 Sample Rate CHA
    
    
    plt.plot(time,data_fft[0], label = g) #FFT
    
    #plt.plot(time,data_fft[0]**2) #Power Spectrum
    
    

plt.legend()
plt.title('My title')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Volts??? [V]')

plt.show()
