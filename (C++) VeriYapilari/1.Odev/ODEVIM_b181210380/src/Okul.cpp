#include "Okul.hpp"
using namespace std;
Okul::Okul()
{
    CursorOgrenciNo=10;//Ogrenci numarasi 10 dan baslayacagi icin
    Siniflar=0;
}
Okul::Okul(int SinifSayisi)
{
    sinifSayisi=SinifSayisi;
    CursorOgrenciNo=10;//Ogrenci numarasi 10 dan baslayacagi icin
    this->Siniflar=new Sinif[SinifSayisi];
    for (int i = 0; i < SinifSayisi; i++)
        Siniflar[i].sinifNo=i+1;//siniflarin sinif Numarasi 1 2 3 ... seklinde olacagindan mutevellit

    Ogrenci* gecici;
    gecici=Siniflar->ilkOgrenci;
    for (int i = 0; i < SinifSayisi; i++)
    {
        gecici=Siniflar[i].ilkOgrenci;
        for (int j = 0; j < Siniflar[i].OgrenciSayisi; j++)
        {
            gecici->numara=CursorOgrenciNo;
            CursorOgrenciNo++;
            gecici=gecici->sonraki;
        }
    }
}

    void Okul::ogrenciDegistir()
    {
        
        int sinif_1,sinif_2;//hangi siniftan hangi sinifa
        int no_1,no_2;//hangi numarali ogrenciler
        
        cout << "Sinif kodu: ";
        cin >> sinif_1;
        cout << "Ogrenci no:";
        cin >> no_1;
        cout << "Sinif kodu: ";
        cin >> sinif_2;
        cout << "Ogrenci no:";
        cin >> no_2;

        Ogrenci *gecici1 =Siniflar[sinif_1 - 1].ilkOgrenci;
        gecici1->sonraki =Siniflar[sinif_1 - 1].ilkOgrenci->sonraki;
        Ogrenci *gecici2 =Siniflar[sinif_2 - 1].ilkOgrenci;
        gecici2->sonraki =Siniflar[sinif_2 - 1].ilkOgrenci->sonraki;
        
        while (gecici1->numara != no_1 && gecici1->sonraki != 0)
        {
            gecici1 = gecici1->sonraki;
        }// bu asamada degistirilecek 1. ogrencinin mekani gecici1 ile sabit

        while (gecici2->numara != no_2 && gecici2->sonraki != 0)
        {
            gecici2 = gecici2->sonraki;
        }// bu asamada degistirilecek 2. ogrencinin mekani gecici2 ile sabit

    //----------------SWAP----------------
        int temp=gecici1->numara;
        gecici1->numara=gecici2->numara;
        gecici2->numara=temp;
        //delete gecici3;
    //----------------SWAP----------------

    }
    void Okul::okulYazdir()
    {
    cout<<"________________________________________________________________________________________\n"<<endl;                       
    
        for (int i = 0; i < sinifSayisi; i++)
        {
            Siniflar[i].yazdir();
        }
   cout<<"________________________________________________________________________________________"<<endl;                       

    } 
    void Okul::ogrenciEkle()
    {
        int sinif_1;//hangi siniftan hangi sinifa
        int no_1;//hangi numarali ogrenciler
        
        cout << "Sinif kodu: ";
        cin >> sinif_1;
        cout << "Ogrenci no:";
        cin >> no_1;
        do
        {
            cout<<"Lutfen baska bir ogrenci numarasi giriniz.."<<endl;
            /* code */
        } while (no_1<=CursorOgrenciNo && no_1>=10);
        Siniflar[sinif_1-1].elemanEkle(no_1); 
    }
    void Okul::ogrenciSil()
    {
        int sinif_1;//hangi siniftan hangi sinifa
        int no_1;//hangi numarali ogrenciler
        
        cout << "Sinif kodu: ";
        cin >> sinif_1;
        cout << "Ogrenci no:";
        cin >> no_1;
        Siniflar[sinif_1-1].sil(no_1); 
    }
    Okul::~Okul()
    {
       
       for (int i = 0; i < sinifSayisi-1; i++)
       {
           Siniflar[i].~Sinif();
           cout<<"asdkjfkasjdf"<<endl;
           /* code */
       }
        delete[] Siniflar;       
        
    }
