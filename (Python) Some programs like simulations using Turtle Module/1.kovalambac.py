#Furkan Yanteri
from turtle import Turtle, Screen

ekran = Screen()
ekran.screensize(500, 500)
ekran.title("SAG ve SOL yon tuslariyla mavi ucagi yonlendirin ve ikmal ucagi(kirmizi) ile uygun sekilde ikmal manevrasina girmeye calisin ve ikmali baslatmak icin 'i' tusuna basin     Cikmak icin 'esc' tusuna basiniz" )

ucak = Turtle()
ucak.speed("fastest")
ucak.color("blue")
ucak.penup()
ucak.setposition(250, 250)
ucak.pendown()
ucak_birim_adim=3

kovalambac = Turtle()
kovalambac.shape('triangle')
kovalambac.speed("fastest")
kovalambac.color("red")
kovalambac.penup()
kovalambac.setposition(-250, -250)
kovalambac.pendown()
kovalambac_birim_adim=2

def sol():
    ucak.left(15)

def sag():
    ucak.right(15)

def bitir():
    ekran.bye()

    
def kovalambac_ucak(f_birim_adim_yerel,r_birim_adim_yerel):
    kovalambac.setheading(kovalambac.towards(ucak))
    kovalambac.forward(f_birim_adim_yerel)
    ucak.forward(r_birim_adim_yerel)
    ekran.ontimer(kovalambac_ucak(f_birim_adim_yerel,r_birim_adim_yerel), 10)

def ikmalbaslat():
    kovalambac.color('green')
    kovalambac_birim_adim=3
    kovalambac_ucak(kovalambac_birim_adim,ucak_birim_adim)

ekran.onkey(sol, "Left")  # the left arrow key
ekran.onkey(sag, "Right")  # you get it!
ekran.onkey(bitir, 'Escape')
ekran.onkey(ikmalbaslat,'i')

ekran.listen()
kovalambac_ucak(kovalambac_birim_adim,ucak_birim_adim)

ekran.mainloop()
#Furkan Yanteri