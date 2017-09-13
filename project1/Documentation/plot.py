from scipy import *
import numpy as np  
import matplotlib.pyplot as plt

data = np.loadtxt('test6')

plt.plot(data[:,0], data[:,3], 'ro')
plt.title('Project 1')
plt.title('test 6', loc='left')
plt.title('Error Analysis', loc='right')
plt.xlabel('Interval (0,1)')
plt.ylabel('log10(relative error)')

plt.show()

