import javax.swing.*;

class Media {
    private int soma;
    private int contador;

    public Media() {
        this.soma = 0;
        this.contador = 0;
    }

    public void acumula(int i) {
        this.soma += i;
        this.contador++;
    }

    public float getMedia() {
        return this.soma / (float) this.contador;
    }
}

class MaiorMenor extends Media {
    private int maiorValor, menorValor;

    public MaiorMenor() {
        this.maiorValor = 0;
        this.menorValor = 9999999;
    }

    public void processa(int n) {
        if (n > this.maiorValor)
            this.maiorValor = n;
        if (n < this.menorValor)
            this.menorValor = n;
        this.acumula(n);
    }

    public int getMaior() {
        return this.maiorValor;
    }
    public int getMenor() {
        return this.menorValor;
    }
}
public class ex03 {
    public static void main(String[] args) {
        MaiorMenor m = new MaiorMenor();
        do {
            int n = Integer.parseInt(JOptionPane.showInputDialog("Digite um número inteiro"));
            m.processa(n);
        } while (JOptionPane.showConfirmDialog(null, "Deseja continuar?") == 0);

        JOptionPane.showMessageDialog(null, "Média: " +m.getMedia()+ "\nMaior valor: " +m.getMaior());
    }
}
