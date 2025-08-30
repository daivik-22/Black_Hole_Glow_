# Spiral Scatter Plot Visualization

- This project generates a beautiful spiral pattern using **Python**, **NumPy**, and **Matplotlib**.  
- The spiral is plotted in polar coordinates, where the radius decreases as the angle increases, creating a colorful decaying spiral effect.

---

## 📂 Code Overview

```python
import matplotlib.pyplot as plt
import numpy as np

# Use a dark theme for the plot
plt.style.use("dark_background")

# Generate values of angle (θ) from 0 to 10π
o = np.linspace(0, 10*np.pi, 2000)

# Define radius function r(θ)
r = 1 / (1 + 0.2*o)

# Convert polar (r, θ) to Cartesian (x, y)
x, y = r * np.cos(o), r * np.sin(o)

# Create scatter plot
plt.scatter(x, y, c=o, cmap="magma", s=3)

# Ensure equal scaling for x and y axes
plt.axis("equal")

# Show the plot
plt.show()
```

🌀 Output

--> The code generates a spiral scatter plot where:
- The radius decreases as the angle increases.
- The color of the points varies with the angle, using the magma colormap.
- The background is set to a dark theme.

📦 Requirements

- Python 3.x
- NumPy
- Matplotlib
- Install dependencies with:
- pip install numpy matplotlib

▶️ Usage

- Run the script:
- python spiral_plot.py
- This will open a window displaying the spiral scatter plot.

🎨 Example Visualization
- The plot resembles a colorful decaying spiral galaxy on a dark background.

✨ Features

- Customizable colormap (cmap) for coloring the spiral.
- Adjustable point size (s in plt.scatter).
- Easily extendable for experimenting with other mathematical spirals.
