package ex04;

import javax.swing.JOptionPane;

public class Principal {
    public static void main(String[] args) {
        Produto produto = new Produto("Braquete", 500);
        int op;

        do {
            op = Integer.parseInt(JOptionPane.showInputDialog("ESTOQUE\n1 - Repor estoque\n2 - Vender produto\n3 - Exibir dados\n4 - Finalizar"));

            switch(op) {
                case 1:
                    produto.repor(Integer.parseInt(JOptionPane.showInputDialog("Digite a quantidade para repor o estoque:")));
                    break;
                case 2:
                    if (produto.vender(Integer.parseInt(JOptionPane.showInputDialog("Digite a quantidade a ser vendida: ")))) {
                        JOptionPane.showMessageDialog(null,"Venda realizada com sucesso!");
                    } else {
                        JOptionPane.showMessageDialog(null,"Saldo insuficiente para venda!");
                    }
                    break;
                case 3:
                    produto.exibirDados();
                    break;
            }
        } while (op != 4);
    }
    
}
