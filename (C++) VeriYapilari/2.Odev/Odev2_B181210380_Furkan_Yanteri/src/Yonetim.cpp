/**************************************************************************** 
**     SAKARYA UNIVERSITY 
**        BILGISAYAR MUHENDISLIGI BOLUMU 
**          VERI YAPILARI  
**     
**    OGRENCI ISMI.....: Furkan Yanteri
**    OGRENCI NUMARASI.: B181210380
****************************************************************************/
#include "Yonetim.hpp"
void Yonetim::dosyadanOku()
{
    ifstream fin("./doc/Yiginlar.Txt");
    char ch;                                //the character I read at once
    int i, nl = 0;                          //nl for new line counting
    int longest_line = 0, current_line = 0; //longest line's number of character going to be used to size of , current line for compare
    //------------------------------------------------------reading the .txt file
    while (fin)
    {
        fin.get(ch);
        i = ch;
        if ((i > 63 && i < 91) || (i > 96 && i < 123)) //is the characcter we have read really a character?(a-A to z-Z)
        {
            current_line++;
        }
        else if (ch == '\n')
        {
            if (current_line > longest_line)
                longest_line = current_line;
            current_line = 0;
            nl++; //the line counting line count in .txt file
        }
    }
    if (current_line > longest_line)
        longest_line = current_line;
    nl++; //(final nl+1 = exact number of lines)
    //------------------------------------------------------reading the .txt file
    yiginDizisi1 = new YiginDizisi(nl);
    fin.close();
    fin.open("./doc/Yiginlar.Txt");
    //*************************************************************************************************************************************
    int whichStackToAdd = 0; //its going to be increment below
    while (fin)
    {
        fin.get(ch);
        i = ch;
        if ((i > 63 && i < 91) || (i > 96 && i < 123)) //is the characcter we have read really a character?(a-A to z-Z)
        {
            yiginDizisi1->elemanekle(whichStackToAdd, ch);
        }
        else if (ch == '\n')
        {
            whichStackToAdd++;//if the char is \n go the line below and read for next stack
        }
    }
    yiginDizisi1->yiginlar[yiginDizisi1->yiginlar->elemanSayisi+1].cikar();//not esthetic but avoids to last letter is added twice
}
Yonetim::Yonetim()
{
    yiginDizisi1 = 0;
}
void Yonetim::oynatBakalim()
{
    int counter=0;//harfleri mesaja duzgunce eklemek icin
    int secim;
    int mesaj_boyut=yiginDizisi1->eleman_sayisi*10;
    
    char* mesaj=new char[mesaj_boyut];
    for (int i = 0; i < mesaj_boyut; i++)
        mesaj[i]=' ';    
    while(secim!=-1)
    {
        system("cls"); //clean the screen and do it again
        cout<<"\n\n";
        cout<<"....Yazi:";
        for (int i = 0; mesaj[i]!=' ' ; i++)
            cout<<mesaj[i];
        cout<<"\n\n\n\n";
                        
        yiginDizisi1->Goster();
        cout << "\n\n\n\nYigin numarasi:";
        cin >> secim;

        if (secim==-1)//-1 sentinel exit
            return;

        mesaj[counter]=yiginDizisi1->yiginlar[secim-1].enUstGetir();//mesaja ekledim
        counter++;
        yiginDizisi1->yiginlar[secim-1].cikar();
    }
    delete yiginDizisi1->yiginlar;
    delete yiginDizisi1;
    cout<<"bye"<<endl;
}