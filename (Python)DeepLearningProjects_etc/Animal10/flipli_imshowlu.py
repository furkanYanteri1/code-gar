import numpy as np
import cv2
import os
import matplotlib.pyplot as plt
def yatay_yansit(arr):
    boyutArray=len(arr)
    boyut=boyutArray-1#boyutun bir eksigini alacagiz array 0 dan basliyor lazim oldu iste uzatma
    for i in range(boyut):
        for j in range(int(boyutArray/2)):
            temp=arr[i][j]
            arr[i][j]=arr[i][boyut-j]
            arr[i][boyut-j]=temp
DATADIR="C:\\Users\\furkanyanteri\\Desktop\\Guncel\\animals10\\hayvanat2\\"
TURLER=["kedi","kelebek","kopek","koyun","orumcek","sincap","tavuk"]
training_data=[]
IMG_SIZE=70#6
for tur in TURLER:
    path=os.path.join(DATADIR,tur)
    tur_numarasi=TURLER.index(tur)
    print(len(os.listdir(path))) #* ---> O pathtedi img sayisi
    for img in os.listdir(path):
        try:
            img_array=cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
            img_array2=cv2.flip(img_array, 1) 
            new_array=cv2.resize(img_array,(IMG_SIZE,IMG_SIZE)) #*tum fotograflari ortak boyutta normalize inceleyelim
            new_array2=cv2.resize(img_array2,(IMG_SIZE,IMG_SIZE)) #*tum fotograflari ortak boyutta normalize inceleyelim
            plt.imshow(new_array,cmap="gray")
            plt.show() 
            plt.imshow(new_array2,cmap="gray")
            plt.show()
            # training_data.append([new_array,tur_numarasi])
            # training_data.append([new_array[::-1],tur_numarasi])
            # print(img)
        except Exception as e:
            pass 
