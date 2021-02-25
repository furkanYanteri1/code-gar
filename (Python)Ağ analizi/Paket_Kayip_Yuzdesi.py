import matplotlib.pyplot as plt1
toplac=[];##icerisinde tutma icin gerekli.Sonradan append ile dolduracagiz
zamanci=[];#grafigi zaman eksenine gore cizmeye calisalim duvar saati
file = open("iz.tr", "r") 
byte_kayip=0 #kaybolan paketlerin byte cinsinden toplam buyuklugu
byte_toplam=0 #butun paketler icin sizelari toplayalim oranlamak icin
for line in file:
  #satiri ' ' karakterleriyle bolup verilerimizi alalim
  fields = line.split(" ")
  event = fields[0]
  time = float(fields[1])
  pkt_size = float(fields[5])
  if event=="d":
    byte_kayip+=pkt_size #paket kayip ise kayip bytler silsilesine bir yenisini daha ekle
  byte_toplam+=pkt_size #kayipsa da degilse de paket boyutuna ekle cunku bu ornek uzay teskil eder

  toplac.append(byte_kayip/byte_toplam*100) #100 ile carpmamim sebebi bu ihtimali yuzdelik olarak gostermek
  zamanci.append(time)

print("-----> Paket Kayip Yuzdesi Maksimum Degeri:",max(toplac))
print("-----> Paket Kayip Yuzdesi Ortalama Degeri:",sum(toplac)/len(toplac))

#plt1.plot(toplac)
plt1.plot(zamanci,toplac)
plt1.xlabel=("zaman")
plt1.ylabel=("Paket Kayip Yuzdesi")
plt1.show()
file.close()
