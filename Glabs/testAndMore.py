import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])
'''
# Using object-oriented approach

fig, ax = plt.subplots() # Create figure and axes objects

ax.plot(xpoints, ypoints) #plot data 
plt.show() # Display the plot
'''

# using object-oriented approach
fig, ax = plt.subplots() # Create figure and axes objects
ax.plot(xpoints, ypoints, 'Zuberi') #Plot data
plt.show() # Display the plot 