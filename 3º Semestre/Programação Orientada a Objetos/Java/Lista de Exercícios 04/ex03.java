class Conta{
    private int numero;
    private String tipo;
    private float saldo;

    public Conta(int numero, String tipo, float saldo) {
        this.numero = numero;
        this.tipo = tipo;
        this.saldo = saldo;
    }

    public void depositar(float valor){
        this.saldo += valor;
    }

    public boolean sacar(float valor){
        if (valor <= this.saldo){
            this.saldo -= valor;
            return true;
        } else {
            return false;
        }
    }

    public int getNumero() {
        return numero;
    }

    public String getTipo() {
        return tipo;
    }

    public float getSaldo() {
        return saldo;
    }

    public boolean transferir(float valor, Conta destino){
        if (valor <= this.saldo){
            destino.depositar(valor);
            return true;
        } else {
            return false;
        }
    }
}

class Cliente{
    private String nome;
    private String CPF;
    private String endereco;
    private String telefone;
    private Conta conta;

    public Cliente(String nome, String CPF, String endereco, String telefone, Conta conta) {
        this.nome = nome;
        this.CPF = CPF;
        this.endereco = endereco;
        this.telefone = telefone;
        this.conta = conta;
    }

    public String getNome() {
        return nome;
    }

    public String getCPF() {
        return CPF;
    }

    public String getEndereco() {
        return endereco;
    }

    public String getTelefone() {
        return telefone;
    }

    public Conta getConta() {
        return conta;
    }
}

public class ex03 {
    public static void main(String[] args){
        Cliente c1, c2;
        c1 = new Cliente("Bento Carlos", "43412618861", "Avenida Brasil", "34172917", new Conta(0001, "Poupança", 0));
        c2 = new Cliente("Hugo Seiti", "12345678901", "Rua Dom Pedro", "40022922", new Conta(0002, "Poupança", 0));

        c1.getConta().depositar(500);
        System.out.println("Depositado R$500 na conta de " +c1.getNome());
        c2.getConta().depositar(500);
        System.out.println("Depositado R$500 na conta de " +c2.getNome());

        c1.getConta().sacar(100);
        System.out.println("Saque de R$100 realizado na conta de " +c1.getNome());
        c2.getConta().sacar(100);
        System.out.println("Saque de R$100 realizado na conta de " +c2.getNome());

        if (c1.getConta().transferir(200, c2.getConta())){
            System.out.println("Transferência realizada com sucesso!");
        } else {
            System.out.println("A transferência não pôde ser realizada!");
        }
    }
}
