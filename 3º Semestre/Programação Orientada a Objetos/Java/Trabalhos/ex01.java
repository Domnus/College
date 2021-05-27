// Andressa Caroline R. Bueno RA: 607290
// Bento Carlos S. dos Santos RA: 600784
// Fernando Cremonez Costa    RA: 604097
// Frederico Hanai            RA: 604593
// Hugo Seiti Odajima         RA: 606537

package Trabalhos;

import javax.swing.JOptionPane;
import java.util.ArrayList;

class Conta {
    private int numero;
    private String tipo;
    private float saldo;

    public Conta(int numero, String tipo, float saldo) {
        this.numero = numero;
        this.tipo = tipo;
        this.saldo = saldo;
    }

    public void depositar(float valor) {
        this.saldo += valor;
    }

    public boolean sacar(float valor) {
        if (this.saldo >= valor){
            saldo -= valor;
            return true;
        }
        return false;
    }

    public boolean transferir(float valor, Conta destino){
        if (this.saldo >= valor){
            destino.depositar(valor);
            this.saldo -= valor;
            return true;
        }
        return false;
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
}

class Cliente {
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

class Banco {
    private ArrayList<Cliente> clientes;

    public Banco() {
        clientes = new ArrayList<Cliente>();
    }

    public void cadastrar(Cliente c) {
        this.clientes.add(c);
    }

    public Cliente consultar(String nome) {
        for (Cliente c : this.clientes) {
            if (c.getNome().equals(nome)) {
                return c;
            }
        }
        return null;
    }

    public boolean depositar(String nome, float valor) {
        for (Cliente c : this.clientes) {
            if (c.getNome().equals(nome)) {
                c.getConta().depositar(valor);
                return true;
            }
        }
        return false;
    }

    public boolean sacar(String nome, float valor) {
        for (Cliente c : this.clientes) {
            if (c.getNome().equals(nome)) {
                return c.getConta().sacar(valor);
            }
        }
        return false;
    }

    public boolean transferir(String origem, String destino, float valor) {
        for (Cliente c : this.clientes) {
            if (c.getNome().equals(origem)) {
                for (Cliente cl : this.clientes) {
                    if (cl.getNome().equals(destino)) {
                        return c.getConta().transferir(valor, cl.getConta());
                    }
                }
            }
        }
        return false;
    }
}

public class ex01 {
    public static void main(String[] args) {
        Banco banco = new Banco();
        int op;
        int numConta = 0;

        do {
            op = Integer.parseInt(JOptionPane.showInputDialog(null,"1 - Cadastrar cliente/conta\n2 - Consultar\n3 - Depositar\n4 - Sacar\n5 - Transferir\n6 - Finalizar\nOpção:", "Agenda", JOptionPane.INFORMATION_MESSAGE));

            switch (op) {
                case 1:
                    cadastrar(banco, numConta);
                    numConta++;

                    break;

               case 2:
                   Cliente cliente = consultar(banco);
                   if (cliente != null) {
                       JOptionPane.showMessageDialog(null, "Nome: " +cliente.getNome()+ "\nCPF: " +cliente.getCPF()+ "\nEndereço: " +cliente.getEndereco()+ "\nTelefone: " +cliente.getTelefone()+ "\nTipo da conta: " +cliente.getConta().getTipo()+ "\nSaldo: R$" +cliente.getConta().getSaldo(), "Consulta", JOptionPane.INFORMATION_MESSAGE);
                   } else {
                       JOptionPane.showMessageDialog(null, "Cliente não existe!", "Consultar", JOptionPane.ERROR_MESSAGE);
                   }

                   break;

                case 3:
                    depositar(banco);

                    break;

                case 4:
                    if (sacar(banco)) {
                        JOptionPane.showMessageDialog(null, "Valor retirado com sucesso!", "Saque", JOptionPane.INFORMATION_MESSAGE);
                    } else {
                        JOptionPane.showMessageDialog(null, "Saldo insuficiente!", "Saque", JOptionPane.ERROR_MESSAGE);
                    }

                    break;

                case 5:
                    if (transferir(banco))  {
                        JOptionPane.showMessageDialog(null, "Transferência realizada com sucesso!", "Transferência", JOptionPane.INFORMATION_MESSAGE);
                    } else {
                        JOptionPane.showMessageDialog(null, "Saldo insuficiente!", "Transferência", JOptionPane.ERROR_MESSAGE);
                    }

                    break;
            }
        } while (op != 6);

    }

    private static void cadastrar(Banco banco, int numConta) {
        String nome = JOptionPane.showInputDialog(null, "Nome: ", "Cadastro", JOptionPane.QUESTION_MESSAGE);
        String CPF = JOptionPane.showInputDialog(null, "CPF: ", "Cadastro", JOptionPane.QUESTION_MESSAGE);
        String endereco = JOptionPane.showInputDialog(null, "Endereço: ", "Cadastro", JOptionPane.QUESTION_MESSAGE);
        String telefone = JOptionPane.showInputDialog(null, "Telefone: ", "Cadastro", JOptionPane.QUESTION_MESSAGE);
        String tipoConta = JOptionPane.showInputDialog(null, "Tipo da conta [Corrente/Poupança]: ", "Cadastro", JOptionPane.QUESTION_MESSAGE);

        banco.cadastrar(new Cliente(nome, CPF, endereco, telefone, new Conta(numConta, tipoConta, 0)));
    }

    private static Cliente consultar(Banco banco) {
        return banco.consultar(JOptionPane.showInputDialog(null, "Nome a ser consultado: ", "Consulta", JOptionPane.QUESTION_MESSAGE));
    }

    private static void depositar(Banco banco) {
        String nome = JOptionPane.showInputDialog(null, "Nome do cliente: ", "Depósito", JOptionPane.QUESTION_MESSAGE);
        float valor = Float.parseFloat(JOptionPane.showInputDialog(null, "Valor a ser depositado: ", "Depósito", JOptionPane.QUESTION_MESSAGE));

        banco.depositar(nome, valor);
        JOptionPane.showMessageDialog(null, "Valor depositado com sucesso!", "Depósito", JOptionPane.INFORMATION_MESSAGE);
    }

    private static boolean sacar(Banco banco) {
        String nome = JOptionPane.showInputDialog(null, "Nome do cliente: ", "Saque", JOptionPane.QUESTION_MESSAGE);
        float valor = Float.parseFloat(JOptionPane.showInputDialog(null, "Valor a ser depositado: ", "Saque", JOptionPane.QUESTION_MESSAGE));

        return banco.sacar(nome, valor);
    }

    private static boolean transferir(Banco banco) {
        String origem = JOptionPane.showInputDialog(null, "Cliente de origem: ", "Transferência", JOptionPane.QUESTION_MESSAGE);
        String destino = JOptionPane.showInputDialog(null, "Cliente de destino: ", "Transferência", JOptionPane.QUESTION_MESSAGE);
        float valor = Float.parseFloat(JOptionPane.showInputDialog(null, "Valor a ser transferido: ", "Transferência", JOptionPane.QUESTION_MESSAGE));

        return banco.transferir(origem, destino, valor);
    }
}