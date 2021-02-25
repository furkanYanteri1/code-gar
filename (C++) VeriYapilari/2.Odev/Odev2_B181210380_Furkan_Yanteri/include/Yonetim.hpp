/**************************************************************************** 
**     SAKARYA UNIVERSITY 
**        BILGISAYAR MUHENDISLIGI BOLUMU 
**          VERI YAPILARI  
**     
**    OGRENCI ISMI.....: Furkan Yanteri
**    OGRENCI NUMARASI.: B181210380
****************************************************************************/ 
#ifndef Yonetim_hpp
#define Yonetim_hpp
#include "YiginDizisi.hpp"
#include <fstream>
#include <iostream>
#include<stdlib.h>

using namespace std;
class Yonetim
{
public:
    Yonetim();
    void dosyadanOku();
    void oynatBakalim();

    YiginDizisi* yiginDizisi1;
};
#endif