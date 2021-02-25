/****************************************************************************
**					SAKARYA ÜNİVERSİTESİ
**				BİLGİSAYAR VE BİLİŞİM BİLİMLERİ FAKÜLTESİ
**				    BİLGİSAYAR MÜHENDİSLİĞİ BÖLÜMÜ
**				   NESNEYE DAYALI PROGRAMLAMA DERSİ
**					2018-2019 BAHAR DÖNEMİ
**	
**				ÖDEV NUMARASI..........:1
**				ÖĞRENCİ ADI............:Furkan Yanteri
**				ÖĞRENCİ NUMARASI.......:b181210380
**                         DERSİN ALINDIĞI GRUP...:1-C
****************************************************************************/

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;

namespace WindowsFormsApp2
{
    
    public partial class Form1 : Form
    {
        
        public Form1()
        {
            InitializeComponent();
        }
        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {

        }
        private void  label1_Click(object sender, EventArgs e){}//labellar burada anlatmaya gerek yok
        private void  label2_Click(object sender, EventArgs e){}
        private void  label3_Click(object sender, EventArgs e){}
        private void  label4_Click(object sender, EventArgs e){}
        private void  label5_Click(object sender, EventArgs e){}
        private void  label6_Click(object sender, EventArgs e){}
        private void  label7_Click(object sender, EventArgs e){}
        private void  label8_Click(object sender, EventArgs e){}
        private void  label9_Click(object sender, EventArgs e){}
        private void label10_Click(object sender, EventArgs e){}
        private void label11_Click(object sender, EventArgs e){}
        private void label12_Click(object sender, EventArgs e){}
        private void label13_Click(object sender, EventArgs e){}
        private void label14_Click(object sender, EventArgs e){}
        private void label15_Click(object sender, EventArgs e){}
        private void label16_Click(object sender, EventArgs e){}
        private void label17_Click(object sender, EventArgs e){}
        private void label18_Click(object sender, EventArgs e){}
        private void label19_Click(object sender, EventArgs e){}
        private void label20_Click(object sender, EventArgs e){}
        private void label21_Click(object sender, EventArgs e){}
        private void label22_Click(object sender, EventArgs e){}
        private void label23_Click(object sender, EventArgs e){}
        private void label24_Click(object sender, EventArgs e){}
        private void label25_Click(object sender, EventArgs e){}
        private void label26_Click(object sender, EventArgs e){}
        private void label27_Click(object sender, EventArgs e){}
        private void label28_Click(object sender, EventArgs e){}
        private void label29_Click(object sender, EventArgs e){}
        private void label30_Click(object sender, EventArgs e){}
        private void label31_Click(object sender, EventArgs e){}

        private void button1_Click(object sender, EventArgs e)
        {
            TextReader reader = new StreamReader(textBox1.Text);
            //TextReader reader = new StreamReader("personeller.txt");
            //string[][] tumSatirlar;
            string[] satirlar;
            string[] kelimeler=null;
            
            string hepsi = reader.ReadToEnd();
            satirlar = hepsi.Split('\n');
            //int cntr=0;
           /*                 foreach (string s in satirlar) // personel bilgileri(satırlar) ayrıştırılabilir.
                            {
                                 kelimeler = s.Split(' ');
                 
                            }*/
            // label1.Text = kelimeler[0];
            int malumSahis;//malum sahsin tcsiyle indexine yonelirken tutacagimiz integer

            for (int i = 0; i <satirlar.Length; i++)
            {
                if (satirlar[i].Contains(richTextBox1.Text))
                {
                    
                    malumSahis = i;
                   
                        kelimeler = satirlar[i].Split(' ');
                        label16.Text = kelimeler[1];//ad
                        label17.Text = kelimeler[2];//soyad
                        label18.Text = kelimeler[3];//yas
                        label19.Text = kelimeler[4];//calisma suresi
                        label20.Text = kelimeler[5];//evlilik durumu
                        label21.Text = kelimeler[6];//esi calisiyormu
                        label22.Text = kelimeler[7];//cocuk sayisi
                        label29.Text = kelimeler[8];//taban maas
                        label28.Text = kelimeler[9];//makam tazminati
                        label27.Text = kelimeler[10];//idari gorev tazminati
                        label26.Text = kelimeler[11];//fazla mesai saati
                        label25.Text = kelimeler[12];//fazla mesai saati ucreti
                        label24.Text = kelimeler[13];//vergi matrahi
                        label23.Text = kelimeler[14];//personel resmi yolu


                }
                else
                    continue;

            }
           
            int burut = 0;
            int damga_vergisi = 0;
            int gelir_vergisi = 0;
            int emekli_kesintisi = 0;
            int net_maas = 0;


            if (kelimeler[5]=="H")
            {
                //burut=taban+makam+idari+(cocuk*30)+(fazla m.saati*f.m ucreti)
                burut =Int32.Parse(kelimeler[8])+ Int32.Parse(kelimeler[9]) + Int32.Parse(kelimeler[10]) + Int32.Parse(kelimeler[7])*30 + Int32.Parse(kelimeler[11])* Int32.Parse(kelimeler[12]);

            }
            if (kelimeler[5] == "E")//evliyse
            {
                if (kelimeler[6] == "E")//esi calisiyorsa
                    burut = Int32.Parse(kelimeler[8]) + Int32.Parse(kelimeler[9]) + Int32.Parse(kelimeler[10]) + Int32.Parse(kelimeler[7]) * 30 + Int32.Parse(kelimeler[11]) * Int32.Parse(kelimeler[12]);
                else//esi calismiyorsa
                    burut = 200+Int32.Parse(kelimeler[8]) + Int32.Parse(kelimeler[9]) + Int32.Parse(kelimeler[10]) + Int32.Parse(kelimeler[7]) * 30 + Int32.Parse(kelimeler[11]) * Int32.Parse(kelimeler[12]);
            }
            damga_vergisi = burut / 10;//damga vergi
            emekli_kesintisi = burut * 15 / 100;//emekli kesintisi
            //---------------------------------------------------gelir vergisi
            if (Int32.Parse(kelimeler[13]) < 10000)
                gelir_vergisi = burut * 15 / 100;
            if (Int32.Parse(kelimeler[13]) >= 10000 && Int32.Parse(kelimeler[13]) < 20000)
                gelir_vergisi = burut * 20 / 100;
            if (Int32.Parse(kelimeler[13]) >= 20000 && Int32.Parse(kelimeler[13]) < 30000)
                gelir_vergisi = burut * 25 / 100;
            if (Int32.Parse(kelimeler[13]) >= 30000)
                gelir_vergisi = burut * 30 / 100;
            //---------------------------------------------------eo gelir vergisi
            
            net_maas = burut - (emekli_kesintisi + gelir_vergisi + damga_vergisi);
            label31.Text = net_maas.ToString();//net maas


            reader.Close();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            openFileDialog1.ShowDialog();
            textBox1.Text = openFileDialog1.FileName;
            //label1
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
    