#include <stdio.h>
#include <stdlib.h>
char* KatarCevir(char* str);
int main() 
{
	char karakter[100]="merhaba";

	printf("\n Cevrilmis string: %s \n",KatarCevir(karakter));//odevde istendigi gibi fonksiyonu mainde cagirdim
										  //char* dondurdugu icin donmus halini direkt printf ile bastim boylece.
	return 0;
}
char* KatarCevir(char* str)
{
	int i,j;//cevirirken dongude kullanacagim iterator
	int boyut=0;//cevrilecek olan katarin uzunlugunu bulup bu degiskende tutalim
	char* cevrilmis;//cevrilmis olan stringi (fonksiyondan dondurecegim) bunda tutacagim.
//----------------------------------string uzunlugu bulundu
	while (str[boyut]!='\0')
		boyut++;
//----------------------------------string uzunlugu bulundu
	cevrilmis=(char*)malloc(sizeof(char)*boyut);//dondurecegim string icin yer aldim
	j=boyut-1;//gerekli index duzenlemesi
	for (i = 0; i < boyut; i++)//cevirme dongusu
	{
		cevrilmis[i]=*(str+j);//cevirme isleminin yapildigi en onemli kisim! ISTENDIGI GIBI ADRES UZERINDEN ERISME YAPIYORUM.
		j--;
	}
	return cevrilmis;//odevde istendigi gibi donusu char* olarak ayarladim.
}
