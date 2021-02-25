import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from matplotlib import pyplot as plt
import sys

text_file = open("sample.txt", "w")
def isTriangular(sayi):
    temp=sayi
    i=1
    while temp-i>=0:
        temp-=i
        i+=1
    if temp==0:
        result=True
    else:
        result=False
    return result

if isTriangular(10):
    print("-------------------------------")
  
##########################################################################################################################################33

num_classes = 10
input_shape = (28, 28, 1)

#grafik cizecegimiz array
acc_liste=[]
loss_liste=[]
# epoch_sayisi=[1,2,3,4,5]
# epoch_sayisi=[1,2,3,4,5,6,7,8,9,10,11]
epoch_sayisi=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#nokta_degerler=[]#grafik ustunde nokta koyuyoruz ya onlardan hangilerinin degerlerini yanina yazacagimiz icin kulln (yerel max,minler icin)
# dropout_degeri=3.1
dropout_degeri=float(sys.argv[1])

# the data, split between train and test sets
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Scale images to the [0, 1] range
x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255
# Make sure images have shape (28, 28, 1)
x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)
print("x_train shape:", x_train.shape)
print(x_train.shape[0], "train samples")
print(x_test.shape[0], "test samples")

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)
#plt.plot(epoch_sayisi, acc_liste,label='dogruluk')
# plt.stem(epoch_sayisi, acc_liste,use_line_collection=True,label='dogruluk')

# #plt.plot(epoch_sayisi, loss_liste,label='loss')
# plt.xlabel('Epoch Sayisi')
# #plt.ylabel()
# plt.yticks(acc_liste)
# plt.xticks(epoch_sayisi)
# plt.title('Epoch Sayisinin Dogruluk Uzerine Etkisi') 
# #plt.legend()
# #plt.ylim(0.920,0.999)
# plt.show()
#---------------------------------------------------------------------------------------------------------build the model
model = keras.Sequential(
    [
        keras.Input(shape=input_shape),
        layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dropout(dropout_degeri),
        layers.Dense(num_classes, activation="softmax"),
    ]
)
model.summary()
#---------------------------------------------------------------------------------------------------------train the model
batch_size = 128

#model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
#for i in range(len(epoch_sayisi)):
for i in range(len(epoch_sayisi)):
    history=model.fit(x_train, y_train, batch_size=batch_size, epochs=1, validation_split=0.3)
#---------------------------------------------------------------------------------------------------------evaluate the Trained Model
    score = model.evaluate(x_test, y_test, verbose=0)
    # print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    # print("Test loss:", score[0])
    # print("Test accuracy:", score[1])
    # print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    loss_liste.append(score[0])
    acc_liste.append(score[1])
    # plt.text(epoch_sayisi[i],acc_liste[i],acc_liste[0])
    # plt.text(epoch_sayisi[i],acc_liste[i],"{:.3f}".format(acc_liste[i]))


plt.plot(epoch_sayisi, acc_liste, linestyle='dashed', linewidth = 1, marker='o', markerfacecolor='red', markersize=4)
#plt.plot(epoch_sayisi, loss_liste,label='loss')
plt.xlabel('Epoch Sayisi')
plt.ylabel('Doğruluk')
#plt.yticks(acc_liste)
plt.xticks(epoch_sayisi)
#en buyuk elemanlari grafikte yazdirmak icin
plt.ylim(min(acc_liste)-0.04,0.999)
acc_sirali=sorted(acc_liste)
max_acc_index=0

for i in range (len(acc_liste)):
    if(acc_liste[i]==acc_sirali[len(acc_sirali)-1]):
        max_acc_index=i
#birinci ve sonuncu icin yerel max veya min olmasina bakmaksizin yaziyoruz.
plt.text(epoch_sayisi[0],acc_liste[0],"{:.3f}".format(acc_liste[0]))
plt.text(epoch_sayisi[len(epoch_sayisi)-1],acc_liste[len(acc_liste)-1],"{:.3f}".format(acc_liste[len(acc_liste)-1]))

for i in range(len(acc_liste)-2):
    if (acc_liste[i+1]>acc_liste[i] and acc_liste[i+1]>acc_liste[i+2]):
        if i+1 != max_acc_index:
            plt.text(epoch_sayisi[i+1],acc_liste[i+1],"{:.3f}".format(acc_liste[i+1]))
        else:
            plt.text(epoch_sayisi[i+1],acc_liste[i+1],"{:.3f}".format(acc_liste[i+1]),color='red')

# if i==max_acc_index:
#     plt.text(epoch_sayisi[i+1],acc_liste[i+1],"{:.3f}".format(acc_liste[i+1]),color='red')
#     continue



title_model=" Maksimum dogruluk: "+str(max_acc_index+1)+".Epoch'ta ->"+"{:.3f}".format(acc_sirali[len(acc_sirali)-1])+" Dropout->"+"{:.3f}".format(dropout_degeri)
plt.title(title_model)

        

plt.legend()
# plt.show()
isim_graf='dropout'+str("{:.2f}".format(dropout_degeri))+'.png'

text_file.write(str(acc_liste))
text_file.close()
plt.savefig(isim_graf)
keras.backend.clear_session()
