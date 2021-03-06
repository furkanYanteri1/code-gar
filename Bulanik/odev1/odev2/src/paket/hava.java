package paket;

import java.io.File;
import java.net.URISyntaxException;

import net.sourceforge.jFuzzyLogic.FIS;

public class hava {
	private FIS fis;
	private double dogal_gaz_kullanim_orani;
	private int nufus;
	private int mevsim;

	public hava(double dogal_gaz_kullanim_orani, int nufus, int mevsim) throws URISyntaxException 
	{
		this.dogal_gaz_kullanim_orani = dogal_gaz_kullanim_orani;
		this.mevsim = mevsim;
		this.nufus = nufus;
		
		File dosya = new File(getClass().getResource("model.fcl").toURI());
		fis = FIS.load(dosya.getPath(),true);
		fis.setVariable("dogal_gaz_kullanim_orani", dogal_gaz_kullanim_orani);
		fis.setVariable("mevsim", mevsim);
		fis.setVariable("nufus", nufus);
		fis.evaluate();		
	}
	public hava() throws URISyntaxException
	{
		File dosya = new File(getClass().getResource("model.fcl").toURI());
		fis = FIS.load(dosya.getPath(),true);
	}
	public FIS getmodel(){
		return fis;
	}
	@Override
	public String toString() {
		String cikti = "Nufus: "+nufus+"\nDogal Gaz Kullanim Orani: "+dogal_gaz_kullanim_orani+"\nMevsim: "+mevsim+"\nHava Kirlilik Orani: "+fis.getVariable("hava_kirlilik_orani").getValue();
		return cikti;
	}
}
