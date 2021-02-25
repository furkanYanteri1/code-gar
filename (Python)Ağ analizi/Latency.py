import matplotlib.pyplot as plt1
toplac=[];##icerisinde tutma icin gerekli.Sonradan append ile dolduracagiz
file = open("iz.tr", "r") 
zaman1=zaman2=latency=0 ## Latency icin kullanilacak.Her ardisik iki olayin zamanlarinin farki lazim cunku
for line in file:
  #satiri ' ' karakterleriyle bolup verilerimizi alalim
  fields = line.split(" ")
  #hocam burada ingilizce isimleri kullaniyorum mecburen kusura bakmayiniz
  time = fields[1]
#  print(float(time)+2) #burada sayisal deger basiyoruz
  zaman2=float(time)
  if zaman1==0:
    toplac.append(0)
    zaman1=zaman2
    continue
  toplac.append(zaman2-zaman1)
  zaman1=zaman2
plt1.plot(toplac)
plt1.show()
file.close()
