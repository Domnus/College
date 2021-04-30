// Bento Carlos    RA: 600784
// Frederico Hanai RA: 604593

import java.util.ArrayList;

class Boleto {
    private int numero;
    private float valor;
    private String dataVencimento;
    private String dataPagamento;
    private boolean pago;

    public Boleto(int numero, float valor, String dataVencimento){
        this.numero = numero;
        this.valor = valor;
        this.dataVencimento = dataVencimento;
        this.pago = false;
    }
    public float getValor(){
        return valor;
    }

    public void pagar(String dataPagamento) {
        this.dataPagamento = dataPagamento;
        this.pago = true;
    }

    public int getNumero() {
        return numero;
    }

    public boolean getPago(){
        return pago;
    }

    public String getDataPagamento(){
        return dataPagamento;
    }

    public String getDataVencimento(){
        return dataVencimento;
    }
}

class Aluno {
    private String RA;
    private String nome;
    private String curso;
    private ArrayList<Boleto> mensalidades;

    public Aluno(String RA, String nome, String curso) {
        this.RA = RA;
        this.nome = nome;
        this.curso = curso;
        mensalidades = new ArrayList<Boleto>();
    }

    public String getRA() {
        return RA;
    }

    public String getNome() {
        return nome;
    }

    public Boleto getMensalidade(int numero) {
        for (Boleto boleto : mensalidades) {
            if (numero == boleto.getNumero()) {
                return boleto;
            }
        }
        return null;
    }

    public void setMensalidades(int numero, String dataVencimento, float valor) {
        this.mensalidades.add(new Boleto(numero, valor, dataVencimento));
    }

    public void pagarMensalidades(int numero, String dataPagamento) {
        Boleto boleto = getMensalidade(numero);
        if (boleto != null) {
            boleto.pagar(dataPagamento);
        }
    }
}
public class ex01 {
    public static void main(String[] args) {
        Aluno aluno = new Aluno("600784", "Bento", "Ciência da Computação");

        aluno.setMensalidades(1, "11/02/2021", 1380f);
        aluno.setMensalidades(2, "11/03/2021", 1380f);
        aluno.setMensalidades(3, "11/04/2021", 1380f);
        aluno.setMensalidades(4, "11/05/2021", 1380f);

        aluno.pagarMensalidades(1, "10/02/2021");
        aluno.pagarMensalidades(2, "10/03/2021");

        for (int i = 1; i <= 4; i++) {
            System.out.println("Número do boleto: " +aluno.getMensalidade(i).getNumero());
            System.out.println("Data de vencimento: " +aluno.getMensalidade(i).getDataVencimento());
            System.out.println("Valor: R$"+aluno.getMensalidade(i).getValor());
            System.out.print("Está pago: ");
            if (aluno.getMensalidade(i).getPago()) {
                System.out.println("Sim");
                System.out.println("Data de pagamento: " +aluno.getMensalidade(i).getDataPagamento());
            } else {
                System.out.println("Não");
            }

            System.out.println();
        }
    }
}
