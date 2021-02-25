import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import random
import pickle
import tensorflow as tf
from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense,Dropout,Activation,Flatten,Conv2D,MaxPooling2D
from tensorflow.keras.layers import*
from tensorflow.keras.activations import*
DATADIR="C:\\Users\\furkanyanteri\\Desktop\\Guncel\\animals10\\hayvanat2\\"
TURLER=["at","fil","inek","kedi","kelebek","kopek","koyun","orumcek","sincap","tavuk"]
training_data=[]
IMG_SIZE=40#6
for tur in TURLER:
    path=os.path.join(DATADIR,tur)
    tur_numarasi=TURLER.index(tur)
    # print(len(os.listdir(path))) #* ---> O pathtedi img sayisi
    for img in os.listdir(path):
        try:
            img_array=cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
            new_array=cv2.resize(img_array,(IMG_SIZE,IMG_SIZE)) #*tum fotograflari ortak boyutta normalize inceleyelim
            training_data.append([new_array,tur_numarasi])
        except Exception as e:
            pass 
        # plt.imshow(img_array,cmap="gray")
        # plt.imshow(new_array,cmap="gray")
        # plt.show()
        # break
    #print (len(img_array))
    # break
# print("------------------------\n",img_array,"\n------------------------")
# print(img_array.shape)
print("train data boyut: ",len(training_data))
random.shuffle(training_data)
X=[]
y=[]
# for features,label in training_data:
#      X.append(features)
#      y.append(label)
tempx=1
for features,label in training_data:
    if (tempx<round(len(training_data)*0.8)):
        X.append(features)
        y.append(label)
    tempx+=1
# for i in range(round(len(training_data)*0.8)):
# for i in range(len(training_data)):
#     X.append(training_data[0])
#     y.append(training_data[1])


X=np.array(X).reshape(-1,IMG_SIZE,IMG_SIZE,1)#!BURAYA BAK BAKALIM KALDIRIP DENEYELIM
y=np.array(y)
# for i in range (len())



#*--------------------------------------------------pickling
pickle_out=open("X.pickle","wb")
pickle.dump(X,pickle_out)
pickle_out.close()

pickle_out=open("y.pickle","wb")
pickle.dump(y,pickle_out)
pickle_out.close()

pickle_in=open("X.pickle","rb")
X=pickle.load(pickle_in)

pickle_in=open("y.pickle","rb")
y=pickle.load(pickle_in)
#*--------------------------------------------------pickling
X=X/255.0
print(X.shape)
print(y.shape)
#!------------------------------------------------------------------------------------------------------
DATADIR="C:\\Users\\furkanyanteri\\Desktop\\Guncel\\animals10\\hayvanat_test\\"
# TURLER=["at","fil","inek","kedi","kelebek","kopek","koyun","orumcek","sincap","tavuk"]
test_data=[]
for tur in TURLER:
    path=os.path.join(DATADIR,tur)
    tur_numarasi=TURLER.index(tur)
    # print(len(os.listdir(path))) #* ---> O pathtedi img sayisi
    for img in os.listdir(path):
        try:
            img_array=cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
            new_array=cv2.resize(img_array,(IMG_SIZE,IMG_SIZE)) #*tum fotograflari ortak boyutta normalize inceleyelim
            test_data.append([new_array,tur_numarasi])
        except Exception as e:
            pass 
print("test data boyut: ",len(test_data))
random.shuffle(test_data)
X2=[]
y2=[]
for features,label in test_data:
    X2.append(features)
    y2.append(label)
X2=np.array(X2).reshape(-1,IMG_SIZE,IMG_SIZE,1)
y2=np.array(y2)
#*--------------------------------------------------pickling
pickle_out=open("X2.pickle","wb")
pickle.dump(X2,pickle_out)
pickle_out.close()

pickle_out=open("y2.pickle","wb")
pickle.dump(y2,pickle_out)
pickle_out.close()

pickle_in=open("X2.pickle","rb")
X2=pickle.load(pickle_in)

pickle_in=open("y2.pickle","rb")
y2=pickle.load(pickle_in)
#*--------------------------------------------------pickling
X2=X2/255.0
# print(X.shape)
# print(y.shape)
#!------------------------------------------------------------------------------------------------------

#?-----------------------------------------------------------------------------------model
# model = Sequential ()

# model.add(Conv2D(64, (3,3), input_shape = X.shape[1:]))
# model.add(Activation("relu"))
# model.add(MaxPooling2D(pool_size=(2,2)))

# model.add(Conv2D(64, (3,3)))
# model.add(Activation("relu"))
# model.add(MaxPooling2D(pool_size=(2,2)))

# model.add(Flatten())
# model.add(Dense(64))

# model.add(Dense(1))
# model.add(Activation('sigmoid'))

# model.compile(loss="binary_crossentropy",optimizer="Adam",metrics=['accuracy'])

# model.fit(X, y, batch_size=32,epochs=4, validation_split=0.1)
# model.fit(X, y,epochs=30, validation_split=0.1)

#?-----------------------------------------------------------------------------------model
model = Sequential()
model.add(Conv2D(32, kernel_size = 3, activation=swish, input_shape = X.shape[1:]))
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

# model.compile(loss="binary_crossentropy",optimizer="Adam",metrics=['accuracy'])

model.fit(X, y, batch_size=32,epochs=4, validation_split=0.1)
print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||son")

score=model.evaluate(X2,y2,verbose=0)
print("Test loss= ",score[0])
print("Test  acc= ",score[1])

# print(X[1])
# print("---------------------------->")
#* atlara bak->kopeklere bak->.... klasordeki ttum fotograflara bakip sonra diger klasore geciyoruz.