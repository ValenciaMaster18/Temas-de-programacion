import java.util.Scanner;

import javax.swing.JOptionPane;

public class Sena{
    public static void main(String args[]){
        String nombre,nombre2,sexo,sexo2;
        int edad,edad2;
        JOptionPane.showMessageDialog(null,"Primer encuestado");
        nombre = JOptionPane.showInputDialog("Cual es tu nombre: ");
        edad = Integer.parseInt(JOptionPane.showInputDialog("Digite su edad: "));
        sexo = JOptionPane.showInputDialog("Digite su sexo: ");
        JOptionPane.showMessageDialog(null,"Segunda persona encuestada");
        nombre2 = JOptionPane.showInputDialog("Cual es tu nombre: ");
        edad2 = Integer.parseInt(JOptionPane.showInputDialog("Digite su edad: "));
        sexo2 = JOptionPane.showInputDialog("Digite su sexo:");

        if (edad > edad2){
            JOptionPane.showMessageDialog(null, nombre + " tiene "+ edad +" años. Es mayor de edad. "+ " Sexo "+ sexo);
        
       }else{
        if (edad2 > edad){
            JOptionPane.showMessageDialog(null, nombre2 + " tiene "+ edad2 +" años. Es mayor de edad. "+ " Sexo "+ sexo2);
       }else{
          JOptionPane.showMessageDialog(null,"Tiene la misma edad");
       }
    }

Scanner datos = new Scanner(System.in);
String nombre3,nombre4,sexo3,sexo4;
int edad3,edad4;

System.out.println("Primer usuario encuestado");

System.out.println("Digite su nombre: ");
nombre3 = datos.next();
System.out.println("Digite su edad: ");
edad3 = datos.nextInt();
System.out.println("Digite su sexo: ");
sexo3 = datos.next();

System.out.println("Segundo usuario encuestado");

System.out.println("Digite su nombre: ");
nombre4 = datos.next();
System.out.println("Digite su edad: ");
edad4 = datos.nextInt();
System.out.println("Digite su sexo: ");
sexo4 = datos.next();
if (edad > edad2){
    System.out.println(nombre3 + " tiene "+ edad3 +" años. Es mayor de edad. "+ " Sexo "+ sexo3);
}else{

if (edad2 > edad){
    System.out.println(nombre4 + " tiene "+ edad4 +" años. Es mayor de edad. "+ " Sexo "+ sexo4);
}else{
    System.out.println("Tiene la misma edad");
    }
    }


  }
}