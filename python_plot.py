import matplotlib.pyplot as plt
import numpy as np

x_arr = np.linspace(0, 6*np.pi)

# Plot a cosine curve
plt.figure()
plt.plot(x_arr, np.cos(x_arr), '-.', color='k')
plt.show()



