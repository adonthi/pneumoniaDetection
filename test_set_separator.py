import os
import numpy as np
import png
import pydicom
import shutil
i = 0;
counter = 0;
directory = "C:\\Users\\Badri Donthi\\Documents\\pneumoniaDetection\\normal_images"
destin = "C:\\Users\\Badri Donthi\\Documents\\pneumoniaDetection\\separated_test_set\\normal_images"
for filename in os.listdir(directory):
    if filename.endswith(".png"):
        counter = counter + 1;
        print(counter);
        i = i + 1;
        if(i == 5):
            path = directory + "\\" + filename;
            destination = destin + "\\" + filename;
            shutil.copy(path,destination);
            os.remove(path);
            i = 0;
        