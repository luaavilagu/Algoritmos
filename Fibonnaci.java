
package fibonnaci;
import java.util.*;
/**
 * @author alejandro.avila
 * Tomado de : http://puntocomnoesunlenguaje.blogspot.com.co/2012/11/fibonacci-en-java.html
 */
public class Fibonnaci {

    /* 
    int : 47
    long : 549
    short : 1
    */
    
    public static void main(String[] args){
        short numero;
        short fibo1;
        short fibo2;
        short i;
        
        numero = 1;

        fibo1=1;
        fibo2=1; 

        for(i=2;i<=numero;i++){
           
             fibo2 = fibo1 + fibo2;
             fibo1 = fibo2 - fibo1;
        }
        System.out.println(fibo2);
    }
}

