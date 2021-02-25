import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

tf.compat.v1.disable_eager_execution()#problem
mnist=tf.keras.datasets.mnist # 28*28 el yazisi rakamlar  (datasetimiz)
(x_train , y_train),(x_test , y_test) = mnist.load_data()

#fotograflari normalize ettik
x_train=tf.keras.utils.normalize(x_train,axis=1)
x_test=tf.keras.utils.normalize(x_test,axis=1)

def karsilastir_akt_fonk():
    liste_akt_fonk=[tf.nn.relu, tf.nn.leaky_relu, tf.nn.sigmoid, tf.nn.swish, tf.nn.tanh]
    for i in range(5):
        for j in range(5):
            print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
            print("1.Layer: ",liste_akt_fonk[i].__name__ ,"   <|||>  "," 2.layer: ",liste_akt_fonk[j].__name__)
            print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
            model=tf.keras.models.Sequential()
            model.add(tf.keras.layers.Flatten())
            model.add(tf.keras.layers.Dense(128,activation=liste_akt_fonk[i]))
            model.add(tf.keras.layers.Dense(128,activation=liste_akt_fonk[j]))
            model.add(tf.keras.layers.Dense(10,activation=tf.nn.softmax))
            model.compile(optimizer='adam', #optimizerler -> https://keras.io/api/optimizers/
                        loss='sparse_categorical_crossentropy',  #loss fonksiyonlari -> https://keras.io/api/losses/probabilistic_losses/#categoricalcrossentropy-class
                        metrics=['accuracy'])
            model.fit(x_train,y_train,epochs=3)
            model.save('ilk_model.model')
            new_model=tf.keras.models.load_model('ilk_model.model')
            predictions= new_model.predict([x_test])
karsilastir_akt_fonk()




#------------------------------------
# print(np.argmax(predictions[1]))
# plt.imshow(x_test[1],plt.cm.binary)
# plt.show()
# resim_goster(0)

#print(x_train[0])