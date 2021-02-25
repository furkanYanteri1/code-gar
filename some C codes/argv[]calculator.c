#include<stdio.h>
#include<stdlib.h>
//not islem sonucunu virgulden sonra iki basamak olacak sekilde ayarladim
int main(int argc, char const *argv[])
{
    double sayi1,sayi2;//islem yapilacak olan iki sayi
    char islec;//isleci icinde tutacagimiz char degiskeni

    sayi1=strtol(argv[1],NULL,10);//argv[] icerisinde bilgi string bunu strtol ile double haline getirdim
    islec=argv[2][0];//islecimizi aldik
    sayi2=strtol(argv[3],NULL,10);
    switch (islec)
    {
        case '+':
            printf("%.2f\n",sayi1+sayi2);
            break;
        case '-':
            printf("%.2f\n",sayi1-sayi2);
            break;
        case 'x'://
            printf("%.2f\n",sayi1*sayi2);
            break;
        case '/':
            printf("%.2f\n",sayi1/sayi2);
            break;
        default:
            printf("\n------------------------------------\nLutfen + - / x operatorlerinden birini kullaniniz.\nNOT:CARPMA ISLEMI ICIN '*' DEGIL 'x' KULLANINIZ \nnot:isletim sistemi kurallarindan dolayi argv[] icinden '*' tek olarak alinamiyor.\n------------------------------------\n" );
            break;
    }
    return 0;
}
