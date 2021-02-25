#include "Ogrenci.hpp"

Ogrenci::Ogrenci(int numara)
{
    this->numara = numara;
    sonraki=0;
}
Ogrenci::Ogrenci()
{
    this->numara=-1;//numarasi verilmemis ogrencilerin numarasi -1 olsun.Kontrrol saglamak icin
}