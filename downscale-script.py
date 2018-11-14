import os;
import numpy as np
import png
import pydicom
import PIL
from PIL import Image
import timeit
start = timeit.timeit()
directory = "C:\\Users\\Badri Donthi\\Documents\\pneumoniaDetection\\separated_test_set\\opacity_images"
counter = 0;
for filename in os.listdir(directory):
    if filename.endswith(".png"):
		counter = counter + 1;
		print(counter);
		basewidth = 128;
		dest = directory + "//" + filename
		img = Image.open(dest);
		wpercent = (basewidth / float(img.size[0]));
		hsize = int((float(img.size[1]) * float(wpercent)));
		img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS);
		img.save(dest);
end = timeit.timeit()
print ((end - start));