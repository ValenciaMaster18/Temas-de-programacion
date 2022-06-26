import java.util.Scanner;
/*Llenar una matriz A[ ][ ] de tipo char de tamaño n x m, donde n y m son
 * ingresados por el usuario y deben ser impares, de tal forma que al
 * imprimir A[ ][ ] se visualice por pantalla una pirámide rellena.
 */
public class Unapiramide {
 
    public static void main(String[] args) {
       
        Scanner teclado = new Scanner(System.in);
       
        int n, m;
        boolean numeroCorrecto = false;
       
        do {
            System.out.print("Ingrese cantidad filas (número impar): ");
            n = teclado.nextInt();
            System.out.print("Ingrese cantidad columnas (número impar): ");
            m = teclado.nextInt();
           
            if(n % 2 != 0 && m % 2 != 0) {
                numeroCorrecto = true;
            }else {
                System.out.println("Error. Debe ingresar dos números impares");
            }
            System.out.println();
           
        }while(!numeroCorrecto);
       
        char matriz [][] = new char [n][m];
       
        int mitad = matriz[0].length / 2;
       
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[0].length; j++) {
                if((i+j) >= mitad && (j-i) <= mitad) {
                    matriz [i][j] = '*';
                }else {
                    matriz [i][j] = ' ';
                }
                System.out.print(matriz [i][j]+" ");
            }
            System.out.println();
        }
    }
}

