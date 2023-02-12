import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Load the data files
data_file='noise2048block50.npy'
noise = np.load(data_file)

#Add the different blocks together
data=np.zeros(len(noise[0]))
for n in range(len(noise)):
    data+= noise[n]

data=data/(len(noise))
print ("Data Len: " + str(len(noise[0])))
#Print Information
print (data_file)
print ("Length Noise: ", len(noise))
print ("Mean: ", np.mean(data))
print ("Variance: ", np.var(data))
print ("Standard deviation: ", np.std(data))

#Average of data
mean = np.mean(data)
std_dev = np.std(data)
variance = np.var(data)


#Plotting
hist_data = plt.hist(data, bins=20, density=True, color='blue')
plt.xlabel('Voltage [V]')
plt.ylabel('Normalised Frequency Counts')
plt.title('Average Gaussian Distribution of ' + data_file[5:9] + " samples in " +  data_file[14:-4] + " block")
plt.grid()

#Labels
mean_label = 'Mean: {:.3g}'.format(mean)
std_dev_label = 'Std Dev: {:.3g}'.format(std_dev)
variance_label = 'Variance: {:.3g}'.format(variance)
plt.text(0.05, 0.95, mean_label, transform=plt.gca().transAxes, fontsize=12)
plt.text(0.05, 0.90, std_dev_label, transform=plt.gca().transAxes, fontsize=12)
plt.text(0.05, 0.85, variance_label, transform=plt.gca().transAxes, fontsize=12)

# Plot the Gaussian distribution
mean = np.mean(data)
std_dev = np.std(data)
x = np.linspace(min(data), max(data), 100)
gaussian_distribution = plt.plot(x, 1/(std_dev * np.sqrt(2 * np.pi)) * np.exp( - (x - mean)**2 / (2 * std_dev**2) ), linewidth=2, color='red')
plt.legend(["Histogram", "Gaussian Distribution"])

# Perform goodness of fit test
ks_statistic, p_value = stats.kstest(data, 'norm', args=(mean, std_dev))
if p_value > 0.05:
    print('The Gaussian distribution fits the data (p-value = {:.3g})'.format(p_value))
else:
    print('The Gaussian distribution does not fit the data (p-value = {:.3g})'.format(p_value))


import pandas as pd

# Load the existing Excel file
file_name = "results.xlsx"
writer = pd.ExcelWriter(file_name, engine='openpyxl', mode='a')

# Create a dictionary to store the results
new_data = {'data_file': [data_file],
           'Length Noise': [len(noise)],
           'Mean': [np.mean(data)],
           'Variance': [np.var(data)],
           'Standard deviation': [np.std(data)],
           'Goodness of fit test': ['The Gaussian distribution fits the data (p-value = {:.3g})'.format(p_value) if p_value > 0.05 else 'The Gaussian distribution does not fit the data (p-value = {:.3g})'.format(p_value)]}

new_df = pd.DataFrame(new_data)

# Check if the sheet exists
if 'Sheet1' in writer.sheets:
    start_row = writer.sheets['Sheet1'].max_row
else:
    start_row = 0

# Append the new data to the existing Excel file
new_df.to_excel(writer, sheet_name='Sheet1', index=False, header=False, startrow=start_row)

# Save the changes
writer.save()