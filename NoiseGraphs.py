import numpy as np
import matplotlib.pyplot as plt

# Load the data files
data_file='noise20480block1.npy'
noise = np.load(data_file)



# Concatenate the arrays along the first axis (rows)
data = noise[0]


#Print
print ("Length Data: ", len(data))
print ("Mean: ", np.mean(data))
print ("Variance: ", np.var(data))
print ("Standard deviation: ", np.std(data))



#Plotting
hist_data = plt.hist(data, bins=20, density=True, color='blue')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Gaussian Distribution of ' + data_file[5:10] + " samples in " +  data_file[-5:-4] + " block")
plt.grid()

# Plot the Gaussian distribution
mean = np.mean(data)
std_dev = np.std(data)
x = np.linspace(min(data), max(data), 100)
gaussian_distribution = plt.plot(x, 1/(std_dev * np.sqrt(2 * np.pi)) * np.exp( - (x - mean)**2 / (2 * std_dev**2) ), linewidth=2, color='red')
plt.legend([hist_data[2][0], gaussian_distribution[0]], ["Histogram", "Gaussian Distribution"])
plt.show()
