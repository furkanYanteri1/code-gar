#ifndef KUYRUK_HPP
#define KUYRUK_HPP
#include <iostream>
using namespace std;
class Kuyruk
{
public:
    static const int max_size=10;

    Kuyruk(/* args */);
    ~Kuyruk();
    bool elemanEkle(int eklenecek_eleman);
    bool getir(int&getirilen);
    void yazdir();
private:
    int kuyruk_basi;
    int kuyruk_sonu;
    int elemanlar[max_size];
    /* data */

};

Kuyruk::Kuyruk(/* args */)
{
    kuyruk_basi = -1;
    kuyruk_sonu = -1;

}
bool Kuyruk::elemanEkle(int eklenecek_eleman)
{
    if (kuyruk_sonu==-1)//kuyruk bosken eleman eklemek
    {
        kuyruk_sonu=0;
        kuyruk_basi=0;
        elemanlar[kuyruk_sonu]=eklenecek_eleman;
        return true;
        /* code */
    }
    if ((kuyruk_sonu+1)%10!=kuyruk_basi)//burasi cok guzel dairesel kuyrugun felsefesi
    {
        kuyruk_sonu=(kuyruk_sonu+1)%10;
        elemanlar[kuyruk_sonu]=eklenecek_eleman;
        return true;
    }
    
}
void Kuyruk::yazdir()
{
    for (int i = 0; i < max_size; i++)
    {
        cout<<elemanlar[i]<<" ";
    }
}
bool Kuyruk::getir(int&getirilen)
{
    if(kuyruk_basi==-1)//eleman yok nasil getircen
        return false;

    getirilen=elemanlar[kuyruk_basi];
    
    if (kuyruk_basi==kuyruk_sonu)
        kuyruk_basi=kuyruk_sonu=-1;
    else
        kuyruk_basi=(kuyruk_basi+1)%10;
    return true;
}

Kuyruk::~Kuyruk()
{
}

#endif // KUYRUK_HPP
