package paket;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.List;
import java.util.Scanner;

import org.neuroph.core.NeuralNetwork;
import org.neuroph.core.data.DataSet;
import org.neuroph.core.data.DataSetRow;
import org.neuroph.nnet.MultiLayerPerceptron;
import org.neuroph.nnet.learning.MomentumBackpropagation;
import org.neuroph.util.TransferFunctionType;

public class YSA {//momentumlu bp
	private static final File egitimDosya = new File(YSA.class.getResource("Egitim.txt").getPath());
	private static final File testDosya = new File(YSA.class.getResource("Test.txt").getPath());
private double [] maksimumlar;
private double [] minimumlar;
private DataSet egitimVeriSeti;
private DataSet testVeriSeti;
private int araKatmanNoronSayisi;
MomentumBackpropagation mbp;

	public YSA(int araKatmanNoronSayisi,double momentum,double ogrenmeKatsayisi,double hata,int epoch) throws FileNotFoundException 
	{

		maksimumlar = new double[3];//
		minimumlar = new double[3];//
		
		for(int i=0;i<3;i++)
		{
			maksimumlar[i] = Double.MIN_VALUE;
			minimumlar[i] = Double.MAX_VALUE;
		}
		VerisetiMinMax(egitimDosya);
		VerisetiMinMax(testDosya);
		egitimVeriSeti=	 VeriSetiOku(egitimDosya);
		testVeriSeti = VeriSetiOku(testDosya);
		
		mbp=new MomentumBackpropagation();
		mbp.setMomentum(momentum);
		mbp.setLearningRate(ogrenmeKatsayisi);
		mbp.setMaxError(hata);
		mbp.setMaxIterations(epoch);
		this.araKatmanNoronSayisi = araKatmanNoronSayisi;
	}
	
	public double egitimHata() 
	{
		return mbp.getTotalNetworkError();
	}
	
	public double mse(double []beklenen,double []cikti) 
	{
		double birSatirdakiHata=0;
		for(int i =0;i<3;i++) 
		{
			birSatirdakiHata+=Math.pow(beklenen[i]-cikti[i], 2);
		}
		return birSatirdakiHata/3;
	} 
	public double testHata() 
	{
		NeuralNetwork sinirselAg = NeuralNetwork.createFromFile("ogrenenAg.nnet");
		double toplamHata=0;
		List<DataSetRow> satirlar = testVeriSeti.getRows();
		for(DataSetRow dr:satirlar) 
		{
			sinirselAg.setInput(dr.getInput());
			sinirselAg.calculate();
			toplamHata += mse(dr.getDesiredOutput(),sinirselAg.getOutput());
		}
		return toplamHata/testVeriSeti.size();
	}
	
	public void egit() //momentumlu bp olaylari
	{
		//alt satirdaki 8 degismelidir
		MultiLayerPerceptron sinirselAg = new MultiLayerPerceptron(TransferFunctionType.SIGMOID,3,araKatmanNoronSayisi,3);
		sinirselAg.setLearningRule(mbp);
		sinirselAg.learn(egitimVeriSeti);
		sinirselAg.save("ogrenenAg.nnet");
		System.out.println("Egitim Tamamlandi");
	}
	private double minMax(double max, double min, double x) 
	{
		return (x-min)/(max-min);
		
	}
	private DataSet VeriSetiOku(File file) throws FileNotFoundException 
	{
		Scanner scan = new Scanner(file);
		DataSet dataset = new DataSet(3,3);//BIZIM 4 3 OLACAK GALIBA
		while(scan.hasNextDouble()) 
		{
			double []inputs = new double[3];//bizde 4 olacak galbe
			for(int i=0; i<3; i++)//bizde 4
			{
				double d = scan.nextDouble();
				inputs[i]=minMax(maksimumlar[i], minimumlar[i], d);
			}
			dataset.add(new DataSetRow(inputs,new double[]{scan.nextDouble(),scan.nextDouble(),scan.nextDouble()}));
		}
		scan.close();
		return dataset;
	}

	private void VerisetiMinMax(File file) throws FileNotFoundException 
	{
		Scanner scan = new Scanner(file);
		while(scan.hasNextDouble()) 
		{
			for (int i = 0; i < 3; i++) 
			{
				double d = scan.nextDouble();
				
				if(d>maksimumlar[i]) maksimumlar[i]=d;
				if(d<minimumlar[i]) minimumlar[i]=d;
			}
			scan.nextDouble();scan.nextDouble();scan.nextDouble();//3 kere bosa okuyorum outputlari gecmek icin
			
		}
		scan.close();
		
		
	
	}

}






