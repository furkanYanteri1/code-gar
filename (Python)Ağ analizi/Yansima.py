import matplotlib.pyplot as plt1
toplac=[];##icerisinde tutma icin gerekli.Sonradan append ile dolduracagiz
file = open("iz.tr", "r") 
zaman1=0 #Bir tcpden sonra ne zaman ack gelecek orada kullanalim
anahtar=0
for line in file:
  
  #satiri ' ' karakterleriyle bolup verilerimizi alalim
  fields = line.split(" ")
  #hocam burada ingilizce isimleri kullaniyorum mecburen kusura bakmayiniz
  event= fields[0]
  time = float(fields[1])
  pkt_type = fields[4]
  pkt_id = float(fields[11])
#  print(float(time)+2) #burada sayisal deger basiyoruz
  zaman2=float(time)
  if pkt_type=="tcp" and event=='+':#enque edilen bir tcp
    if anahtar==0:
      zaman1=time
      anahtar=1
    else:
      continue
  elif pkt_type=="ack" and event=='r':#alinan bir ack tipi paket
    toplac.append(time-zaman1)
    anahtar=0
print("--------------")

plt1.plot(toplac)
#ortaci=plt1.subplot()
#ortaci.axhline((sum(toplac)/len(toplac)),color='r',linestyle='--')  
plt1.xlabel=("zaman")
plt1.ylabel=("TCP-ACP arasi gecikme")
plt1.show()
 #Print the song
 # print(event+" | "+time+" | "+from_node+" | "+to_node+" | "+pkt_type+" | "+pkt_size+" | "+flags+" | "+fid+" | "+src_addr+" | "+dst_addr+" | "+seq_num+" | "+pkt_id)

#It is good practice to close the file at the end to free up resources   
file.close()
