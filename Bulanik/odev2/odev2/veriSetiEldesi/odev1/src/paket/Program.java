package paket;

import java.net.URISyntaxException;
import java.util.Scanner;
import java.util.Random;
import java.lang.Math;

import net.sourceforge.jFuzzyLogic.plot.JFuzzyChart;
import net.sourceforge.jFuzzyLogic.rule.Rule;

public class Program {

	public static void main(String[] args) {
		Scanner girdi = new Scanner(System.in);
		int nufus;
		double dogal_gaz_kullanim_orani;
		int mevsim;
		
		int random_int;//nufus ve mevsim rastgele atamalari icin
		double random_double;//dogalgaz kullanim orani rastgele atamalari icin
		
		for (int i = 0; i < 1000; i++)//1000 satirlik veri seti oldugundan dolayi
		{
			
			//nufus icin rastgele atama
			random_int= (int)(Math.random() * (23000))+1;
			if(random_int>23000 || random_int<1)
				continue;
			else 
			{
				nufus = random_int;//nufus atandi
				System.out.print("\n"+nufus+" ");
			}
			
			//mevsim icin rastgele atama 
			random_int= (int)(Math.random() * (4)) + 1;
			if(random_int>4 || random_int<1)
				continue;
			else
			{//mevsim bilgisi siniflandirma verisi oldugundan ve kis ilkbahar yaz ve sonbahar oldugundan
				//4 frkli oldugundan 2 inputa donusturdum
				if(random_int == 1)
					System.out.print("0 0 ");//kis
				if(random_int == 2)
					System.out.print("0 1 ");//ilkbahar
				if(random_int == 3)
					System.out.print("1 0 ");//yaz
				if(random_int == 4)
					System.out.print("1 1 ");//sonbahar
				mevsim=random_int;//mevsim atandi
			}
			
			//dogal gaz kullanim orani icin rastgele atama
			random_double = Math.random() * (100);
			if(random_double>100 || random_double<0)
				continue;
			else 
			{
				dogal_gaz_kullanim_orani = random_double;//dogalgaz kullanim orani atandi
				System.out.print(dogal_gaz_kullanim_orani+" ");
			}
			try {
				hava incelenecek_hava=new hava(dogal_gaz_kullanim_orani,nufus,mevsim);
				String donusturulmemis_sonuc = incelenecek_hava.sonuc();//iyi kotu ve ortayi donusturmeden onceki hali
				if(donusturulmemis_sonuc == "iyi")
					System.out.print("1 0 0");//iyi icin donusum
				else if(donusturulmemis_sonuc == "kotu")
					System.out.print("0 0 1");//kotu icin donusum
				else// orta icin
					System.out.print("0 1 0");//orta icin donusum
					
				
			} catch (URISyntaxException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}

			
		
		}
			

}
}

/*BU DOSYANIN ONCEKI HALI FULL
 * package paket;

import java.net.URISyntaxException;
import java.util.Scanner;
import java.util.Random;
import java.lang.Math;

import net.sourceforge.jFuzzyLogic.plot.JFuzzyChart;
import net.sourceforge.jFuzzyLogic.rule.Rule;

public class Program {

	public static void main(String[] args) {
		Scanner girdi = new Scanner(System.in);
		System.out.print("Nufus: ");
		int nufus = girdi.nextInt();//cok absurt yuksek degerler icin en kalabalik sinifini secer detayli bilgi model.flcnin ilgili bolumerinde bulunuyor
		double dogal_gaz_kullanim_orani;
		do 
		{
			System.out.print("Dogal Gaz Kullanim Orani (%): ");
			dogal_gaz_kullanim_orani = girdi.nextDouble();			
		}while(dogal_gaz_kullanim_orani>100 || dogal_gaz_kullanim_orani<0);
		int mevsim;
		do 
		{
			System.out.print("Mevsim (1=Kis, 2=Ilkbahar, 3=Yaz, 4=Sonbahar): ");
			mevsim= girdi.nextInt();
		}while(mevsim<0 || mevsim>4);
		
		try {
			hava incelenecek_hava=new hava(dogal_gaz_kullanim_orani,nufus,mevsim);
//			hava incelenecek_hava=new hava();
			System.out.println(incelenecek_hava);
//			JFuzzyChart.get().chart(incelenecek_hava.getmodel());
			//System.out.println(incelenecek_hava);
			var rules= incelenecek_hava.getmodel().getFunctionBlock("model").getFuzzyRuleBlock("kuralblok1").getRules();
			for(Rule r : rules ) 
			{
				
				if(r.getDegreeOfSupport()>0) System.out.println(r);//support degeri buyukse yazdiracak sadece.Istersen if kontrolunu silip hepsini gorebilirsin				
			}
			
		} catch (URISyntaxException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
//		double random_double;
//		for (int i = 0; i < 20; i++) 
//		{
//			random_double = Math.random() * (100 - 0 + 1) + 0;
//			System.out.println("\n--->"+random_double+"<----");
//			
//		}
		
	}

}
 */