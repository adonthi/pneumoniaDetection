import os
import numpy as np
import png
import pydicom
import shutil
i = 0;
counter = 0;
directory = "C:/Users/Badri Donthi/Documents/pneumoniaDetection/model3_training/pneumonia_images"
destin = "C:/Users/Badri Donthi/Documents/pneumoniaDetection/sepmodel4_test_set/normal_images"
for filename in os.listdir(directory):
    counter = counter + 1;
    print(counter);
    path = destin + "/" + filename;
    if (os.path.exists(path)):
        os.remove(path);
        
        