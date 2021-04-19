package ex04;

import javax.swing.JOptionPane;

public class Produto {
    String descricao;
    float preco;
    int qtde_disp;
    int qtde_ved;

    public Produto(String descricao, float preco) {
        this.descricao = descricao;
        this.preco = preco;
    }

    void repor(int qtde) {
        qtde_disp += qtde;
    }

    boolean vender(int qtde) {
        if (qtde_disp >= qtde) {
            qtde_disp -= qtde;
            return true;
        } else {
            return false;
        }
    }

    void exibirDados() {
        JOptionPane.showMessageDialog(null, descricao.toUpperCase()+ "\nDescrição: " +descricao+ "\nPreço: R$" +preco+ "\nQuantidade disponível: " +qtde_disp+ " unidades");
    }
}