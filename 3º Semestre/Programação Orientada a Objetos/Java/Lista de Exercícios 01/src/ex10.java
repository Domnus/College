import javax.swing.*;

public class ex10 {
    static String verificaTriangulo(int a, int b, int c) {
        if (a < b + c && b < a + c && c < a + b) {
            if (a == b && b == c) {
                return "Triângulo Equilátero";
            } else if (a == b || b == c || c == a) {
                return "Triângulo Isósceles";
            } else
                return "Triângulo Escaleno";
        }
        return"Não forma um triângulo";
    }

    public static void main(String[] args) {
        int l1 = Integer.parseInt(JOptionPane.showInputDialog("Digite o primeiro lado: "));
        int l2 = Integer.parseInt(JOptionPane.showInputDialog("Digite o segundo lado: "));
        int l3 = Integer.parseInt(JOptionPane.showInputDialog("Digite o terceiro lado: "));

        JOptionPane.showMessageDialog(null,verificaTriangulo(l1,l2,l3));
    }
}
