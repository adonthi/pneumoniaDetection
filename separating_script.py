import pandas as pd;
import os;
import shutil;
src = "C:/Users/Badri Donthi/Documents/pneumoniaDetection/all_images/"
dest1 = "C:/Users/Badri Donthi/Documents/pneumoniaDetection/training_set/opacity_images/";
dest0 = "C:/Users/Badri Donthi/Documents/pneumoniaDetection/training_set/normal_images/";
df = pd.read_csv("stage_2_train_labels.csv");
x = 0;
for idx,row in df.iterrows():
    print (idx);
    if(row["Target"] == 1):
        itemsrc = src  + row["patientId"] +".png";
        itemdest = dest0;
        shutil.copy(itemsrc,itemdest);
    if(row["Target"] == 0):
        itemsrc = src  + row["patientId"] +".png";
        itemdest = dest1;
        shutil.copy(itemsrc,itemdest);
