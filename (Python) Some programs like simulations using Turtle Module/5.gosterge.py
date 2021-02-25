#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#Furkan Yanteri
import random
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pylab

plt.style.use('fivethirtyeight')
fig = pylab.gcf()
fig.canvas.set_window_title('Ucaklar arasi mesafe, kalan yakit, ortalama sureler, degisker kararlar,... gibi konularda asil sistem uzerinde kullanilabilecek bir kod')

x_degerleri = []
y_degerleri = []

index = count()

def calistir(son_deger):
    x_degerleri.append(next(index))
    y_degerleri.append(random.randint(0, 5))
    plt.cla()
    plt.plot(x_degerleri, y_degerleri)


simule_et = FuncAnimation(plt.gcf(), calistir, 1000)

plt.tight_layout()
plt.show()

