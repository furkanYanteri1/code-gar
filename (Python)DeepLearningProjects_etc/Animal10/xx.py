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
# def yatay_yansit(arr):
#     boyutArray=len(arr)
#     boyut=boyutArray-1#boyutun bir eksigini alacagiz array 0 dan basliyor lazim oldu iste uzatma
#     for i in range(boyut):
#         for j in range(int(boyutArray/2)):
#             temp=arr[i][j]
#             arr[i][j]=arr[i][boyut-j]
#             arr[i][boyut-j]=temp

# DATADIR="C:\\Users\\furkanyanteri\\Desktop\\Guncel\\animals10\\hayvanat\\"
# TURLER=["at","fil","inek","kedi","kelebek","kopek","koyun","orumcek","sincap","tavuk"]
# training_data=[]
# IMG_SIZE=60#6
# indis=0#burada flipped imagelari testten ayirmak icin tutacagiz ya kardes ondan dolayli
# for tur in TURLER:
#     path=os.path.join(DATADIR,tur)
#     tur_numarasi=TURLER.index(tur)
#     for img in os.listdir(path):
#         try:
#             img_array=cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
#             new_array=cv2.resize(img_array,(IMG_SIZE,IMG_SIZE)) #*tum fotograflari ortak boyutta normalize inceleyelim
#             training_data.append([new_array,tur_numarasi])
#         except Exception as e:
#             print("##########################################")
#             pass 
# print("train data boyut: ",len(training_data))
# random.shuffle(training_data)
# X=[]
# y=[]
# X2=[]
# y2=[]

# tempx=1

# for features,label in training_data:
#     if (tempx<round(len(training_data)*0.7)):
#         X.append(features)
#         y.append(label)
#         X.append(cv2.flip(features,1))#?YATAY YANSIMASININ ALINMIS HAILNI BURADA EKLIYORUZ
#         y.append(label)

#     else:
#         X2.append(features)
#         y2.append(label)
#     tempx+=1

# print("X boyut: ",len(X))
# print("y boyut: ",len(y))
# print("X2 boyut: ",len(X2))
# print("y2 boyut: ",len(y2))


# fermuar=list(zip(X,y))#?X ve y yi baglayip shuffle sonra tekrar ayristirma.(X ve y ayri ayri shuffle edilirse sira karisiyor)
# random.shuffle(fermuar)
# X,y=zip(*fermuar)

# fermuar=list(zip(X2,y2))#?X2 ve y2 yi baglayip shuffle sonra tekrar ayristirma.(X2 ve y2 ayri ayri shuffle edilirse sira karisiyor)
# random.shuffle(fermuar)
# X2,y2=zip(*fermuar)

# X=np.array(X).reshape(-1,IMG_SIZE,IMG_SIZE,1)#!BURAYA BAK BAKALIM KALDIRIP DENEYELIM
# y=np.array(y)

# X2=np.array(X2).reshape(-1,IMG_SIZE,IMG_SIZE,1)
# y2=np.array(y2)
# # for i in range (len())



#*--------------------------------------------------pickling
# pickle_out=open("X.pickle","wb")
# pickle.dump(X,pickle_out)
# pickle_out.close()

# pickle_out=open("y.pickle","wb")
# pickle.dump(y,pickle_out)
# pickle_out.close()

pickle_in=open("X.pickle","rb")
X=pickle.load(pickle_in)

pickle_in=open("y.pickle","rb")
y=pickle.load(pickle_in)
#*--------------------------------------------------pickling
X=X/255.0
print(X.shape)
print(y.shape)
#!------------------------------------------------------------------------------------------------------
# DATADIR="C:\\Users\\furkanyanteri\\Desktop\\Guncel\\animals10\\hayvanat_test\\"
# # TURLER=["at","fil","inek","kedi","kelebek","kopek","koyun","orumcek","sincap","tavuk"]
# test_data=[]
# for tur in TURLER:
#     path=os.path.join(DATADIR,tur)
#     tur_numarasi=TURLER.index(tur)
#     # print(len(os.listdir(path))) #* ---> O pathtedi img sayisi
#     for img in os.listdir(path):
#         try:
#             img_array=cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
#             new_array=cv2.resize(img_array,(IMG_SIZE,IMG_SIZE)) #*tum fotograflari ortak boyutta normalize inceleyelim
#             test_data.append([new_array,tur_numarasi])
#         except Exception as e:
#             pass 
# print("test data boyut: ",len(test_data))
# random.shuffle(test_data)
# X2=[]
# y2=[]
# for features,label in test_data:
#     X2.append(features)
#     y2.append(label)
# X2=np.array(X2).reshape(-1,IMG_SIZE,IMG_SIZE,1)
# y2=np.array(y2)
#*--------------------------------------------------pickling

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
model = Sequential()
model.add(Conv2D(32, kernel_size = 3, activation='relu', input_shape = X.shape[1:]))
model.add(BatchNormalization())
model.add(Conv2D(64, kernel_size = 5, strides=3, activation=swish))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(BatchNormalization())
model.add(Conv2D(128, kernel_size = 7, strides=2, padding='same', activation=swish))
model.add(BatchNormalization())
model.add(Conv2D(256, kernel_size = 9, strides=2, padding='same', activation=swish))
model.add(BatchNormalization())
model.add(Dropout(0.3))
model.add(Conv2D(64, kernel_size = 2, strides=2, padding='same', activation=swish))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(BatchNormalization())
# model.add(Dropout(0.3))
model.add(BatchNormalization())
model.add(Flatten())
model.add(Dropout(0.3)) 
model.add(Dense(1024, activation='relu'))
model.add(Dense(512, activation='relu'))
model.add(Dense(1024, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(10, activation='softmax'))  

# #?-----------------------------------------------------------------------------------model
# model = Sequential()
# model.add(Conv2D(32, kernel_size = 3, activation='swish', input_shape = X.shape[1:]))
# model.add(BatchNormalization())
# model.add(Conv2D(256, kernel_size = 5, strides=3, activation=swish))
# model.add(MaxPooling2D(pool_size=(2,2)))
# model.add(BatchNormalization())
# model.add(Conv2D(256, kernel_size = 2, strides=2, padding='same', activation=swish))
# model.add(BatchNormalization())
# model.add(Dropout(0.3))
# model.add(Conv2D(64, kernel_size = 2, strides=2, padding='same', activation=swish))
# model.add(MaxPooling2D(pool_size=(2,2)))
# model.add(BatchNormalization())
# model.add(Dropout(0.3))
# model.add(BatchNormalization())
# model.add(Flatten())
# model.add(Dropout(0.3))
# model.add(Dense(1024, activation='relu'))
# model.add(Dense(512, activation=swish))
# model.add(Dense(1024, activation='relu'))
# model.add(Dense(512, activation=swish))
# model.add(Dense(64, activation=swish))
# model.add(Dense(10, activation='softmax'))  
# #?-----------------------------------------------------------------------------------model
# opt=tf.keras.optimizers.Adam(learning_rate=0.01)   
model.compile(optimizer='Adam', loss="sparse_categorical_crossentropy", metrics=["accuracy"]) 
# model.compile(loss="binary_crossentropy",optimizer="Adam",metrics=['accuracy'])

model.fit(X, y, batch_size=32,epochs=6, validation_split=0.1)
print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||son")

score=model.evaluate(X2,y2,verbose=0)
print("Test loss= ",score[0])
print("Test  acc= ",score[1])

# print(X[1])
# print("---------------------------->")
#* atlara bak->kopeklere bak->.... klasordeki ttum fotograflara bakip sonra diger klasore geciyoruz.