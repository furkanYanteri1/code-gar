package paket;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.Random;
public class Program {

	public static void main(String[] args) throws IOException {
		
		// TODO Auto-generated method stub
		System.out.println("Egitim basladi, lutfen bekleyiniz...");
		Scanner in = new Scanner(System.in);
		
		int araKatmanNoronSayisi;
		double momentum,ogrenmeKatsayisi,hata;
		int epoch,sec=0;
		YSA ysa = null;//momentumlu bp
		YSA2 ysa2= null;//momentumsuz bp
		
			
					araKatmanNoronSayisi = 20;
					momentum = 0.9;
					ogrenmeKatsayisi = 0.1;
					hata = 0.001;
					epoch = 2000;

					ysa = new YSA(araKatmanNoronSayisi,momentum,ogrenmeKatsayisi,hata,epoch); 
					ysa.egit();
					
					System.out.println("\nMOMENTUMLU BP ICIN ->");
					System.out.println("Egitim hatasi: "+ysa.egitimHata());
					System.out.println("Testte hatasi: "+ysa.testHata());
					System.out.println("lutfen bekleyiniz...: ");
					
					ysa2 = new YSA2(araKatmanNoronSayisi,ogrenmeKatsayisi,hata,epoch); 
					ysa2.egit();
					System.out.println("\nMOMENTUMSUZ BP ICIN:----(adim adim egitim hata grafigi rapordadir.)");
					System.out.println("Egitimden elde edilen hata: "+ysa2.egitimHata());
					System.out.println("Testte elde edilen hata: "+ysa2.testHata());
					
					do {
					System.out.println("\n1)Egitim hata listesini gormek icin\n2)Cikmak icin\n seciminiz=>");
					
					sec = in.nextInt();
					if(sec==1)
					{
						double[] hatalar = ysa2.hatalar_listesi();
						epoch = 0;
						for(double h : hatalar) 
						{
							System.out.println(epoch+" : "+h);
							epoch++;
						}
					}
					else if(sec==2)
						break;
					}while (sec!=1 || sec!=2);
		
	}

}

