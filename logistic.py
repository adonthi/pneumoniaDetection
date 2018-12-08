from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
import numpy
import os
json_file = open('C:/Users/Badri Donthi/Documents/pneumoniaDetection/model1final.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("C:/Users/Badri Donthi/Documents/pneumoniaDetection/model1final.h5")
print("Loaded model from disk")
normal = 0;
opacity = 0;
counter = 0;
# evaluate loaded model on test data
import numpy as np
from keras.preprocessing import image
directory = "C:/Users/Badri Donthi/Documents/pneumoniaDetection/separated_test_set/normal_images"
for filename in os.listdir(directory):
    if filename.endswith(".png"):
      loc = "C:/Users/Badri Donthi/Documents/pneumoniaDetection/separated_test_set/normal_images/" + filename;
      test_image = image.load_img(loc);
      test_image = image.img_to_array(test_image)
      test_image = np.expand_dims(test_image, axis = 0)
      result = loaded_model.predict(test_image)
      counter = counter + 1;
      print(counter);
      if result[0][0] == 1:
        opacity = opacity + 1;
        #opacity = pneumonia
      else:
        normal = normal + 1;
        #normal = notnormal

counter = 0;
opacity2 = 0;
normal2 = 0;
directory = "C:/Users/Badri Donthi/Documents/pneumoniaDetection/separated_test_set/opacity_images";
for filename in os.listdir(directory):
    if filename.endswith(".png"):
      loc = "C:/Users/Badri Donthi/Documents/pneumoniaDetection/separated_test_set/opacity_images/" + filename;
      test_image = image.load_img(loc);
      test_image = image.img_to_array(test_image)
      test_image = np.expand_dims(test_image, axis = 0)
      result = loaded_model.predict(test_image)
      counter = counter + 1;
      print(counter);
      if result[0][0] == 1:
        opacity2 = opacity2 + 1;
        #opacity = pneumonia
      else:
        normal2 = normal2 + 1;
        #normal = notnormal

print("Normal count:" + normal);
print("Opacity count:"  + opacity);