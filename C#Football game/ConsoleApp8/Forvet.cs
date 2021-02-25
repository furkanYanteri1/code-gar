/****************************************************************************
**					SAKARYA ÜNİVERSİTESİ
**				BİLGİSAYAR VE BİLİŞİM BİLİMLERİ FAKÜLTESİ
**				    BİLGİSAYAR MÜHENDİSLİĞİ BÖLÜMÜ
**				   NESNEYE DAYALI PROGRAMLAMA DERSİ
**					2018-2019 BAHAR DÖNEMİ
**	
**				ÖDEV NUMARASI..........:2
**				ÖĞRENCİ ADI............:Furkan Yanteri
**				ÖĞRENCİ NUMARASI.......:B181210380
**                         DERSİN ALINDIĞI GRUP...:1-C
****************************************************************************/
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp8
{
    class Forvet : Futbolcu
    {
        int Bitiricilik;
        int IlkDokunus;
        int Kafa;
        int OzelYetenek;
        int SogukKanlilik;
        public int bitiricilik { get { return Bitiricilik; } set { Bitiricilik = value; } }
        public int ilkDokunus { get { return IlkDokunus; } set { IlkDokunus = value; } }
        public int kafa { get { return Kafa; } set { Kafa = value; } }
        public int ozelYetenek { get { return OzelYetenek; } set { OzelYetenek = value; } }
        public int sogukKanlilik { get { return SogukKanlilik; } set { SogukKanlilik = value; } }
        Random random4 = new Random();
        public Forvet(string isim,int numara)
        {
            base.adSoyad = isim;
            base.formaNo = numara;
            bitiricilik = random4.Next(70, 100);
            ilkDokunus = random4.Next(70, 100);
            kafa = random4.Next(70, 100);
            ozelYetenek = random4.Next(70, 100);
            sogukKanlilik = random4.Next(70, 100);
            PasSkor = pas * 0.3 + (yetenek + ozelYetenek) * 0.2 + (dayaniklilik + dogalForm + sans) * 0.1;
            GolSkor = GolSkor - (yetenek + sut + hiz + sans) * 0.1 + (kafa + ilkDokunus + bitiricilik + sogukKanlilik) * 0.1 + ozelYetenek * 0.2;
        }
        public Forvet()
        {
            bitiricilik = random4.Next(70, 100);
            ilkDokunus = random4.Next(70, 100);
            kafa = random4.Next(70, 100);
            ozelYetenek = random4.Next(70, 100);
            sogukKanlilik = random4.Next(70, 100);
            PasSkor = pas * 0.3 + (yetenek + ozelYetenek) * 0.2 + (dayaniklilik + dogalForm + sans) * 0.1;
            GolSkor = GolSkor - (yetenek + sut + hiz + sans) * 0.1 + (kafa + ilkDokunus + bitiricilik + sogukKanlilik) * 0.1 + ozelYetenek * 0.2;
        }
    }
}
