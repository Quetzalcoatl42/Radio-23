import numpy as np
import matplotlib.pyplot as plt

# Load the data files
noise1 = np.load('noise1.npy')
noise2 = np.load('noise2.npy')
noise3 = np.load('noise3.npy')
noise4 = np.load('noise4.npy')
noise5 = np.load('noise5.npy')


# Concatenate the arrays along the first axis (rows)
data = np.concatenate((noise1[0], noise2[0], noise3[0], noise4[0], noise5[0]), axis=0)


#Print
print ("Length Data: ", len(data))
print ("Mean: ", np.mean(data))
print ("Variance: ", np.var(data))
print ("Standard deviation: ", np.std(data))



#Plotting
hist_data = plt.hist(data, bins=20, density=True, color='blue')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Gaussian Distribution of Data')
plt.grid()

# Plot the Gaussian distribution
mean = np.mean(data)
std_dev = np.std(data)
x = np.linspace(min(data), max(data), 100)
gaussian_distribution = plt.plot(x, 1/(std_dev * np.sqrt(2 * np.pi)) * np.exp( - (x - mean)**2 / (2 * std_dev**2) ), linewidth=2, color='red')
plt.legend([hist_data[2][0], gaussian_distribution[0]], ["Histogram", "Gaussian Distribution"])
plt.show()
