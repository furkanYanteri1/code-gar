/**************************************************************************** 
**     SAKARYA UNIVERSITY 
**        BILGISAYAR MUHENDISLIGI BOLUMU 
**          VERI YAPILARI  
**     
**    OGRENCI ISMI.....: Furkan Yanteri
**    OGRENCI NUMARASI.: B181210380
****************************************************************************/ 
#ifndef YiginDizisi_hpp
#define YiginDizisi_hpp
#include "Yigin.hpp"
using namespace std;
class YiginDizisi
{
public:
    YiginDizisi(int size);
    void elemanekle(int a, char x);
    void Goster();
    void Cikar(int k);
    Yigin* yiginlar;
    int eleman_sayisi;
private:
};
#endif




