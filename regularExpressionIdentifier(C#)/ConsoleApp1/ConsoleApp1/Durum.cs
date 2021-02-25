/*
 * B181210380
 * Furkan Yanteri
 * Bicinsel Diller Ve Soyut Makineler Odev1
 */
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Durum
    {
        public int durum_no;//hangi durum
        public char hamle;//hangi harle gidiyoruz
        public bool kabul;//kabul durumu mu yoksa deil mi
        public Durum()
        {
            durum_no = 0;//  baslangic durumu 0.durum ayni zamanda kabul durumu.
            hamle = 'x';//     x daha belirtilmemis anlaminda
            kabul=true;
        }
        public void calistir()
        {
            //-------------------------------------------------------------------------------------------------------
            if (durum_no == 0)
            {
                if(hamle=='a')
                {
                    durum_no=1;
                    kabul=false;
                }
                else
                {
                    durum_no=2;
                    kabul=false;
                }
            }
            else if (durum_no == 1)
            {
                if(hamle=='a')
                {
                    durum_no=3;
                    kabul=true;
                }
                else
                {
                    durum_no=4;
                    kabul=true;
                }
            }
            else if (durum_no == 2)
            {
                if(hamle=='a')
                {
                    durum_no=5;
                    kabul=false;
                }
                else
                {
                    durum_no=6;
                    kabul=true;
                }
            }
            else if (durum_no == 3)
            {
                if(hamle=='a')
                {
                    durum_no=1;
                    kabul=false;
                }
                else
                {
                    durum_no=7;
                    kabul=true;
                }
            }
            else if (durum_no == 4)
            {
                if(hamle=='a')
                {
                    durum_no=1;
                    kabul=false;
                }
                else
                {
                    durum_no=2;
                    kabul=false;
                }
            }
            else if (durum_no == 5)
            {
                if(hamle=='a')
                {
                    durum_no=5;
                    kabul=false;
                }
                else
                {
                    durum_no=4;
                    kabul=true;
                }
            }
            else if (durum_no == 6)
            {
                if(hamle=='a')
                {
                    durum_no=1;
                    kabul=false;
                }
                else
                {
                    durum_no=2;
                    kabul=false;
                }
            }
            else if (durum_no == 7)
            {
                if(hamle=='a')
                {
                    durum_no=1;
                    kabul=false;
                }
                else
                {
                    durum_no=8;
                    kabul=true;
                }
            }
            else if (durum_no == 8)
            {
                if(hamle=='a')
                {
                    durum_no=1;
                    kabul=false;
                }
                else
                {
                    durum_no=8;
                    kabul=true;
                }
            }
            //-------------------------------------------------------------------------------------------------------
        }/*
        public bool kontrolEt(char[]katar)
        {
            for (int i = 0; i < length; i++)
			{

			}
        }*/
    }
}
