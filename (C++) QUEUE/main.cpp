#include<iostream>
#include"kuyruk.hpp"
using namespace std;
int main(){
    Kuyruk* k1=new Kuyruk();
    for (int i = 0; i < 10; i++)
    {
        k1->elemanEkle(i);
        /* code */
    }
    k1->yazdir();
    cout<<""<<endl;
    cout<<""<<endl;
    
    int temp;

    for (int i = 0; i < 9; i++)
    {
        k1->getir(temp);
        cout<<temp<<"-";
    }
    cout<<""<<endl;
    k1->yazdir();
    
    





}