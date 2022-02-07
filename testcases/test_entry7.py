import matplotlib.pyplot as plt
# plt.show(photo)
from skimage import io
photo=io.imread('C:\\Users\\srika\\OneDrive\\Pictures\\iki.png')
print(type(photo))
print(photo.shape)
plt.show(photo)