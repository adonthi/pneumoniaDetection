import os
import numpy as np
import png
import pydicom
directory = "C:\\Users\\Badri Donthi\\Documents\\pneumoniaDetection\\opacity_images"
for filename in os.listdir(directory):
    if filename.endswith(".dcm"):
        print(filename)
        path = directory + "\\" + filename;
        ds = pydicom.dcmread(path);
        shape = ds.pixel_array.shape
        # Convert to float to avoid overflow or underflow losses.
        image_2d = ds.pixel_array.astype(float)
        # Rescaling grey scale between 0-255
        image_2d_scaled = (np.maximum(image_2d,0) / image_2d.max()) * 255.0
        # Convert to uint
        image_2d_scaled = np.uint8(image_2d_scaled)
        # Write the PNG file
        destination = directory + "\\" + filename[:-3] + "png"
        with open(destination, 'wb') as png_file:
            w = png.Writer(shape[1], shape[0], greyscale=True)
            w.write(png_file, image_2d_scaled)
        os.remove(path)