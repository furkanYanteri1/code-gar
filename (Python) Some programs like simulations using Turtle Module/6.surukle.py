#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# SAKARYA UNIVERSITESI BILGISAYAR VE BILISIM BILIMLERI FAKULTESI BILGISAYAR MUHENDISLIGI BOLUMU BITIRME CALISMASI      -EYLUL 2020

# AD: Furkan
# SOYAD: Yanteri
# NU: B181210380
# OGRETMEN: Doc.Dr Ahmet ZENGIN

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

import turtle
from turtle import Turtle,Screen

ekran=turtle.Screen()
ekran.title("Lutfen kaplumbagayi istediginiz noktaya surukleyiniz. Anlik olarak biraktiginiz pozisyonun koordinatlari yazdirilir")
t=Turtle("turtle")
t.speed(-1)#6
# t.penup()
def surukle(x,y):
    t.ondrag(None)
    t.setheading(t.towards(x,y))
    t.goto(x,y)
    t.ondrag(surukle)
    print(t.position())
    # print("calisti")

def cizgi_temizle(x,y):
    t.clear()
ucaklar=[]
def main():
    t.ondrag(surukle)
    ucaklar.append(t)
    t.ondrag(surukle)
    ucaklar.append(t)
    turtle.onscreenclick(cizgi_temizle,3)#sag tik ile cizgi temizlenir 3 o
    ekran.mainloop()

main()
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# SAKARYA UNIVERSITESI BILGISAYAR VE BILISIM BILIMLERI FAKULTESI BILGISAYAR MUHENDISLIGI BOLUMU BITIRME CALISMASI      -EYLUL 2020

# AD: Furkan
# SOYAD: Yanteri
# NU: B181210380
# OGRETMEN: Doc.Dr Ahmet ZENGIN

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
