import matplotlib.pyplot as plt
import numpy as np
plt.style.use("dark_background")
o = np.linspace(0, 10*np.pi, 2000)
r = 1/(1+0.2*o)
x, y = r*np.cos(o), r*np.sin(o)
plt.scatter(x, y, c=o, cmap="magma", s=3)
plt.axis("equal")
plt.show()
