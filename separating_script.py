import pandas as pd;
import os;
import shutil;
src = "C:\Users\Badri Donthi\Documents\\pneumoniaDetection\\stage_2_train_images\\"
dest1 = "C:\Users\Badri Donthi\Documents\\pneumoniaDetection\opacity_images\\";
dest0 = "C:\Users\Badri Donthi\Documents\\pneumoniaDetection\\normal_images\\";
df = pd.read_csv("stage_2_train_labels.csv");
x = 0;
for idx,row in df.iterrows():
    print (idx);
    if(row["Target"] == 1):
        itemsrc = src  + row["patientId"] +".dcm";
        itemdest = dest1;
        shutil.copy(itemsrc,itemdest);
    if(row["Target"] == 0):
        itemsrc = src  + row["patientId"] +".dcm";
        itemdest = dest0;
        shutil.copy(itemsrc,itemdest);
