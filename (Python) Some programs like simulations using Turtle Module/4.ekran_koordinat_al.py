#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#Furkan Yanteri
import turtle
ekran=turtle.Screen()
ekran.title("Lutfen koordinatini almak istediginiz noktaya tiklayiniz.Anlik olarak koordinatlar calistirma ortaminizda yazdirilacaktir")
baslangic_koor_liste=[(float,float)]
def ekran_koordinat_al(x, y):
    arr=(x,y)
    baslangic_koor_liste.append(arr)
    print(arr)
turtle.onscreenclick(ekran_koordinat_al)

turtle.mainloop()

