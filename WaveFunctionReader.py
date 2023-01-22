import ugradio
import matplotlib.pyplot as plt
import numpy as np
coni = ugradio.sdr.SDR(fir_coeffs=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2047]), sample_rate =3.2e6)
data = coni.capture_data()


"""
Arg 1: direct=True???

vs=3.2Mhz (Max freq rate)

Sample time. How long does it sample data for? 20248 data points

np.save('CLEAR NAME OF EXPERIMENT.npy', data)
"""

plt.plot(data[0])
plt.show()
import IPython
IPython.embed()
