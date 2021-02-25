#ifndef Okul_hpp
#define Okul_hpp
#include "Sinif.hpp"
#include <iostream>

class Okul
{
  public:
    Sinif*   Siniflar;//siniflari dinamik bir liste ile tutacagim
    int CursorOgrenciNo;//ogrenci no en son kacta kaldi onun tayini icin
    int sinifSayisi;
    Okul();
    Okul(int SinifSayisi);
    void ogrenciEkle();
    void ogrenciSil();
    void ogrenciDegistir(); 
    void okulYazdir();
    ~Okul();

};


#endif