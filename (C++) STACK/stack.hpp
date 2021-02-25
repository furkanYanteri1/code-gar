#if !defined(STACK_HPP)
#define STACK_HPP
class Stack
{

public:
    static const int max_yigin=5;
    Stack(/* args */);
    ~Stack();
    int dizi[max_yigin];
    int top;
    bool Bosmu();//bos mu dolu mu
    bool Ekle(int eklenecek);
    bool Cikar();//burada parametreye ihtiyacim yok cunku lifo vaa ** sadece en ustekini cikar bana dondurme
    bool Getir(int&getirilecek);//en usttekini getir
};

Stack::Stack(/* args */)
{
    top=0;
}

Stack::~Stack()
{
}
bool Stack::Bosmu()
{
    if (top==0)
        return true;//yani bos
    return false;    
}
bool Stack::Ekle(int eklenecek)//burada ekleme yapip yapamadigimizi bilmek icin BOOL.istersen void yap 
{
    if (top<max_yigin)
    {
        dizi[top]=eklenecek;
        top++;
        return true;
    }
    else// Stack doludur ekleme yapamaz
    return false;
}
bool Stack::Cikar()
{
    if (top<=0)//stackta eleman yok nasil cikaracaksin
        return false;    
    else
        {
            top--;
            return true;
        }
}
bool Stack::Getir(int&getirilecek)//buresi baya onemli bu ayrinti bir artistik sart deil ama fark yaratan her sey sart olmayan seylerdir.
{                          //sunu yapiyorum en ustteki veriyi almak icin parametre olarak int& yani referans var
    if (top<=0)            //mainde bir int olusturup onu parametre olarak buna verirsem o integerin degerine
        return -1;         //stackin en ustundeki yani aradigimiz deger gelir ve cout deyip bastirabiliriz.
    getirilecek=dizi[top];
    return true;    
}



#endif // Stack_HPP
