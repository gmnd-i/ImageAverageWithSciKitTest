import os
import skimage
from skimage import data, io, filters

path = "C:\\Users\\Personal\\Desktop\\bst img\\2"
files = os.listdir(path);

images = [];
for f in files:
    images.append (io.imread(path + '\\' + f));

newImage = images[0]; #copy

#averaging color pixel by pixel
X = newImage.shape[0];
Y = newImage.shape[1];

for x in range(0, X):
    for y in range(0, Y):
    #for each pixel................. {
        pixels = []; #(x,y) th pixel of every image
        for i in images:
            pixels.append(i[x][y])

        rAvg = gAvg = bAvg = 0;
        for p in pixels:
            rAvg += p[0];
            gAvg += p[1];
            bAvg += p[2];

        numberOfImages = len(pixels);
        rAvg = rAvg / numberOfImages;
        gAvg = gAvg / numberOfImages;
        bAvg = bAvg / numberOfImages;
        #done averaging

        newImage[x][y] = [rAvg, gAvg, bAvg];
    #................................}
#now newImage contains the pixel averaged image
#print(pixels)

#img = io.imread(path + '\\' + files[0]);

io.imshow(newImage);
io.show();
io.imsave("averaged.jpg", newImage);



