import java.util.Scanner;

public class Ejercicios {
    public static void main (String args[]) {
        Scanner notas = new Scanner(System.in);
        int n1 , n2 , n3;
        int suma = 0;

        System.out.println("Digite '3' notas: ");
        n1 = notas.nextInt();
        n2 = notas.nextInt();
        n3 = notas.nextInt();

        suma = n1 + n2 + n3;
        System.out.println("La suma de las notas es: " + suma);
// EJERCICIO 2

        Scanner entrada = new Scanner(System.in);
        float Andrea,Luis,Eduardo;
        float total;

        System.out.println("Cuanto dinero tiene Andrea: ");
        Andrea = entrada.nextFloat();
        
        Luis = Andrea/2;
        Eduardo = (Andrea+Luis)/2;
        total = Andrea + Luis + Eduardo;
        System.out.println("El total es: " + total);
// EJERCICIO 3       

        Scanner entrada1 = new Scanner(System.in);
        float Participacion, primerExamen, segundoExamen, examenFinal, notaFinal;

        System.out.println("Digite nota de participacion en clase: ");
        Participacion = entrada1.nextFloat();
        System.out.println("Digite nota primer examen: ");
        primerExamen = entrada1.nextFloat();
        System.out.println("Digite nota segundo examen: ");
        segundoExamen = entrada1.nextFloat();
        System.out.println("Digite nota del examen final: ");
        examenFinal = entrada1.nextFloat();

        Participacion *= 0.10f;
        primerExamen *= 0.25f;
        segundoExamen *= 0.25f;
        examenFinal *= 0.40f;

        notaFinal = Participacion + primerExamen + segundoExamen + examenFinal;

        System.out.println("La nota final es : " + notaFinal + "%");
// EJERCICIO 4
        Scanner entrada3 = new Scanner(System.in);
        int horasTotales, semanas,dias,horas;
        System.out.println("Digite el numero de horas: ");
        horasTotales = entrada3.nextInt();

        semanas = horasTotales/168;
        dias = horasTotales%168 / 24;
        horas = horasTotales%24;

        System.out.println("Numero de semanas: " + semanas);
        System.out.println("Numero de dias: " + dias);
        System.out.println("Numero de horas: " + horas);
     }
    
}
