import numpy as np
import matplotlib.pyplot as plt


gs=['DSB600-630.npy','DSB600-570.npy']
gs=['DSB600-570.npy']
for g in gs:

    data = np.load(g) #Insert Data File Name

    #Build Plot
    data_fft = np.fft.fftshift(abs(np.fft.fft(data))) #Fourier Transform
    fft_freq = np.fft.fftshift(np.fft.fftfreq(len(data[0]),1/2.2))


    plt.plot(fft_freq,data_fft[0]**2/1000, label = g[3:-4] + "KHz Wave") #FFT
    plt.legend()

plt.title('Power Spectrum of 600-570 KHz DSB Wave')
plt.xlabel('Frequency [MHz]')
plt.ylabel('Log of Power Proportional to :[KW/Hz]?')
plt.yscale("log") #ADD & REMOVE
plt.show()
