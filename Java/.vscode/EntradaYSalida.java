import javax.swing.JOptionPane; //Este import saca una ventana emergente para preguntar en la entrda

//ENTRADA Y SALIDA DE Entrada CON 'Joptionpate'

public class EntradaYSalida {
    public static void main(String [] args) {
        String  cadena;
        int entero;
        double decimal;
        char letra;
        
        cadena = JOptionPane.showInputDialog("Digite una cadena: ");
        // Este metodo convierte esta cadena en entero ' Integer.parseInt'
        entero = Integer.parseInt(JOptionPane.showInputDialog("Digite un entero: "));
        decimal =  Double.parseDouble(JOptionPane.showInputDialog("Digite un decimal: "));
        letra = JOptionPane.showInputDialog("Digite un caracter: ").charAt(0);
        // Salida de Entrada con ventanas emergente 'JOptionPane.showMessageDialog'

        JOptionPane.showMessageDialog(null,"La cadena es: " + cadena);
        JOptionPane.showMessageDialog(null,"El entero es: " + entero);
        JOptionPane.showMessageDialog(null,"El decimal es: " + decimal);
        JOptionPane.showMessageDialog(null,"El caracter es: " + letra);
        
    }

    
}
