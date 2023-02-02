import numpy as np
import matplotlib.pyplot as plt

# Load the data files
data_file='noise2048block4.npy'
noise = np.load(data_file)

#Add the different blocks together
data=np.zeros(len(noise[0]))
for n in range(len(noise)):
    data+= noise[n]



#Average of data
data=data/(len(noise))

"""
#Print Information
print (data_file)
print ("Length Noise: ", len(noise))
print ("Mean: ", np.mean(data))
print ("Variance: ", np.var(data))
print ("Standard deviation: ", np.std(data))
"""

#Build Plot
data_fft = np.fft.fftshift(abs(np.fft.fft(data*2))) #Fourier Transform #???
fft_freq = np.fft.fftshift(np.fft.fftfreq(len(noise[0]),1/2.2)) #!!!

print("fft_freq: ",fft_freq)
print("data_fft: ",data_fft)

#Plotting
plt.plot(fft_freq,data_fft, label = data_file[3:-4] + "KHz Wave", color="black") #FFT
plt.xlabel('Frequency [MHz]')
plt.ylabel('Log of Normalised Frequency Counts')
plt.title('Power Spectrum of ' + data_file[5:9] + " samples in average of " +  data_file[-5:-4] + " blocks")
plt.grid()
plt.yscale("log") #!!!

plt.show()
