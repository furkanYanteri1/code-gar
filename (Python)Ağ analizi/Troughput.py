import matplotlib.pyplot as plt1
toplac=[]#icerisinde tutma icin gerekli.Sonradan append ile dolduracagiz
saniye=[]#Her satirda yer alan saniye degerlerini de tutuyorum ki saniyeye gore troughput cizebilelim
veri=0#bunu o ana kadar elden gecen verilerin bit olarak toplamini tutmak icin kullanalim
max=0
file = open("iz.tr", "r") 
for line in file:
  
  #satiri ' ' karakterleriyle bolup verilerimizi alalim
  fields = line.split(" ")
  #hocam burada ingilizce isimleri kullaniyorum mecburen kusura bakmayiniz
  event = fields[0]
  time = float(fields[1])
  pkt_size = float(fields[5])

  saniye.append(time)#o anki duvar saatini yani saniye degerini biriktir
#  print(float(time)+2) #burada sayisal deger basiyoruz
  if event=="r":
    veri+=pkt_size*8 #bit olarak kullanacagim cunku bps yani bit/sec olarak geciyor troughput

  toplac.append(veri/time)#burada belli oluyor (toplam veri/o anki zaman) olarak verileri topluyorum
  if veri/time>max:
    max=veri/time
print("--------------Maksimum deger:")
print(max)
print("--------------Ortalama deger:")
print(sum(toplac)/sum(saniye))
plt1.plot(saniye,toplac)#troughput grafigini saniyeye gore ciziyorum duvar saatine
plt1.show()
file.close()
