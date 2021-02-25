/*
Furkan Yanteri

*/
#include <iostream>
#include <string>
#include <math.h>
#include <sstream> 

using namespace std;
//S-box Tablolari
    int s[8][4][16]= 
    {{ 
        14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7, 
        0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8, 
        4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0, 
        15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13 
    }, 
    { 
        15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10, 
        3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5, 
        0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15, 
        13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9 
    }, 
  
  
    { 
        10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8, 
        13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1, 
        13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7, 
        1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12 
    }, 
    { 
        7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15, 
        13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9, 
        10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4, 
        3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14 
    }, 
    { 
        2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9, 
        14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6, 
        4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14, 
        11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3 
    }, 
    { 
        12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11, 
        10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8, 
        9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6, 
        4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13 
    }, 
    { 
        4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1, 
        13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6, 
        1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2, 
        6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12 
    }, 
    { 
        13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7, 
        1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2, 
        7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8, 
        2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11 
    }}; 
class Metin
{
public:
    string sag, sol, tekParca;
    Metin(string x) //metin 32bit sag ve 32bit sol parcadan olusur
    {
        for (int i = 0; i < 32; i++)
            sol += x.at(i);
        for (int i = 32; i < 64; i++)
            sag += x.at(i);
        tekParca = sol + sag;
    };
    Metin()
    {

    }
     //metin 32bit sag ve 32bit sol parcadan olusur

};
class Anahtar
{
public:
    string sag,sol,tekParca;
    string anahtarlar[16];
     
    Anahtar(string x)
    {
        int k=1;//burada k cok onemli asagiya bak
        for (int i = 1; i < 9; i++)
        {
            x.erase(x.begin() + 8*i-k);//eger k yi artirmazsam yanlis pozisyondaki karakteri silmeye calisir bir sure sonra disari cikarim, bakilmali..fancy
            k++;
        }
        tekParca=x;
        for (int i = 0; i < 28; i++)//iki parca icin de
            sol+=tekParca.at(i);        
        for (int i = 28; i < 56; i++)//iki parca icin de
            sag+=tekParca.at(i);        
        for (int i = 0; i < 16; i++)
        {
            anahtarlar[i]=sol.substr(4,28)+sag.substr(0,24);//cok iyi kod -> des anahtari olusturulurkenki o circular swapimsi muhabbete geliyoruz
            sol=sol.substr(1,27)+sol.substr(0,1);//bu alttakinin aynisi
            sag=sag.substr(1,27)+sag.substr(0,1);//key olustururken ortadaki 48den sonra circular rotasyon yapalim
        }
        
    }
};
string Digitize(char x);        //bir harfi digitize edecegiz 8 bit ile
void DigitizeGoster(string x);  //digitize edilmis mesaji gostermek icin kullanacagim
string XOR(string x, string y); //herhangi 2 x ve y stringleri icin XOR yapma fonksiyonu
string Genislet(string x);
string sBoxlama(string x);
string DesSifrele(Metin metin,Anahtar AnahtarDes);


//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\|
int main()
{

    string metin_girdi, anahtar_girdi, temp; //temp gecici olarak kullanilacak metin_girdi giriste alinacak metin 4 harflik.
    do
    {
        cout << "Sifrelemek istediginiz blogu giriniz (64 bit)(8 HARF): ";
        cin >> metin_girdi;
    } while (metin_girdi.length() != 8);                                                                                                                                                                                                                  //Tam 8 Harften (8*8=64 bit)
    temp = Digitize(metin_girdi.at(0)) + Digitize(metin_girdi.at(1)) + Digitize(metin_girdi.at(2)) + Digitize(metin_girdi.at(3)) + Digitize(metin_girdi.at(4)) + Digitize(metin_girdi.at(5)) + Digitize(metin_girdi.at(6)) + Digitize(metin_girdi.at(7)); //metin nesnesi olusturmak icin artik hazirim
    Metin metinim(temp);//Metin nesnemiz hazir   

    do
    {
        cout << "Anahtar giriniz (64 bit)(8 HARF): ";
        cin >> anahtar_girdi;
    } while (anahtar_girdi.length() != 8);
    temp = Digitize(anahtar_girdi.at(0)) + Digitize(anahtar_girdi.at(1)) + Digitize(anahtar_girdi.at(2)) + Digitize(anahtar_girdi.at(3)) + Digitize(anahtar_girdi.at(4)) + Digitize(anahtar_girdi.at(5)) + Digitize(anahtar_girdi.at(6)) + Digitize(anahtar_girdi.at(7)); //metin nesnesi olusturmak icin artik hazirim
    Anahtar anahtarim(temp);

    Metin gecici_metin;    
    for (int i = 0; i < 16; i++)
    {
        gecici_metin.sol=metinim.sag;
//        gecici.sag = sBoxlama(XOR(Genislet(metin.sag), anahtar.anahtarlar[0]));
        gecici_metin.sag=sBoxlama(XOR(Genislet(metinim.sag), anahtarim.anahtarlar[i]));
 //       gecici.tekParca = gecici.sol + gecici.sag;
        gecici_metin.tekParca=gecici_metin.sol+gecici_metin.sag;
  //      metin = gecici; //bu sefer bunla calistir sac orgusu model
        metinim=gecici_metin;
    }
        cout<<metinim.tekParca;
    

    //cout<<"++"<<DesSifrele(metinim,anahtarim)<<endl;

 //string xx="111100001111000011110000111100001111000011110000";
 //cout<<"++ "<<sBoxlama(xx)<<" ++"<<endl;
 string son;
 cin>>son;
  
    return 0;
}
string Digitize(char x)
{
    string str;   //en son digitleri string olarak dondurelim
    int harf = x; //ilk once harfi integera cevirelim
    int digitler[8] = {0, 0, 0, 0, 0, 0, 0, 0};
    for (int i = 7; i >= 0; i--)
    {
        if (harf >= pow(2, i)) //bir sayiyi 2lik tabanda (binary) ifade etmek icin yaptigimiz hareket
        {
            digitler[7 - i] = 1;
            harf -= pow(2, i);
        }

        str += to_string(digitler[7 - i]); //yerel olarak kullandigimiz gecici str stringine ekle
    }
    return str;
}
void DigitizeGoster(string x) //digitize edilmis mesaji gostermek icin kullanacagim
{
    for (int i = 0; i < x.size(); i++)
    {
        cout << Digitize(x.at(i));
        if (i != x.size() - 1)
            cout << " | ";
    }
}
string XOR(string x, string y)
{
    string temp;                  //gecici , asagida donuste kullanacagim
    if (x.length() != y.length()) //xor lanmak istenen iki stringin uzunlugu ayni olmasi sart
        return "***HATA";
    for (int i = 0; i < x.length(); i++) //x veya y farketmez
    {
        if (x.at(i) == y.at(i))
            temp += '0';
        else
            temp += '1';
    }
    return temp;
}
string Genislet(string x)//32 biti 48 bite cikarirken kullanicaz
{
    char eklenecekler[14];//2 tane de sunlar:1.sona ve sonuncu 1e
    eklenecekler[0]=x.at(5);
    eklenecekler[1]=x.at(4);
    eklenecekler[2]=x.at(9);
    eklenecekler[3]=x.at(8);
    eklenecekler[4]=x.at(13);
    eklenecekler[5]=x.at(12);
    eklenecekler[6]=x.at(17);
    eklenecekler[7]=x.at(16);
    eklenecekler[8]=x.at(21);
    eklenecekler[9]=x.at(20);
    eklenecekler[10]=x.at(25);
    eklenecekler[11]=x.at(24);
    eklenecekler[12]=x.at(29);
    eklenecekler[13]=x.at(28);

    x.insert(0,1,x.at(31));
    x.insert(4,1,eklenecekler[0]);
    x.insert(5,1,eklenecekler[1]);
    x.insert(10,1,eklenecekler[2]);
    x.insert(11,1,eklenecekler[3]);
    x.insert(16,1,eklenecekler[4]);
    x.insert(17,1,eklenecekler[5]);
    x.insert(22,1,eklenecekler[6]);
    x.insert(23,1,eklenecekler[7]);
    x.insert(28,1,eklenecekler[8]);
    x.insert(29,1,eklenecekler[9]);
    x.insert(34,1,eklenecekler[10]);
    x.insert(35,1,eklenecekler[11]);
    x.insert(40,1,eklenecekler[12]);
    x.insert(41,1,eklenecekler[13]);
    x.insert(46,1,x.at(1));
    return x;
}
string sBoxlama(string x) //x stringi 48 haneden olusmali ve bu sonucta xboxlarla 32bite dusecek ve o 32biti ifade eden string donecek
{
    string donus_string; //donuste gonderecegim son(final) string
    if (x.size() != 48)
    {
        cout << "----HATA---sbox" << endl;
        return " ";
    }
    string Girecekler[8]; //48lik stringi 8 tane 6 lik es parcaya bolelim.
    for (int i = 0; i < 48; i++)
    {
        Girecekler[i / 6] += x.at(i);
    }
    int cevirilmis;
    int row, column; //asagida row ve column bulacagiz sbox icin
    for (int i = 0; i < 8; i++)
    {
        stringstream cevirici; //stringden integer olarak aldim
        cevirici << Girecekler[i];
        cevirici >> cevirilmis;
        row = 2 * cevirilmis / 100000 + cevirilmis % 10;
        column = (cevirilmis % 100) / 10 + (cevirilmis % 1000) / 100 * 2 + (cevirilmis % 10000) / 1000 * 4 + (cevirilmis % 100000) / 10000 * 8; //column degerini bulduk
        donus_string += Digitize(s[1][row][column]).substr(4, 7);
    }
    return donus_string;
}
string DesSifrele(Metin metin,Anahtar AnahtarDes)
{
    string str;//simdi anahtarda kullanacagim
    Anahtar anahtar=AnahtarDes;
    cout<<"test"<<endl;
    //Metin gecici("0000000000000000000000000000000000000000000000000000000000000000"); //gecici olarak kullanacagim bir Metin nesnesi bilerek hepsini initial 0 yaptim
    Metin gecici;
    for (int i = 0; i < 15; i++)
    {
    gecici.sol=metin.sag;
    //gecici.sag=sBoxlama( XOR(Genislet(metin.sag) , anahtar.anahtarlar[0]) );
    gecici.sag=sBoxlama( XOR(Genislet(metin.sag) , anahtar.anahtarlar[0]) );
    gecici.tekParca=gecici.sol+gecici.sag;
    metin=gecici;//bu sefer bunla calistir sac orgusu modeli yani
    }
    cout<<"------------------2"<<gecici.tekParca<<"------------------2"<<endl;
    return metin.tekParca;
    
    //gecici.sol = metin.sag; //bir tarafi direkt geciriyorduk ya orasi iste
    
    
    
}