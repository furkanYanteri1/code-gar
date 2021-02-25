/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
  *
  * @author Furkan Yanteri	furkan.yanteri@ogr.sakarya.edu.tr  
  * @since 20.03.2019  
  * group 2-c
  *   
  */
package RastgeleKarakter;

/**
 *
 * @author furkanyanteri
 */
public class RastgeleKarakter {
    //-----------------------Bir tane veya istenilen sayida rastgele karakter--------------------------------1
    public char rast()//---------------rastgele 1 karaktr verir misin?
    {
        long random=System.currentTimeMillis();//%26;
        random+=(random%10)*(random%10);
        
        // System.out.println(random+"---");
        String chars="abcdefghijklmnopqrstuvwxyz";
        long m=1955343848;
        long k=0;
        while(k!=m)
            k++;
        if (random<0) 
            random*=-1;
        char c;
        long temp;
        temp=random%26;
        c=chars.charAt((int)temp);
        return c;
    }
    public void rast(int a)//--------istedigim sayida rastgele karakter verir misin?
    {
        long m=1234543848;
        long k=0;
        while(k!=m)
            k++;

        System.out.print("Rastgele "+a+" Karakter: ");
        long random=System.currentTimeMillis();
        String srandom=String.valueOf(random);//randomu bu stringe atalim
        //System.out.println("--> srandom = "+srandom);
        //System.out.println("---> random = "+random);
        String chars="abcdefghijklmnopqrstuvwxyz";
        char c;
        for (int i = 0; i < a; i++) {
            // System.out.println(">>> "+srandom+" <<<");
             random=Long.reverse(random)/100+random;
             if(random<0)
                 random*=-1;
             //System.out.println("   "+random);
               //  random=System.currentTimeMillis();
//             srandom=srandom.replace(srandom.charAt(srandom.length()-1),srandom.charAt(0));
  //           srandom=srandom.replace(srandom.charAt(srandom.length()-2),srandom.charAt(1));
            // System.out.println(">>> "+srandom+" <<<");
             
          //   random = Long.parseLong(srandom);
             c=chars.charAt((int)(random%26));
             System.out.print(c);
             //   System.out.println("-->>>> "+srandom);
//             System.out.println("->>>"+srandom.charAt(srandom.length()-1)); 
    }
        System.out.println("");
    }
    //-----------------------Bir tane veya istenilen sayida rastgele karakter---------------------------------1
//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\
    //-------------------Verilen iki karakter arasinda bir veya istenile sayida karakter---------------------2
    //
    public char rast(char a,char b)//1 tane karakter verir misin?
    {
        System.out.print("Verilen 2 Karakter: ");
        int firstChar,secondChar;//girilen karakterleri ascii olarak degerlendirelim
        firstChar=(int)a;//verilen ilk karakterin ascii karsiligi
        secondChar=(int)b;//verilen ikinci karakterin ascii karsiligi
        char temp;//dondurecegimiz karakter burada
        temp=rast();
        //burada 3 ihtimal var verilen iki karakterden hangisi buyuk? veya esit mi? ki esitse sorun olur. 
        if(firstChar>secondChar+1)//aralarinda karakter olabilmesi icin en az iki fazla olmasi lazim!
        {
            if((int)temp>secondChar && (int)temp<firstChar)
                return temp;
            else
            {
                while(((int)temp>secondChar && (int)temp<firstChar)!=true)
                    temp=rast();//temp aralarinda degilken yeni temp yap
                return temp;//olunca da dondur onu.
            }
        }
        else if(secondChar>firstChar+1)
        {
             if((int)temp>firstChar && (int)temp<secondChar)
                return temp;
            else
            {
                while(((int)temp>firstChar && (int)temp<secondChar)!=true)
                    temp=rast();//temp aralarinda degilken yeni temp yap
                return temp;//olunca da dondur onu.
            }                   
        }
        else//girilen iki karakterin aralarinda karakter yok ise hatadir.
        {
            System.out.println("HATA! "+a+" ile "+b+" arasinda karakter bulunmamaktadir.");
            return 0;
        }
    }
    public void rast(char a,char b,int count)//istedigim kadar karakter verir misin?
    {
        System.out.print("Verilen 2 Karakter:"+"("+count+" tane): ");
        long random=System.currentTimeMillis();
        String srandom=String.valueOf(random);
        String chars="abcdefghijklmnopqrstuvwxyz";

        
        int firstChar,secondChar;//girilen karakterleri ascii olarak degerlendirelim
        firstChar=(int)a;//verilen ilk karakterin ascii karsiligi
        secondChar=(int)b;//verilen ikinci karakterin ascii karsiligi
        
        char c;//dondurecegimiz karakter burada
        //burada 3 ihtimal var verilen iki karakterden hangisi buyuk? veya esit mi? ki esitse sorun olur. 
        if(firstChar>secondChar+1)//aralarinda karakter olabilmesi icin en az iki fazla olmasi lazim!
        {
            for (int i = 0; i < count; i++) {
                random=Long.reverse(random)/100+random;
                if(random<0)
                    random*=-1;
                c=chars.charAt((int)(random%26));
                if ((int)c<firstChar && (int)c>secondChar)
                {
                    System.out.print(c);
                    
                }
                else
                {
                    while(((int)c>=firstChar || (int)c<=secondChar)){
                      //  System.out.println("asdasd");
                        random=Long.reverse(random)/100+random;
                        if(random<0)
                            random*=-1;
                    c=chars.charAt((int)(random%26));
                    }
                    System.out.print(c);
                }
            }

        }
//----------------------------------------        
        else if(secondChar>firstChar+1)//aralarinda karakter olabilmesi icin en az iki fazla olmasi lazim!
        {
            for (int i = 0; i < count; i++) {
                random=Long.reverse(random)/100+random;
                if(random<0)
                    random*=-1;
                c=chars.charAt((int)(random%26));
                if ((int)c>firstChar && (int)c<secondChar)
                {
                    System.out.print(c);
                    
                }
                else
                {
                    while(((int)c<=firstChar || (int)c>=secondChar)){
                      //  System.out.println("asdasd");
                        random=Long.reverse(random)/100+random;
                        if(random<0)
                            random*=-1;
                    c=chars.charAt((int)(random%26));
                    }
                    System.out.print(c);
                }
            }

        }
        else//girilen iki karakterin aralarinda karakter yok ise hatadir.
        {
            System.out.println("HATA! "+a+" ile "+b+" arasinda karakter bulunmamaktadir.");
        }
        System.out.println("");

    }
    //-------------------Verilen iki karakter arasinda bir veya istenile sayida karakter----------------------2
//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\
    //-------------------Verilen karakterler arasindan secim yap
    public char rast(char a,char b,char c,char d,char e,char f)//sadece 1 tane istiyorum
    {
        
        System.out.print("Belirtilen Karakterler("+a+","+b+","+c+","+d+","+e+","+f+") :");
        char x;//aradigim karakter sensin bebegim
        x=rast();
        if (x==a || x==b || x==c || x==d || x==e || x==f)
            return x;
        else
        {
            while((x==a || x==b || x==c || x==d || x==e || x==f)!=true)
            {
                x=rast();
            }
            return x;
        }
        
    }
    public void rast(char a,char b,char c,char d,char e,char f,int count)//istedigim sayida ver lutfen
    {
        System.out.print("Belirtilen Karakterler("+a+","+b+","+c+","+d+","+e+","+f+")("+count+"tane) :");
        long random=System.currentTimeMillis();
        String chars="abcdefghijklmnopqrstuvwxyz";
        char x;
        for (int i = 0; i < count; i++) {
            random = Long.reverse(random)+random%(random%10+(random/10000)%10);
            if (random < 0) {
                random *= -1;
            }
            x = chars.charAt((int) (random % 26));
            if(x==a || x==b || x==c || x==d || x==e || x==f)
                System.out.print(x+" ");
            else
            {
                while((x==a || x==b || x==c || x==d || x==e || x==f)!=true){
                    random = Long.reverse(random) / 100 + random;
                    if (random < 0) {
                        random *= -1;
                    }
                    x = chars.charAt((int) (random % 26));
                    if (random < 0) {
                        random *= -1;
                    }
                }
                System.out.print(x+" ");
            }
        }
        System.out.println("");
    }/*
    public String cumle()
    {
        String cumlem;
        char[] arr;//bunu cumleme koyacagim
        int size;
        int spacer;
        long random=System.currentTimeMillis();//%26;
        long a=random%10;
        while(a<130)//kelime cok kisa olmasin 50 sayisi o yuzden secildi
            a*=a;
        a=a+(random%1000)/100;
        size=(int)a;
        if(size<0)
            size*=-1;
        arr = new char[(int)a];
        for (int i = 0; i <size; i++) {
            arr[i]=rast();
        }
        spacer=size%2+size%5+size%10;
        spacer=spacer%10;//kac tane bosluk olacagi belirsiz
        int heyyo;
        for (int k = 0; k < spacer; k++) {
            heyyo=(int)(k+spacer);
            if(k+size<spacer)
                arr[k+size]=' ';
            else
            {
                while(heyyo>spacer)
                {
                    random=System.currentTimeMillis();
                    random=Long.reverse(random);
                    if (random<0)
                        random*=-1;
                    heyyo=(int)random%spacer;
                    if(heyyo<0)
                        heyyo*=-1;
                }
                arr[heyyo]=' ';
            }
        }
        cumlem=arr.toString();
        return cumlem;
    }*/
    //-------------------Verilen karakterler arasindan secim yap
}
