import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import random
from tensorflow import keras
from tensorflow.keras import layers

DATADIR="C:\\Users\\furkanyanteri\\Desktop\\Guncel\\animals10\\hayvanat2\\"
TURLER=["at","fil","inek","kedi","kelebek","kopek","koyun","orumcek","sincap","tavuk"]
training_data=[]
test_data=[]
input_shape = (100, 100, 1)
num_classes=10
for tur in TURLER:
    path=os.path.join(DATADIR,tur)
    tur_numarasi=TURLER.index(tur)
    # print(len(os.listdir(path))) #* ---> O pathtedi img sayisi
    for img in os.listdir(path):
        try:
            img_array=cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
            normalized_array=cv2.resize(img_array,(100,100)) #*tum fotograflari 100*100 olarak ortak boyutta normalize inceleyelim
            training_data.append([normalized_array,tur_numarasi])
        except Exception as e:
            plt.imshow(img_array,cmap="gray")
            plt.show()
            pass 
        # break
    # print (len(img_array))
    # break
print(len(training_data))
random.shuffle(training_data)
x_train=[]
y_train=[]
for features,label in training_data:
    x_train.append(features)
    y_train.append(label)

#---------------------------------------------------------------------------------------------------------------------------------------------------
DATADIR="C:\\Users\\furkanyanteri\\Desktop\\Guncel\\animals10\\hayvanat_test\\"
for tur in TURLER:
    path=os.path.join(DATADIR,tur)
    tur_numarasi=TURLER.index(tur)
    # print(len(os.listdir(path))) #* ---> O pathtedi img sayisi
    for img in os.listdir(path):
        try:
            img_array=cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
            normalized_array=cv2.resize(img_array,(100,100)) #*tum fotograflari 100*100 olarak ortak boyutta normalize inceleyelim
            test_data.append([normalized_array,tur_numarasi])
        except Exception as e:
            plt.imshow(img_array,cmap="gray")
            plt.show()
            pass 
random.shuffle(test_data)
x_test=[]
y_test=[]
for features,label in test_data:
    x_test.append(features)
    y_test.append(label)
#---------------------------------------------------------------------------------------------------------------------------------------------------
# x_train = x_train.astype("float32") / 255
x_train = np.array(x_train,dtype=np.float32)
x_test = np.array(x_test,dtype=np.float32)

y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

model = keras.Sequential(
    [
        keras.Input(shape=input_shape),
        layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        #layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        #layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation="softmax"),
    ]
)
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
model.fit(x_train, y_train, batch_size=32, epochs=1, validation_split=0.3)

score = model.evaluate(x_test, y_test, verbose=0)
print(score)
print("Test loss:", score[0])
print("Test accuracy:", score[1])
print("------------------->")

# for element in y:
#     print(element)

    #! atlara bak->kopeklere bak->.... klasordeki ttum fotograflara bakip sonra diger klasore geciyoruz.