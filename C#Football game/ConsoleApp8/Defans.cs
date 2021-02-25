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
    class Defans:Futbolcu
    {
        int PozisyonAlma;
        int Kafa;
        int Sicrama;
        public int pozisyonAlma { get { return PozisyonAlma; } set { PozisyonAlma = value; } }
        public int kafa { get { return Kafa; } set { Kafa = value; } }
        public int sicrama { get { return Sicrama; } set { Sicrama = value; } }
        Random random2 = new Random();
        public Defans(string isim,int numara)
        {
            base.adSoyad = isim;
            base.formaNo = numara;
            pozisyonAlma = random2.Next(50, 90);
            kafa = random2.Next(50, 90);
            sicrama = random2.Next(50, 90);
            GolSkor = GolSkor - (hiz * 0.1 + sans * 0.1) + kafa * 0.1 + sicrama * 0.1;
            PasSkor = pas * 0.3 + yetenek * 0.3 + (dayaniklilik + dogalForm + pozisyonAlma) * 0.1 + sans * 0.2;
        }
        public Defans()//isim ve numara verilmezse rastgele uretelim
        {
            pozisyonAlma = random2.Next(50, 90);
            kafa = random2.Next(50, 90);
            sicrama = random2.Next(50, 90);
            GolSkor = GolSkor - (hiz*0.1+sans*0.1)+kafa*0.1+sicrama*0.1;
            PasSkor = pas * 0.3 + yetenek * 0.3 + (dayaniklilik + dogalForm + pozisyonAlma) * 0.1 + sans * 0.2;
        }

    }
}
