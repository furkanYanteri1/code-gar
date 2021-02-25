/**************************************************************************** 
**     SAKARYA UNIVERSITY 
**        BILGISAYAR MUHENDISLIGI BOLUMU 
**          VERI YAPILARI  
**     
**    OGRENCI ISMI.....: Furkan Yanteri
**    OGRENCI NUMARASI.: B181210380
****************************************************************************/ 
#ifndef Stack_hpp
#define Stack_hpp
class Yigin
{
public:
	const static int MAX_LIMIT = 10;

	Yigin();
	bool ekle(char yeniEleman);
	bool cikar();
	char enUstGetir();
	bool bosmu();
	bool fullmu();
	int elemanSayisi;
	char veri(int m);
private:

	char veriler[MAX_LIMIT];
};
#endif
