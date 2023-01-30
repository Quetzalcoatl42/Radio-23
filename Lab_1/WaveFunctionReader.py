import ugradio
import matplotlib.pyplot as plt
import numpy as np
coni = ugradio.sdr.SDR(fir_coeffs=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2047]), sample_rate =2.2e6)
data = coni.capture_data()






np.save('SSB30MHZ-30.5MHZ.im[phaseshift].npy', data)


plt.plot(data[0])
plt.show()
plt.plot(np.fft.fft(data[0]))
plt.show()
#import IPython
#IPython.embed()
