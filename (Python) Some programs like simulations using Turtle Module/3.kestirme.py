
# SAKARYA UNIVERSITESI BILGISAYAR VE BILISIM BILIMLERI FAKULTESI BILGISAYAR MUHENDISLIGI BOLUMU BITIRME CALISMASI      -EYLUL 2020

# AD: Furkan
# SOYAD: Yanteri
# NU: B181210380
# OGRETMEN: Doc.Dr Ahmet ZENGIN

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

import turtle
import random
import time
from math import sqrt
ekran=turtle.Screen()
ekran.title("Belirlediginiz donus sayisi kadar 4 yonde rastgele giden bir yolcunun son durak ile ilk durak arasi aldigi esas mesafenin simule edilmesi ")
yolcu = turtle.Turtle()
yolcu.speed(0)

yolcu.color("green")
yolcu.dot(6)  # mark the baslaing location
yolcu.color("black")

directions = ['K', 'G', 'D', 'B']
donus_sayisi=int(ekran.numinput("Lutfen sistemi denemek istediginiz donus sayisini giriniz.", "Donus Sayisi:", "1-300 arasi ideal", minval=1, maxval=1000))

# step_size = 20
adim_boyu=[5,10,15,20,25,30]
basla = time.time()

for i in range(donus_sayisi):

    heading = random.choice(directions)

    if heading == 'K':#kuzey
        yolcu.setheading(90)
    elif heading == 'G':#guney
        yolcu.setheading(270)
    elif heading == 'D':#dogu
        yolcu.setheading(0)
    else:#bati
        yolcu.setheading(180)

    # yolcu.forward(step_size)
    yolcu.forward(random.choice(adim_boyu))

(x,y) = yolcu.position()

mesafe = sqrt( x**2 + y**2 )

bitir = time.time()

yolcu.color("red")    # mark the bitir location
yolcu.dot(6)
yolcu.hideturtle()

# drawing the final mesafe: basla to bitir
kestirme = turtle.Turtle()
kestirme.color("blue")
kestirme.goto(x,y)
kestirme.hideturtle()

print("Toplam zaman:", bitir - basla)
print("Toplam donus sayisi:", donus_sayisi)
print("Toplam mesafe:", mesafe)
ekran.mainloop()
# SAKARYA UNIVERSITESI BILGISAYAR VE BILISIM BILIMLERI FAKULTESI BILGISAYAR MUHENDISLIGI BOLUMU BITIRME CALISMASI      -EYLUL 2020

# AD: Furkan
# SOYAD: Yanteri
# NU: B181210380
# OGRETMEN: Doc.Dr Ahmet ZENGIN

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
