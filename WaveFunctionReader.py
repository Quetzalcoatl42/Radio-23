import ugradio
import matplotlib.pyplot as plt
import numpy as np
coni = ugradio.sdr.SDR(fir_coeffs=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2047]))
data = coni.capture_data()

"""
np.save('CLEAR NAME OF EXPERIMENT.npy', data)
"""

plt.plot(data[0])
plt.show()
import IPython
IPython.embed()
