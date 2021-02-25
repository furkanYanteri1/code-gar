package paket;

import java.net.URISyntaxException;
import java.util.Scanner;

import net.sourceforge.jFuzzyLogic.plot.JFuzzyChart;

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
			JFuzzyChart.get().chart(incelenecek_hava.getmodel());
			System.out.println(incelenecek_hava);
		} catch (URISyntaxException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
		
	}

}
