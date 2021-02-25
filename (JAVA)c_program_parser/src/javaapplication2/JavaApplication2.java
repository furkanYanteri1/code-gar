/**
  *
  * @author Furkan Yanteri	furkan.yanteri@ogr.sakarya.edu.tr  
  * @since 01.03.2019  
  *   
  * Function Class'i haricinde her sey burada yapiliyor.Detayli aciklama kodun yorum satirlarinda ve rapordadir. 
  *   
  */ 
package javaapplication2;

//Bu alttaki importlar ilgili fonksiyonlarin kullanim on sartlari olup zaruriyet arzeder.
//import java.io.BufferedReader;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.List;
//import java.util.ArrayList;
//import java.io.FileWriter;

/**
 *
 * @author furkanyanteri
 */
public class JavaApplication2 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        File f=new File("abc.txt");  
        try{
 
            List<Function> list1 = new ArrayList<Function>();//Function klasi icinde fonksiyonlara ait bilgileri tutariz burada da temelini attik. 

//            Function a=new Function();

            //---------------------------------------------------------------------------------------
            String line;
            char[] Cline;//string olan linelarin her seferinde bu karakter dizisine koyarak calisacagiz
            int operatorCounter=0;//operator sayaci
            int functionCounter=0;//fonksiyon sayaci
            int parameterCounter=0;//toplam parametre sayisi
            int x;//fonksiyon ararken substring aramalarimizda var mi yok mu diye kullanacagiz
            
            int j;//fonkiyon isimlerini bulurken kullanacagim.Dongunun icindeki i yi bozmamak icin kullanacagim.
            String tempo;//fonksiyonun ismini gecici olarak icinde tutacagim.
            
            File f1=new File("abc.txt");//Buradaki f2 ve fr2 BufferedReader kullanimini anlatmak icin
            FileReader fr1=new FileReader(f1);//ayrica yapildi.BufferedReaderla line olarak okudum. 
//---------------------------------------------------------
            BufferedReader bfr= new BufferedReader(fr1);
            line=bfr.readLine();
            while(line!=null)
            {   
                //-------------------------------foksiyon sayma burada
                x=line.indexOf("){");
                if(x!=-1)
                    functionCounter++;
                
                //-------------------------------.
                Cline=line.toCharArray();
                for (int i = 0; i < Cline.length; i++) {
                    if(Cline[i]=='+'||Cline[i]=='-'||Cline[i]=='>'||Cline[i]=='<'||Cline[i]=='*'||Cline[i]=='/'||Cline[i]=='='||Cline[i]=='&')        
                        operatorCounter++;
                    if((Cline[i]=='+'||Cline[i]=='-')&&(Cline[i+1]=='+'||Cline[i+1]=='-'))        
                        operatorCounter=operatorCounter-1;//++ ve -- ler 1 sayilacakmis onun icin
                }
                line=bfr.readLine();//tekrar oku
            
            }
            //-----------------------------------------------------
            fr1.close();//Kapatmalari unutmuyoruz.
            //-------------------tekrar actik fonksiyon islemleri icin
            File f2=new File("abc.txt");//Buradaki f2 ve fr2 BufferedReader kullanimini anlatmak icin
            FileReader fr2=new FileReader(f2);//ayrica yapildi.BufferedReaderla line olarak okudum. 
            BufferedReader bfr2= new BufferedReader(fr2);

            line=bfr2.readLine();
            while(line!=null)
            {   
                Cline=line.toCharArray();
                for (int i = 0; i < Cline.length; i++) {
                    //------------------------------------------Fonksiyon ismi buradan
                    if(Cline[i]=='{'&&Cline[i-1]==')')
                    {
                        Function ftmp=new Function();//gecici olarak function classindan nene uretip listemize ekleyek
                        j=i;

                        while(Cline[j]!='(')
                            j--;
                        while(Cline[j]!=' ')
                        {
                            j--;
                        }
                        tempo=(line.substring(j, line.indexOf('(')));
                        ftmp.name=tempo;
                        list1.add(ftmp);
                        //System.out.println("////->"+tempo);
                        
                    }//------------------------------------------.
                }
                line=bfr2.readLine();//tekrar oku
            
            }
            
            //----------------------------------------<><>----------------------
             fr2.close();//Kapatmalari unutmuyoruz.
            //-------------------tekrar actik fonksiyon islemleri icin
            File f3=new File("abc.txt");//Buradaki f2 ve fr2 BufferedReader kullanimini anlatmak icin
            FileReader fr3=new FileReader(f3);//ayrica yapildi.BufferedReaderla line olarak okudum. 
            BufferedReader bfr3= new BufferedReader(fr3);

            String abece;//gecici bir string
            char[]zibidi;//gecici olarak stringi bu araya koy
            line=bfr3.readLine();
            while(line!=null)
            {  
                for (int i = 0; i < list1.size(); i++) {
                    if(line.indexOf(list1.get(i).name)!=-1 && (line.indexOf((int)'(')+1 != line.indexOf((int)')')))
                    {
                        if (line.substring(line.indexOf((int)'(')+1 , line.indexOf((int)')')).indexOf("int")!=-1 || line.substring(line.indexOf((int)'(')+1 , line.indexOf((int)')')).indexOf("double")!=-1 || line.substring(line.indexOf((int)'(')+1 , line.indexOf((int)')')).indexOf("char")!=-1 || line.substring(line.indexOf((int)'(')+1 , line.indexOf((int)')')).indexOf("bool")!=-1 || line.substring(line.indexOf((int)'(')+1 , line.indexOf((int)')')).indexOf("float")!=-1)
                        {
                            list1.get(i).parameters=(line.substring(line.indexOf((int)'(')+1 , line.indexOf((int)')')));
                        }
                    
                    }
                }

                line=bfr3.readLine();

            }
            for (int i = 0; i < list1.size(); i++) {
                if (list1.get(i).parameters==null) {
                    continue;
                }
                else
                    parameterCounter++;
                Cline=list1.get(i).parameters.toCharArray();
                
                for (int k = 0; k < Cline.length; k++) {
                    if(Cline[k]==',')
                        parameterCounter++;
                }
            }
            System.out.println("Toplam  operator sayisi: "+operatorCounter);
            System.out.println("Toplam fonksiyon sayisi: "+functionCounter);
            System.out.println("Toplam parametre sayisi: "+parameterCounter);
            System.out.println("Fonksiyon isimleri:");
            for (int i = 0; i < list1.size(); i++) {
              
                if (list1.get(i).parameters==null)//icinde parametre yazmayan fonksiyonlarda sikinti cikmamasi icin
                {
                   System.out.println(list1.get(i).name+"- Parametreler:");
                   continue;
                }

                
               list1.get(i).parameters =list1.get(i).parameters.replaceAll("int", "");
               list1.get(i).parameters =list1.get(i).parameters.replaceAll("char", "");
               list1.get(i).parameters =list1.get(i).parameters.replaceAll("double", "");
               list1.get(i).parameters =list1.get(i).parameters.replaceAll("float", "");
                 //   System.out.println("##################################");
                //}
                System.out.println(list1.get(i).name+"- Parametreler: "+list1.get(i).parameters);
            }
            fr3.close();
            

        }
        catch(Exception e){
           // e.printStackTrace();
        }
        //**********************************************************
        
}
}
