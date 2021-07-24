import numpy as np
import matplotlib.pyplot as plt

# Create the sine and cosine function
x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# Draw the graph and save it as a png file. 
# Then, you can open the file with the below command on your WSL environment.
# wslview sincos.png
plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle = "--", label="cos")    # draw it with a dotted line
plt.xlabel("x")     # x-axis label
plt.ylabel("y")     # y-axis label
plt.title('sin & cos')  # title
plt.legend()
plt.savefig("sincos.png")
