import numpy as np
import joblib
import cv2
import tensorflow
model1= tensorflow.keras.models.load_model("models/vggmodel.h5")
model2= tensorflow.keras.models.load_model("models/iv3model.h5")

IMG_SIZE = (224, 224)

def prediction(img_path):
  image= cv2.imread(img_path)
  image= cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
  image= cv2.resize(image,IMG_SIZE)
  image= np.expand_dims(image,axis=0)
  pred1= model1.predict(image)
  pred2= model2.predict(image)
  ind1= np.argmax(pred1)
  ind2= np.argmax(pred2)
  classes= ['B.subtilis', 'C.albicans', 'E.coli', 'P.aeruginosa', 'S.aureus']
  prediction=''
  if pred1[0][ind1]>pred2[0][ind2]:
    prediction= classes[ind1]
  else:
    prediction= classes[ind2]
  return prediction

