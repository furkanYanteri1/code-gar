#ifndef Sinif_hpp
#define Sinif_hpp
#include "Ogrenci.hpp"
class Sinif
{
  public:
    Sinif();

    int randomizer();//rastgele sayida ogrenci eklemek icin gereken rastgele integeri ureten
    int OgrenciSayisi;
    int sinifNo;//hangi sinif (kacinci sinif?)
    void elemanEkle(int veri);
    void sil(int veri);
    void yazdir();

    Ogrenci*  ilkOgrenci;
    ~Sinif();
};


#endif