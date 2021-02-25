#include <iostream>
using namespace std;
int main(int argc, char const *argv[])
{
	int a =5;
	int *aptr=&a;
	cout<<"a = "<<*aptr<<endl;
//---------------------------------------------------------------------------(end of 1) temel pointer bilgisi
	
	cout<<"-------------------------------"<<endl;


	int dizi[]={1,2,3,4,5};

	int *dptr;//diziye iliskin pointer
	dptr=dizi;

	cout<<"dizi 0 ="<<*(dptr+1)<<endl;//dizinin 1. elemanini bas
//---------------------------------------------------------------------------(end of 2) pointer dizi iliskisi
	int *dizi2=new int[10];
	dizi2[0]=67;
	cout<<"dizi2 0 = "<<dizi2[0]<<endl;

	delete[] dizi2;//-------dizi silmek istiyorsan bu sekilde. Dizi degilse normal.
	cout<<"sildigimiz dizinin elemanlari: "<<dizi2[0]<<" , "<<dizi2[1]<<" , "<<dizi2[2]<<" , "<<dizi2[3]<<" ...  diye gidiyor."<<endl;//-gorundugu gibi erisemiyoruz.Aslinda erisiyoruz ama ici bos.bos derken acayip bir sey var.
	dizi2[2]=5;
	cout<<dizi2[2]<<endl;
	dizi2=0;

	int*x=new int();
	*x=5;
	cout<<"iii"<<*x<<endl;
	delete x;
	x=0;//burada bir nuans var eger ki bir pointeri silersen onu sifira gonderebilirsin.Dikkat!!pointerin icini degil kendisini yani adres.
		//Bunu yaptiktan sonra bu pointer ile ilgili islem yapmaya calisirsan compiler donuyor yani garabtiye aliyorsun kendini.ister yap ister yapma.

//---------------------------------------------------------------------------(end of 3) heap ve new anahtar kelimesi

	return 0;
}