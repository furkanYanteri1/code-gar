/**************************************************************************** 
**     SAKARYA UNIVERSITY 
**        BILGISAYAR MUHENDISLIGI BOLUMU 
**          VERI YAPILARI  
**     
**    OGRENCI ISMI.....: Furkan Yanteri
**    OGRENCI NUMARASI.: B181210380
****************************************************************************/ 
#include<iostream>
#include<fstream>
#include"Yonetim.hpp"
using namespace std;
int main()
{
    Yonetim* yonetici=new Yonetim();

    yonetici->dosyadanOku();
    yonetici->oynatBakalim();

    return 0; 
}
