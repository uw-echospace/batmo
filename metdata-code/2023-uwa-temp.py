import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator
import numpy as np

# Read the CSV file into a DataFrame, skipping the header row
data = pd.read_csv('2023-uwa.csv', skiprows=1)

# Convert 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Convert Fahrenheit to Celsius
data['Temperature'] = (data['Temperature'] - 32) * 5/9

# Set up the plot
fig, ax1 = plt.subplots(1, figsize=(8, 10))

# Create temperature gradient colormap
cmap = plt.cm.get_cmap('turbo')

# Calculate statistics per date
daily_stats = data.groupby(data['Date'].dt.date)['Temperature'].agg(['mean', 'median', lambda x: np.percentile(x, 25), lambda x: np.percentile(x, 75)])
daily_stats.columns = ['Mean', 'Median', '25th Percentile', '75th Percentile']

# Plot the scatter plot with temperature gradient colors and adjusted opacity
sc = ax1.scatter(data['Date'], data['Temperature'], c=data['Temperature'], cmap=cmap, alpha=0.7)
ax1.set_ylabel('Temperature (°C)')
ax1.set_title('2023 UWA Temperature')

# Plot trendlines per date
ax1.plot(daily_stats.index, daily_stats['Mean'], color='red', linestyle='--', label='Mean')
ax1.plot(daily_stats.index, daily_stats['Median'], color='green', linestyle='--', label='Median')
ax1.plot(daily_stats.index, daily_stats['25th Percentile'], color='blue', linestyle='--', label='25th Percentile')
ax1.plot(daily_stats.index, daily_stats['75th Percentile'], color='orange', linestyle='--', label='75th Percentile')

# Add legend
ax1.legend()

# Add colorbar
cbar = fig.colorbar(sc, ax=ax1)
cbar.set_label('Temperature (°C)')

# Adjust the y-axis ticks
ax1.yaxis.set_major_locator(MultipleLocator(1))

# Adjust the layout and spacing
plt.tight_layout()

# Display the plot
plt.show()



