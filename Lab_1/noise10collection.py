import ugradio
import matplotlib.pyplot as plt
import numpy as np
coni = ugradio.sdr.SDR(fir_coeffs=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2047]), sample_rate =2.2e6)
samples = int(2048)
blocks = int(50)
data = coni.capture_data(nsamples = samples, nblocks = blocks)
np.save('noise2048block50.npy', data)
plt.plot(data[0])
plt.show()