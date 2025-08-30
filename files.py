import matplotlib.pyplot as plt
import numpy as np
theta = np.linspace(0, 8*np.pi, 2000)
r = np.linspace(0, 5, 2000) # Make the number of elements the same as theta
for h in range(1,4):
    x = r*np.cos(theta*h)
    y = r*np.sin(theta*h)
    plt.plot(x, y)
plt.axis("equal")
plt.show()
