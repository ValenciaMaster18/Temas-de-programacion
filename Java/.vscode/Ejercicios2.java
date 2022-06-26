import javax.swing.JOptionPane;

public class Ejercicios2{
    public static void main(String args[]){
        int numero;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));

        if (numero %10==0){
            JOptionPane.showMessageDialog(null, "El numero " +numero+ "es multiplo de 10");        
        }
        else{
            JOptionPane.showMessageDialog(null, "El numero "+numero+" no es multiplo de 10");
        }
        char letra;
        letra = JOptionPane.showInputDialog("Digite una letra: ").charAt(0);
        // Esta es una funcion para saber si la letra es mayuscula 
        if (Character.isUpperCase(letra)){
            JOptionPane.showMessageDialog(null, "La letra es mayuscula");

        }
        else{
            JOptionPane.showMessageDialog(null, "La letra es minusculas");
        }

        int horasTrabajadas;
        float salarioTotal;

        horasTrabajadas = Integer.parseInt(JOptionPane.showInputDialog("Digite horas trabjadas: "));
        
        if (horasTrabajadas <=40){
            salarioTotal = horasTrabajadas * 16;
        }
        else{
            salarioTotal = (40*16) + (horasTrabajadas - 40)*20;
        }
        JOptionPane.showMessageDialog(null, "El salario total: " + salarioTotal);
    }

    
}