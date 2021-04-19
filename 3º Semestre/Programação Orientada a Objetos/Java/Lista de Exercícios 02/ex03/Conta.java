package ex03;

class Conta {
    private int numero;
    private String nomeTitular;
    private float saldo;

    public Conta(int saldoInicial) {
        this.saldo = saldoInicial;
    }

    public void depositar(float valor) {
        this.saldo = saldo + valor;
    }

    public boolean sacar(float valor) {
        if (saldo > 0 && valor <= saldo) {
            saldo = saldo - valor;
            return true;
        } else {
            return false;
        }
    }

    public float retornaSaldo() {
        return saldo;
    }

}
