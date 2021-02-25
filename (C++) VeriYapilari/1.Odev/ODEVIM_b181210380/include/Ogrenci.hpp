#ifndef Dugum_hpp
#define Dugum_hpp

class Ogrenci
{
  public:
    Ogrenci(int numara);
    Ogrenci();//kullandigim bu ogrenci olustururken (sinif classinda) numara vermeyecegiz 
    Ogrenci* sonraki;  
    int numara;
};


#endif