#include "Sinif.hpp"
#include<iostream>
//---------------------------Bu ikisini random sayi uretmek icin kullanacagim.
#include <cstdlib>
#include <ctime>
//---------------------------Bu ikisini random sayi uretmek icin kullanacagim. r10
using namespace std;
int Sinif:: randomizer()
{
  srand((unsigned)time(0));
  int random_integer = 0;
  while (random_integer < 2 || random_integer > 6)//2 ile 6 arasinda bir rastgele sayiya ihtiyacim var
  {
    random_integer = (rand() % 20);// %20 yaptim az da olsa rastgeleligi artirmaya yonelik bir hareket
  }
  return random_integer;
}
Sinif::Sinif()
{
  cout<<""<<endl;
    sinifNo=-2;//sinif nosu verilmemis bir sinifi kolay anlayabilmek ve yakalayabilmek icin boyle yaptim.
    int RandomOgrenciSayisi=randomizer();
    this->OgrenciSayisi=RandomOgrenciSayisi;
    ilkOgrenci=new Ogrenci();
    //ilkOgrenci->numara=13;
    Ogrenci* gecici=ilkOgrenci;
    
    for (int i = 1; i < RandomOgrenciSayisi; i++)//olusturdugumuz 2 ile 6 arasindaki random sayi kadar ogrenci ekleyelim
    {
        gecici->sonraki=new Ogrenci();
      //  gecici->sonraki->numara=(i+1)*10;
        //cout<<gecici->sonraki->numara<<" -> ";
        gecici=gecici->sonraki;
    }
    cout<<" "<<endl;
    gecici->sonraki=0;
   
}
void Sinif::yazdir()
{
  Ogrenci* gezmen = ilkOgrenci;
 // cout<<"gezmen: "<<gezmen->numara<<endl;
  cout<<"------------"<<endl;
  cout<<"| "<<this<<" |"<<endl;
  cout<<"------------   ";
  for (int i = 0; i < OgrenciSayisi; i++)
  {
      cout<<"************   ";
  }
  cout<<""<<endl;

  for (int i = 0; i < OgrenciSayisi + 1; i++)
  {
    if (i == 0)
      cout << "|    " << this->sinifNo << "    |   ";
    else
    {
      cout << "* " << gezmen << " *   ";
      gezmen = gezmen->sonraki;
    }
  }
  cout<<""<<endl;
  for (int i = 0; i < OgrenciSayisi+1; i++)
  {
    if (i==0)
      cout<<"------------   ";
    else    
    cout<<"************   ";
  }
  cout<<""<<endl;
  gezmen=ilkOgrenci;
  for (int i = 0; i < OgrenciSayisi + 1; i++)
  {
    if (i == 0)
      cout << "| " << this->ilkOgrenci << " |   ";
    else
    {
      cout << "*    " << gezmen->numara << "    *   ";
      if (gezmen->sonraki != 0)
        gezmen = gezmen->sonraki;
    }
  }
  cout << "" << endl;
  for (int i = 0; i < OgrenciSayisi+1; i++)
  {
     if (i==0)
      cout<<"------------   ";
    else    
    cout<<"************   ";
  }
  cout<<"\n\n\n";
}
 
void Sinif::elemanEkle(int veri)
{

    
  Ogrenci* gecici = ilkOgrenci;//ilk ogrenciyi kaybetmek istemezsin bro

  while(gecici->sonraki!=0)
  {
    gecici = gecici->sonraki;
  }

  gecici->sonraki = new Ogrenci(veri);
  this->OgrenciSayisi++;
}
void Sinif::sil(int aranan)
{
  if(ilkOgrenci==0)//eleman kalmadiysa
    return;

  if(ilkOgrenci->numara==aranan)
  {
    Ogrenci* silinecek = ilkOgrenci;
    ilkOgrenci = ilkOgrenci->sonraki;
    delete silinecek;
    this->OgrenciSayisi--;
    return;
  }

  Ogrenci* gecici = ilkOgrenci;

  while((gecici->numara!=aranan) && (gecici->sonraki!=0))
  {
    if(gecici->sonraki->numara==aranan)
    {
      Ogrenci* silinecek = gecici->sonraki;
      gecici->sonraki = silinecek->sonraki;
      delete silinecek;
      break;
    }
      gecici = gecici->sonraki;
  }
    this->OgrenciSayisi--;

}
 Sinif::~Sinif()
{
  Ogrenci*gecici1=ilkOgrenci;
  Ogrenci*gecici2=ilkOgrenci->sonraki;
 /* 
  while (ilkOgrenci->sonraki!=0)
  {
    ilkOgrenci=ilkOgrenci->sonraki;
    delete gecici1;
    gecici1=ilkOgrenci;
  }
*/
  delete ilkOgrenci;
  delete gecici1;
  delete gecici2;

} 