/**
  *
  * @author Furkan Yanteri	furkan.yanteri@ogr.sakarya.edu.tr  
  * @since 20.03.2019  
  * group 2-c
  */
///lutfen birkac kere deneyiniz
package rastgeletest;
import RastgeleKarakter.RastgeleKarakter;
/**
 *
 * @author furkanyanteri
 */
public class RastgeleTest {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        RastgeleKarakter ornek=new RastgeleKarakter();//nesnemiz
        
//---------------------------------------------------------------------------------------------------1        
        System.out.print("Rastgele Karakter: ");
        System.out.println(ornek.rast());//------------>rastgele karakter verir rast() fonksiyonu
        System.out.print("Rastgele Karakter: ");
        System.out.println(ornek.rast());//------------>rastgele karakter verir rast() fonksiyonu
        System.out.print("Rastgele Karakter: ");
        System.out.println(ornek.rast());//------------>rastgele karakter verir rast() fonksiyonu
//---------------------------------------------------------------------------------------------------1        
//---------------------------------------------------------------------------------------------------2        
        ornek.rast(5);//------------>rastgele karakter verir rast() fonksiyonu istenen sayida
        ornek.rast(6);//------------>rastgele karakter verir rast() fonksiyonu istenen sayida
        ornek.rast(7);//------------>rastgele karakter verir rast() fonksiyonu istenen sayida
//---------------------------------------------------------------------------------------------------2        
//---------------------------------------------------------------------------------------------------3      
        System.out.println(ornek.rast('a','g'));//------------>iki karakterin alfabetik olarak arasindan rastgele verir 
        System.out.println(ornek.rast('a','g'));//------------>iki karakterin alfabetik olarak arasindan rastgele verir
        System.out.println(ornek.rast('y','b'));//------------>iki karakterin alfabetik olarak arasindan rastgele verir
//---------------------------------------------------------------------------------------------------3        
//---------------------------------------------------------------------------------------------------2        
        ornek.rast('a','z',4);//------------>iki karakterin alfabetik olarak arasindan rastgele verir istenen sayida
        ornek.rast('w','n',5);//------------>iki karakterin alfabetik olarak arasindan rastgele verir istenen sayida
        ornek.rast('f','t',4);//------------>iki karakterin alfabetik olarak arasindan rastgele verir istenen sayida
//---------------------------------------------------------------------------------------------------4        
//---------------------------------------------------------------------------------------------------5        
        System.out.println(ornek.rast('f','u','r','k','a','n'));//------------>verilen karakterlerin arasindan rastgele sec
        System.out.println(ornek.rast('f','u','r','k','a','n'));//------------>verilen karakterlerin arasindan rastgele sec
        System.out.println(ornek.rast('f','u','r','k','a','n'));//------------>verilen karakterlerin arasindan rastgele sec
//---------------------------------------------------------------------------------------------------5        
//---------------------------------------------------------------------------------------------------6        
        ornek.rast('f','u','r','k','a','n',4);//------------>verilen karakterlerin arasindan rastgele sec istenen sayida
        ornek.rast('d','e','v','r','e','k',5);//------------>verilen karakterlerin arasindan rastgele sec istenen sayida
        ornek.rast('t','u','r','k','e','y',6);//------------>verilen karakterlerin arasindan rastgele sec istenen sayida
//---------------------------------------------------------------------------------------------------6        
   
//        ornek.rast('d','a',10);
//        ornek.rast(3);

        // System.out.println(+ornek.rast('f','u','h','k','a','n'));
       // System.out.println(ornek.rast('f','u','r','k','a','n'));
        //ornek.rast('f','u','r','k','a','n',5);
    
    }
    
}
