import numpy as np
import os
import skimage
from skimage import data, io, filters, color

path = "C:\\Users\\Personal\\Desktop\\bst img\\2"
files = os.listdir(path);

images = [];
for f in files:
    images.append (io.imread(path + '\\' + f));
    break; #testing purposes. remove this when running

newImage = images[0]; #copy
'''
stepSize = 0.5;
step = 10;
for img in images:
    newImage += step*img;
    step = step + stepSize;

io.imsave("Summed.jpg", newImage);
'''

height, width = newImage.shape[0], newImage.shape[1];
newImageA = np.ndarray(shape=(width,height,4), dtype=np.int8)

for r in range(0, height):
    for c in range(0, width):
        pixel = newImage[r,c];
        pixelWithAlpha = pixel, 255;
        print(pixelWithAlpha);
        break
    break
#io.imshow(data.cat());
#io.show()
