/* Furkan Yanteri*/
#include <stdio.h>
#include <string.h>
void sirala(char sirasiz[12][8], char son_hal[12][8]); //icinde aylar dizisini koyup duzenleyecegim.Void olarak bunu yapiyorum.
int main(void)										   //yukarida son_hal yazan char[][] icin sirali_aylar dizisini verip fonksiyon icinde duzenleme yapilacak.
{
	char aylar[12][8]; //maksimum ay adi uzunlugu 8 (agustos).
	int okutucu = 0;
	char sirali_aylar[12][8]; //siralanmis halini bunun icine dizecegim "sirala" fonksiyonunun icinde
	char *p_aylar[12];
	//------------------------------------------1.kisim-----------------------------aylari kullaniciya okutma------------------------------------->
	do
	{
		printf("%d.ay giriniz:", okutucu + 1);
		scanf("%s", aylar[okutucu]);
		okutucu++;
	} while (okutucu < 12);
	//------------------------------------------1.kisim-----------------------------aylari kullaniciya okutma------------------------------------->

	//-------------2.kisim---------------aylar dizisinin elemanlarinin adreslerini p_aylar icine yerlestirdim------------------------------------->
	int i;
	for (i = 0; i < 12; i++)
	{
		p_aylar[i] = aylar[i];
	}
	//-------------2.kisim---------------aylar dizisinin elemanlarinin adreslerini p_aylar icine yerlestirdim------------------------------------->
	
	sirala(aylar, sirali_aylar); //fonksiyonla sirali_aylar icine alfabetik olarak siraladim
	return (0);
}
	//-------------3.kisim---------------------aylar dizisinin siralanmis halini sirali_aylara dizen fonksiyon------------------------------------->
void sirala(char sirasiz[12][8], char son_hal[12][8])
{
	int i, j;
	char temp[8];
	for (i = 0; i < 12; i++)
	{
		strcpy(son_hal[i], sirasiz[i]);//bu sayede son hale siralama yapacagim ama aylar dizisi degismeyecek ***
	}                                  //mainde aylar dizisini bastirarak degismedigini gorebilirsiniz       ***
	for (i = 0; i < 11; i++)
	{
		for (j = i + 1; j < 12; j++)
		{
			if (strcmp(son_hal[i], son_hal[j]) > 0)//alfabetik olarak ondeyse
			{
				strcpy(temp, son_hal[i]);//kayip yasama
				strcpy(son_hal[i], son_hal[j]);//switch 2.asama
				strcpy(son_hal[j], temp);//switch tamamlandi
			}
		}
	}
	printf("---------------------------------\n");
	for (i = 0; i < 12; i++)//bastirma kismi burada yapiliyor
	{
		printf("-> %s\n", son_hal[i]);
	}
}
	//-------------3.kisim---------------------aylar dizisinin siralanmis halini sirali_aylara dizen fonksiyon------------------------------------->











/* Furkan Yanteri*/



