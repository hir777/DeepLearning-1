import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('sin.png')     # Read an image file. Pass a correct path as a argument
plt.imshow(img)

plt.show()
