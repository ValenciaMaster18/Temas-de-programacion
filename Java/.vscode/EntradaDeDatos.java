
//ENTRADA DE Entrada POR CONSOLA
import java.util.Scanner;




public class EntradaDeDatos {
    public static void main(String args []) {
        
        try (Scanner entrada = new Scanner (System.in)) {
            int numero;

            System.out.println("Digite un numero: ");

            numero = entrada.nextInt();

            System.out.println("El numero es: " + numero);
        }
        
    }
    
}
