#include <iostream>
using namespace std;
class Dugum
{
public:
	int veri;
	Dugum *sonraki;
	Dugum()//         1. kurucu fonksiyon
	{
		sonraki=NULL;//------------------ONEMLI!!! bunu yaparak hata yapma riskini azalt.  (veya  sonraki=0)
	};
	Dugum(int veri)// 2. kurucu fonksiyon
	{
		this->veri=veri;
		sonraki=NULL;
	};
	~Dugum();
	
};
//------------------------------------------------------------dugum prototipi hazir

int main(int argc, char const *argv[])
{
	Dugum *kok=new Dugum();
	kok->veri=0;//----------------------------------------------kok dugum olusturuldu ve verisi 0 olarak verildi 
	Dugum *gezici;
	gezici=kok;//-------------------------------------------------gezici dugum olusturuldu ve kok dugumun gosterdigi yer gostertildi 
	for (int i = 1; i < 11; ++i)
	{
		gezici->sonraki=new Dugum(10*i);
		gezici=gezici->sonraki;
	}
	//-------------------------------------------------------------kok dugume gezici kullanarak 10 tane eleman eklendi ve icine sayilar konuldu
	gezici=kok;
	//--------------------------------------------------------------geziciye tekrar kok gosterildi
	for (int i = 1; i < 11; ++i)
	{
		cout<<gezici->veri<<" | ";
		gezici=gezici->sonraki;
	}
	//----------------------------------------------------------------gezici kullanarak bagli listenin elemanlari gezildi ve verilerine bakildi
}
/*
                               #^&$^&$*&$%*&$&*$&*^&*$$&@%
                              $$$$$$$$$$$$$$$$$$$$$$)))))))
                             ?????????????????????????????))
                            /``````````````````|||||////????
                           /                 /||||||///?????
                          /                 /|||||||////????
                         /                 /||||||||////????
                        /  ________       /|||||||||////???
                       /  *********\      \||||||||\///???
                       \     --            \||||/  \|/???
                       /   |-----           |||\    )//??
                      /                     |||/   /  \?
                     /                      |||\__/    |
                    / _                     |/\        | 
                   /____)                   |/|        |  
                   	  |   \                 |//        |   
                   	  \\\\\\\          __////          |    
					   \\\\\\\     ___//////           |     
                   	    /   \\\   ///////              |      
                   	    ||   \\__///////               |       
                   	   /~~\___ /~/// |                 |        
                   	   |~~~~~~~~//   /                 |                      
                        ~~~~~~//    /                                   
                                                      
*/