/**************************************************************************** 
**     SAKARYA UNIVERSITY 
**        BILGISAYAR MUHENDISLIGI BOLUMU 
**          VERI YAPILARI  
**     
**    OGRENCI ISMI.....: Furkan Yanteri
**    OGRENCI NUMARASI.: B181210380
****************************************************************************/
#include "YiginDizisi.hpp"
#include <iostream>
using namespace std;
YiginDizisi::YiginDizisi(int size)
{
    yiginlar = new Yigin[size];
    eleman_sayisi = size;
}
void YiginDizisi::elemanekle(int a, char x)
{
    yiginlar[a].ekle(x);
}
void YiginDizisi::Goster()
{

    for (int t = 0; t < eleman_sayisi; t++)
        cout << " **" << t + 1 << "**    ";
    cout << "\n";
    for (int i = 0; i < 10; i++)
    {
        for (int j = 0; j < eleman_sayisi; j++)
        {
            if (10 - yiginlar[j].elemanSayisi > i)
            {
                cout << " *   *    ";
                continue;
            }

            // if(yiginlar[j].elemanSayisi>i)
            cout << " * " << yiginlar[j].veri(yiginlar[j].elemanSayisi - ((yiginlar[j].elemanSayisi + i) - 9)) << " *    ";
            //  else
            //    cout<<" * "<<" "<<" *    ";

            //            cout<<" * "<<yiginlar[j].enUstGetir()<<" *    ";
        }
        cout << "\n";
    }
    for (int j = 0; j < eleman_sayisi; j++)
        cout << " *****    ";
}
void YiginDizisi::Cikar(int k) //k is an unimportant number... which stack to put off
{
    yiginlar[k].elemanSayisi--;
}
