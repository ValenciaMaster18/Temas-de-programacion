import java.util.Scanner;

public class WhileDo {
    public static void main(String args[]) {
        Scanner entrada = new Scanner(System.in);
        int i =1,contador;
        System.out.println("Digite el numero de ejecuciones: ");
        contador = entrada.nextInt();

        do{
            System.out.println(i);
            i +=1;
        }
        while (i<=contador);


        
    }
    
}
