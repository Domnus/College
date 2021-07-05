// Andressa Caroline R. Bueno RA: 607290
// Bento Carlos S. dos Santos RA: 600784
// Fernando Cremonez Costa    RA: 604097
// Frederico Hanai            RA: 604593
// Hugo Seiti Odajima         RA: 606537

package banco.gui;

import java.util.ArrayList;
import javax.swing.UIManager;

class Conta {
    private int numero;
    private String tipo;
    private float saldo;
    private String senha;

    public Conta(int numero, String tipo, float saldo, String senha) {
        this.numero = numero;
        this.tipo = tipo;
        this.saldo = saldo;
	this.senha = senha;
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

    public String getSenha() {
	return senha;    
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
    private int numConta = 0;

    public Banco() {
        clientes = new ArrayList<Cliente>();
    }

    public void cadastrar(Cliente c) {
        this.clientes.add(c);
		numConta += 1;
    }

    public Cliente consultarNome(String nome) {
        for (Cliente c : this.clientes) {
            if (c.getNome().equals(nome)) {
                return c;
            }
        }
        return null;
    }

    public Cliente consultarNumero(int numero) {
        for (Cliente c : this.clientes) {
            if (c.getConta().getNumero() == numero) {
                return c;
            }
        }
        return null;
    }

    public boolean depositar(int numConta, float valor) {
        for (Cliente c : this.clientes) {
            if (c.getConta().getNumero() == numConta) {
                c.getConta().depositar(valor);
                return true;
            }
        }
        return false;
    }

    public boolean sacar(int numConta, float valor) {
        for (Cliente c : this.clientes) {
            if (c.getConta().getNumero() == numConta) {
                return c.getConta().sacar(valor);
            }
        }
        return false;
    }

    public boolean transferir(int origem, int destino, float valor) {
        for (Cliente c : this.clientes) {
            if (c.getConta().getNumero() == origem) {
                for (Cliente cl : this.clientes) {
                    if (cl.getConta().getNumero() == destino) {
                        return c.getConta().transferir(valor, cl.getConta());
                    }
                }
            }
        }
        return false;
    }
    
    public int getNumConta() {
		return numConta;    
    }
	
	public ArrayList<Cliente> getClientes() {
		return this.clientes;
	}
}

public class BancoGUI {
    public static void main(String[] args) {
        try {
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
        } catch (Exception e) {
            e.printStackTrace();
        }

        frmHome frameHome = new frmHome();
        frameHome.setVisible(true);
    }
}