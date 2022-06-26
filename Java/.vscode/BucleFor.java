import java.util.Scanner;

public class BucleFor {
    public static void main(String args[]) {
        Scanner entrada = new Scanner(System.in);
        int i = 0,contador;
        System.out.println("Digite un numero para el final de iteraciones: ");
        contador = entrada.nextInt();

        for(i=0;i<=contador;i++){
            System.out.println(i);
        }
    }
    
}
