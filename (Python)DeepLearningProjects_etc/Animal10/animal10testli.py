#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense, Flatten ,Dropout, Activation, Conv2D, MaxPooling2D, BatchNormalization
from tensorflow.keras.models import Sequential
import numpy as np
import os 
import random
import cv2

from keras.utils.generic_utils import get_custom_objects
from sklearn.model_selection import train_test_split
from keras.backend import sigmoid
from tensorflow.keras import regularizers
import matplotlib.pyplot as plt
from tensorflow.keras.callbacks import TensorBoard
import time


DATADIR = r"\Users\doguk\Desktop\Animal10\raw-img"
CATEGORIES = ["butterfly", "cat", "chicken", "cow", "dog", "elephant", "horse",
             "sheep", "spider", "squirrel"]

for category in CATEGORIES:
    path = os.path.join(DATADIR, category)
    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
        plt.imshow(img_array, cmap="gray")
        plt.show()
        break
    break


# In[2]:


IMG_SIZE = 100

new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))

plt.imshow(new_array, cmap="gray")
plt.show()


# In[3]:


training_data = []

def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                training_data.append([new_array, class_num])
            except Exception as e:
                pass
        
create_training_data()


# In[4]:


print(len(training_data))


# In[5]:


import random
random.shuffle(training_data)


# In[6]:


for sample in training_data:
    print(sample[1])


# In[7]:


X = []
y = []


# In[8]:


for features, label in training_data:
    X.append(features)
    y.append(label)
    
x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.2)


# In[9]:


x_train=np.array(x_train).reshape(-1,IMG_SIZE,IMG_SIZE,1)
x_train=tf.keras.utils.normalize(x_train,axis=1)
y_train=np.array(y_train)


# In[10]:


def swish(x, beta = 1):
    return(x*sigmoid(beta*x))

get_custom_objects().update({'swish': Activation(swish)})


# In[33]:


x_train.shape[1:]


# In[11]:


NAME = "Animal-10-cnn-{}".format(int(time.time()))


# In[30]:


"""model = Sequential()
model.add(Conv2D(32, kernel_size = 3, activation=swish, input_shape = x_train.shape[1:]))
model.add(BatchNormalization())
model.add(Conv2D(32, kernel_size = 3, activation=swish))
model.add(BatchNormalization())
model.add(Conv2D(32, kernel_size = 5, strides=2, padding='same', activation=swish))
model.add(BatchNormalization())
model.add(Dropout(0.4))
model.add(Conv2D(64, kernel_size = 5, strides=2, padding='same', activation=swish))
model.add(BatchNormalization())
model.add(Dropout(0.4))
model.add(Conv2D(256, kernel_size = 5, activation=swish))
model.add(BatchNormalization())
model.add(Flatten())
model.add(Dropout(0.4))
model.add(Dense(64, activation=swish))
model.add(Dense(10, activation='softmax'))     
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])  """        


# In[12]:


model = Sequential()
model.add(Conv2D(32, kernel_size = 3, activation=swish, input_shape = x_train.shape[1:]))
model.add(BatchNormalization())
model.add(Conv2D(256, kernel_size = 5, strides=3, activation=swish))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(BatchNormalization())
model.add(Conv2D(256, kernel_size = 2, strides=2, padding='same', activation=swish))
model.add(BatchNormalization())
model.add(Dropout(0.3))
model.add(Conv2D(64, kernel_size = 2, strides=2, padding='same', activation=swish))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(BatchNormalization())
model.add(Dropout(0.3))
model.add(BatchNormalization())
model.add(Flatten())
model.add(Dropout(0.3))
model.add(Dense(1024, activation='relu'))
model.add(Dense(512, activation=swish))
model.add(Dense(1024, activation='relu'))
model.add(Dense(512, activation=swish))
model.add(Dense(64, activation=swish))
model.add(Dense(10, activation='softmax'))     
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]) 


# In[26]:


model.summary()


# In[17]:


tensorboard = TensorBoard(log_dir='logs\{}'.format(NAME))

batch = 64
epoch = 500


# In[18]:


history = model.fit(x_train,y_train,epochs=epoch,batch_size=batch, validation_split = 0.2, callbacks=[tensorboard])


# In[20]:


x_test= np.array(x_test).reshape(-1,IMG_SIZE,IMG_SIZE,1)
predictions = model.predict(x_test) 


# In[21]:


predicted_val = []

for i in range(len(x_test)):
    predicted_val.append(np.argmax(predictions[i]))
    
    print('Predicted label: {}\nActual label: {}\n'.format(np.argmax(predictions[i]), y_test[i])) 
    


# In[23]:


predicted_val = []
correct, false = 0,0
for i in range(len(x_test)):
    predicted_val.append(np.argmax(predictions[i]))
    
    #print('Predicted label: {}\nActual label: {}\n'.format(np.argmax(predictions[i]), y_test[i])) 
    #print(np.argmax(predictions[i]))
    if np.argmax(predictions[i]) == y_test[i]:
        correct+= 1
    else:
        false+=1
        
test_acc= (correct / (false + correct)) * 100
print(test_acc)


# In[24]:


import pandas as pd

submission_df = pd.DataFrame({'label':y_test,'PredictedLabel': predicted_val})


# In[25]:


submission_df.to_csv("submission-500-EPOCH.csv", index=False)


# In[19]:


model.save("animal10-500EPOCH-CNN.model")


# In[129]:




