package ex05;

import javax.swing.*;

public class Principal {
    public static void main(String[] args) {
        Aluno aluno = new Aluno("600784", "Bento Carlos");
        int op;
        float n1, n2;

        do  {
            op = Integer.parseInt(JOptionPane.showInputDialog("ALUNO\n1 - Atribuir notas\n2 - Exibir média\n3 - Exibir situação\n4 - Finalizar"));

            switch(op) {
                case 1:
                    n1 = Float.parseFloat(JOptionPane.showInputDialog("Nota 1: "));
                    n2 = Float.parseFloat(JOptionPane.showInputDialog("Nota 2: "));
                    aluno.atribuirNotas(n1, n2);
                    JOptionPane.showMessageDialog(null,"Notas atribuídas!");
                    break;
                case 2:
                    aluno.calcularMedia();
                    JOptionPane.showMessageDialog(null,"A média do aluno " +aluno.Nome+ " é " +aluno.media);
                    break;
                case 3:
                    JOptionPane.showMessageDialog(null,"A situação do aluno " +aluno.Nome+ " é " +aluno.verificarSituacao());
            }

        } while (op != 4);
    }
}
