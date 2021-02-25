# SAKARYA UNIVERSITESI BILGISAYAR VE BILISIM BILIMLERI FAKULTESI BILGISAYAR MUHENDISLIGI BOLUMU BITIRME CALISMASI      -EYLUL 2020

# AD: Furkan
# SOYAD: Yanteri
# NU: B181210380
# OGRETMEN: Doc.Dr Ahmet ZENGIN

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

import turtle
import time
from numpy import array
yakinlasma=10
ekran=turtle.Screen()
ekran.title("Ucaklarin nasil ikmal manevrasina girdigini gostermeye yonelik bir simulasyon")
ucak=turtle.Turtle()

ucak.color('red')
ucak.penup()
ucak.setposition(0,-100)
ucak.pendown()
ucak_ikmalci=turtle.Turtle()
ucak.color('blue')
ucak_ikmalci.penup()
ucak_ikmalci.setposition(-100,0)
ucak_ikmalci.pendown()
while ucak.position()!=ucak_ikmalci.position():
    ucak_ikmalci.goto(ucak_ikmalci.xcor()+(ucak.xcor()-ucak_ikmalci.xcor())/yakinlasma,ucak_ikmalci.ycor()+(ucak.ycor()-ucak_ikmalci.ycor())/yakinlasma)
    ucak.left(1)
    ucak.forward(3)
    ucak_ikmalci.setheading(ucak.heading())
    if yakinlasma>=1:
        yakinlasma-=0.02
ekran.exitonclick()
# SAKARYA UNIVERSITESI BILGISAYAR VE BILISIM BILIMLERI FAKULTESI BILGISAYAR MUHENDISLIGI BOLUMU BITIRME CALISMASI      -EYLUL 2020

# AD: Furkan
# SOYAD: Yanteri
# NU: B181210380
# OGRETMEN: Doc.Dr Ahmet ZENGIN

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
