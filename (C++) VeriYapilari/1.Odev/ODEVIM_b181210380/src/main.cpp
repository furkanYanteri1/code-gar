#include <iostream>
//#include "Sinif.hpp"
#include "Okul.hpp"
using namespace std;

int main()
{
  int secim = 0; //ne yapmak istiyorsun?
  int okulunSinifSayisi;
  cout<<"\nKac sinifli bir okul olusturmak istiyorsunuz? : ";
  cin>>okulunSinifSayisi;
  Okul *okul1 = new Okul(okulunSinifSayisi);//n sinifli bir okul olustur...  new Okul(n)  icin n tane sinifi olan okul olusturur.
  okul1->okulYazdir();
  do
  {
    cout << "(1) Ogrenci degistir\n(2) Ogrenci sil\n(3) Ogrenci ekle\n(4)Cikis\nSeciminiz: ";
    cin >> secim; //kullanicidan secim al
    cout << "" << endl;

    if (secim == 1)
      okul1->ogrenciDegistir();
    if (secim == 2)
      okul1->ogrenciSil();
    if (secim == 3)
      okul1->ogrenciEkle();

    okul1->okulYazdir();
  } while (secim != 4);

  //------------------------------------------------temizlik
  okul1->~Okul();

  //------------------------------------------------temizlik

}