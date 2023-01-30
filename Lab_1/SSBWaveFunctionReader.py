import ugradio
import matplotlib.pyplot as plt
import numpy as np
coni = ugradio.sdr.SDR(direct = False, center_freq = 150e6, sample_rate =2.2e6)
data = coni.capture_data()
data = coni.capture_data()
data = coni.capture_data()
data = coni.capture_data()






np.save('SSB150-150.5MHZ.npy', data)


plt.plot(data[0])
plt.show()
plt.plot(np.fft.fft(data[0]))
plt.show()
#import IPython
#IPython.embed()