import numpy as np
import matplotlib.pyplot as plt

gs=['sin500.npy','sin700.npy','sin900.npy', 'sin1100.npy', 'sin1300.npy', 'sin1500.npy']
for g in gs:

    data = np.load(g) #Insert Data File Name
    #Build Plot
    data_fft = np.fft.fftshift(abs(np.fft.fft(data))) #Fourier Transform
    fft_freq = np.fft.fftshift(np.fft.fftfreq(len(data[0]),1/2.2))

    plt.plot(fft_freq,(data_fft[0]**2)/1000, label = g[3:-4] + "KHz Wave") #FFT


plt.legend(loc='center')
plt.grid(linestyle=":")
plt.title('Superimposed Power Spectrums with sample frequency 2.2MHz', size="14")
plt.xlabel('Frequency [MHz]', size="14")
plt.ylabel('Power proportional to [KW/Hz]', size="14")

plt.show()
