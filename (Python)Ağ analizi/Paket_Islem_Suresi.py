import matplotlib.pyplot as plt1
toplac=[];##icerisinde tutma icin gerekli.Sonradan append ile dolduracagiz
file = open("iz.tr", "r") 
pkt_id_bakilan=0 #paket idlerinin degisimi olmasi durumu kiyas setimiz olacagi icin .tr dosyasindaki ilk pkt_id sini verdim 
pkt_ilk_zaman=1.10531
paket_son_zaman=0
for line in file:
  
  #satiri ' ' karakterleriyle bolup verilerimizi alalim
  fields = line.split(" ")
  #hocam burada ingilizce isimleri kullaniyorum mecburen kusura bakmayiniz
  time = float(fields[1])
  event = fields[0]
  pkt_id = fields[11]
#  print(float(time)+2) #burada sayisal deger basiyoruz
  if pkt_id != pkt_id_bakilan:
    toplac.append(abs(paket_son_zaman-pkt_ilk_zaman))
    pkt_id_bakilan=pkt_id
    pkt_ilk_zaman=time
  else:
    paket_son_zaman=time
#plt1.plot(toplac)
toplac.remove(toplac[toplac.index(max(toplac))])#hocam grafigi dogru cizmek icin en bastaki elemani egale ettim yani hatali degeri 

print("Ortalama deger:",sum(toplac)/len(toplac))

plt1.plot(toplac)
plt1.ylim(min(toplac),max(toplac))
plt1.xlim(1)#burada 0. elementi gostermedim cunku bir ust satirda grafigi netlestirmek icin max ve min degerler arasina sikistiriyorum->
plt1.xlabel=("PAKETLER")#-> 0. element icin 0 dan 1 e cikan dikme grafigi bozmasin diye grafigi hicbirsekilde bozmuyor test edildi.
plt1.ylabel=("PAKET ISLEM SURESI")
#fig=plt1.subplot() #hocam burayi kapattim ortalamayi cizdirmek icin yaptim gormek isterseniz acabilirsiniz
#fig.axhline((sum(toplac)/len(toplac)),color='r',linestyle='--') #usttekinin devami
plt1.show()
 #Print the song
 # print(event+" | "+time+" | "+from_node+" | "+to_node+" | "+pkt_type+" | "+pkt_size+" | "+flags+" | "+fid+" | "+src_addr+" | "+dst_addr+" | "+seq_num+" | "+pkt_id)

#It is good practice to close the file at the end to free up resources   
file.close()
