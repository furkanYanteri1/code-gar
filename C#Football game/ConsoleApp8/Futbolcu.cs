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
using System.IO;
using System.Threading.Tasks;
using System.Threading;

namespace ConsoleApp8
{
    class Futbolcu
    {
        string AdSoyad;
        int FormaNo;
        int Hiz;
        int Dayaniklik;
        int Pas;
        int Sut;
        int Yetenek;
        int Kararlilik;
        int DogalForm;
        int Sans;
        
        public string adSoyad { get { return AdSoyad; } set { AdSoyad = value; } }
        public int formaNo { get { return FormaNo; } set { FormaNo = value; } }
        public int hiz { get { return Hiz; } set { Hiz = value; } }
        public int dayaniklilik { get { return Dayaniklik; } set { Dayaniklik = value; } }
        public int pas { get { return Pas; } set { Pas = value; } }
        public int sut { get { return Sut; } set { Sut = value; } }
        public int yetenek { get { return Yetenek; } set { Yetenek = value; } }
        public int kararlilik { get { return Kararlilik; } set { Kararlilik = value; } }
        public int dogalForm { get { return DogalForm; } set { DogalForm = value; } }
        public int sans { get { return Sans; } set { Sans = value; } }
        public double GolSkor;
        public double PasSkor;
        public Boolean PasVer()
        {
            if (PasSkor > 60)
                return true;
            else
                return false;
        }
        public Boolean GolVurusu()
        {
            if (GolSkor > 70)
                return true;
            else
                return false;
        }

        Random random = new Random();
        public Futbolcu(string isim,int numara)
        {
            adSoyad = Path.GetRandomFileName();
            adSoyad = adSoyad.Replace(".", string.Empty);/*rastgele adsoyad ata icinde rakam olmasin*/            adSoyad = adSoyad.Replace("0", string.Empty); adSoyad = adSoyad.Replace("1", string.Empty); adSoyad = adSoyad.Replace("2", string.Empty); adSoyad = adSoyad.Replace("3", string.Empty); adSoyad = adSoyad.Replace("4", string.Empty); adSoyad = adSoyad.Replace("5", string.Empty); adSoyad = adSoyad.Replace("6", string.Empty); adSoyad = adSoyad.Replace("7", string.Empty); adSoyad = adSoyad.Replace("8", string.Empty); adSoyad = adSoyad.Replace("9", string.Empty);//burada yaptigim islem butun rakamlari yok etmek ismin icinde rakam olmasin diye
            formaNo = random.Next(50, 100);
            hiz = random.Next(50, 100);
            dayaniklilik = random.Next(50, 100);
            pas = random.Next(50, 100);
            sut = random.Next(50, 100);
            yetenek = random.Next(50, 100);
            kararlilik = random.Next(50, 100);
            dogalForm = random.Next(50, 100);
            sans = random.Next(50, 100);
            GolSkor = yetenek * 0.3 + sut * 0.2 + kararlilik * 0.1 + dogalForm * 0.1 +hiz * 0.1 + sans * 0.2;


        }
        public Futbolcu()//program.cs te isim v numara verilmezse burada rastgele isim ve numara uretilir
        {
            adSoyad = Path.GetRandomFileName();
            adSoyad = adSoyad.Replace(".", string.Empty);/*rastgele adsoyad ata icinde rakam olmasin*/            adSoyad = adSoyad.Replace("0", string.Empty);adSoyad = adSoyad.Replace("1", string.Empty);adSoyad = adSoyad.Replace("2", string.Empty);adSoyad = adSoyad.Replace("3", string.Empty);adSoyad = adSoyad.Replace("4", string.Empty);adSoyad = adSoyad.Replace("5", string.Empty);adSoyad = adSoyad.Replace("6", string.Empty);adSoyad = adSoyad.Replace("7", string.Empty);adSoyad = adSoyad.Replace("8", string.Empty);adSoyad = adSoyad.Replace("9", string.Empty);//burada yaptigim islem butun rakamlari yok etmek ismin icinde rakam olmasin diye
            formaNo = random.Next(50,100);
            Thread.Sleep(random.Next(10,30));
//            Console.WriteLine("<------------------------------------------>");
            hiz = random.Next(50, 100);
            Thread.Sleep(random.Next(10, 30));
            dayaniklilik = random.Next(50, 100);
            Thread.Sleep(random.Next(10, 30));
            pas = random.Next(50, 100);
            Thread.Sleep(random.Next(10, 30));
            sut = random.Next(50, 100);
            Thread.Sleep(random.Next(10, 30));
            yetenek = random.Next(50, 100);
            Thread.Sleep(random.Next(10, 30));
            kararlilik = random.Next(50, 100);
            Thread.Sleep(random.Next(10, 30));
            dogalForm = random.Next(50, 100);
            Thread.Sleep(random.Next(10, 30));
            sans = random.Next(50, 100);
           GolSkor = yetenek * 0.3 + sut * 0.2 + kararlilik * 0.1 + dogalForm * 0.1 + hiz * 0.1 + sans * 0.2;
        }
    
    }
}
