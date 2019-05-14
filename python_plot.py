import matplotlib.pyplot as plt
import numpy as np

x_arr = np.linspace(0, 6*np.pi)
y = x_arr.copy()

# Plot a linear curve
plt.figure()
plt.plot(x_arr, y, '-.', color='k')
plt.show()



