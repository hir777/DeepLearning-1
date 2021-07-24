import numpy as np
import matplotlib.pyplot as plt

# Create the sine function.
x = np.arange(0, 6, 0.1)
y = np.sin(x)

# Draw the graph.
plt.plot(x, y)
# Save it as a png file. Then, you can open the file with the below command on your WSL environment.
# wslview sin.png
plt.savefig("sin.png")
