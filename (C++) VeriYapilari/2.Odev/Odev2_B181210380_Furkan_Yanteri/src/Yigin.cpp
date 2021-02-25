/**************************************************************************** 
**     SAKARYA UNIVERSITY 
**        BILGISAYAR MUHENDISLIGI BOLUMU 
**          VERI YAPILARI  
**     
**    OGRENCI ISMI.....: Furkan Yanteri
**    OGRENCI NUMARASI.: B181210380
****************************************************************************/ 
#include"Yigin.hpp"
Yigin::Yigin()
{
	elemanSayisi = 0;
}

bool Yigin::ekle(char yeniEleman)
{
	if (elemanSayisi < MAX_LIMIT)
	{
		veriler[elemanSayisi] = yeniEleman;
		elemanSayisi++;

		return true;
	}

	return false;
}

bool Yigin::cikar()
{
	if (elemanSayisi > 0)
	{
		elemanSayisi--;

		return true;
	}

	return false;
	
}

char Yigin::enUstGetir()
{
	if (elemanSayisi > 0)
	{
		return veriler[elemanSayisi - 1];
	}
	return -1;
}

bool Yigin::bosmu()
{
	if (elemanSayisi == 0)
		return true;
	else
		return false;
}
bool Yigin::fullmu()
{
	if (elemanSayisi == 10)
		return true;
	else
		return false;
}
char Yigin::veri(int m)
{
	return veriler[m];
}