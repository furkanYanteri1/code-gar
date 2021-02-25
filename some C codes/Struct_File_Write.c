#include <stdio.h>
#include <string.h>
typedef struct ogrenci_not_bilgileri
{
	char isim[20];
	float vize,final;
}onb;
//struct istenen sekilde tanimlandi fakat islemleri karisikliktan kurtarmak icin typedef anahtar sozcugu kulandim.
//bu sayede ONB dedigim anda struct ogrenci_not_bilgileri kastedilecek ve kelime fazlaligindan kurtularak temiz bir kod yazacagim.
onb not_bilgileri_al(float vize_not,float final_not)
{
	onb ogrenci;
	ogrenci.vize=vize_not;
	ogrenci.final=final_not;
	return ogrenci;
}
int main() 
{
	FILE* fp;
	fp=fopen("ogrenci.txt","w");//ogrenci bilgilerini icine yazacagimiz .txt dosyasi

	onb OGRENCILER[10];// tum ogrenciler bunun icinde olacak
	int i=0;//sayac
	float tmp1,tmp2;//dongu ivinde not alirken kullanilacak
	char tmp3[20];//isim icin gecici olan
	while (i<10)
	{
		printf("%d.ogrenci vize notu giriniz:",i+1);
		scanf("%f",&tmp1);
		printf("%d.ogrenci final notu giriniz:",i+1);
		scanf("%f",&tmp2);
		OGRENCILER[i].vize=not_bilgileri_al(tmp1,tmp2).vize;//verilaeri almak icin odevde istendigi gibi not_bilgiler_ial fonksiyonunu kullandim
		OGRENCILER[i].final=not_bilgileri_al(tmp1,tmp2).final;
		sprintf(tmp3,"%d.ogrenci",i+1);//Ogrenci isimleri 1.ogrenci 2.ogrenci ... seklinde gidecek.
		strcpy(OGRENCILER[i].isim,tmp3);
		i++;
	}

	i=0;//dongu sayacini sifirlayalim
	while (i<10)
	{
		fprintf(fp,"ISIM: %s   Vize:%.2f   Final:%.2f   Ortalama=%.2f\n",OGRENCILER[i].isim,OGRENCILER[i].vize,OGRENCILER[i].final,(OGRENCILER[i].vize+OGRENCILER[i].final)/2);
		i++;
	}
	fclose(fp);
	return 0;
}
