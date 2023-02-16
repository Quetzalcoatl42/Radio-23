import ugradio
import matplotlib.pyplot as plt
import numpy as np
coni = ugradio.sdr.SDR(direct = False, center_freq = 1421e6, sample_rate =2.2e6, gain = 30)
data = coni.capture_data()
data = coni.capture_data()
data = coni.capture_data()
data = coni.capture_data()
data = np.empty((2048,2048))
blocks = 2048
i = 0
#while(i < blocks):
    
#    new_data = coni.capture_data(nsamples = 2048)
#    data[i] = new_data[0]
    #np.save('hydrogen_sample_1.npy', data)
#    i += 1
#    print(str(i))
data = coni.capture_data(nsamples = 2048, nblocks = 2048)



np.save('hydrogen_sample_5.npy', data)
avg = np.average(data)
plt.plot(avg)
plt.show()
plt.plot(np.fft.fft(avg))
plt.show()
#import IPython
#IPython.embed()