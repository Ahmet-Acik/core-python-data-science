"""
Weather Dataset Exercise
------------------------
Practice time series analysis and visualization.
"""
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset
weather = pd.read_csv('weather.csv')
print(weather.head())

# 2. Plot temperature over time
weather['date'] = pd.to_datetime(weather['date'])
plt.plot(weather['date'], weather['temperature'])
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.title('Temperature Over Time')
plt.show()
