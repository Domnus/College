package ex02;

import javax.swing.*;

class Pessoa {
    String nome;
    String telefone;
    int idade;

    public Pessoa(String nome, String telefone, int idade) {
        this.nome = nome;
        this.telefone = telefone;
        this.idade = idade;
    }

    public void fazAniversario() {
        idade++;
    }

    public void atualizaTelefone(String novoFone) {
        telefone = novoFone;
    }
}

public class Principal {
    public static void main(String[] args) {
        String nome = JOptionPane.showInputDialog("Nome da pessoa:");
        String telefone = JOptionPane.showInputDialog("Telefone da pessoa:");

        int idade = Integer.parseInt(JOptionPane.showInputDialog("Idade:"));

        Pessoa p = new Pessoa(nome, telefone, idade);

        System.out.println("Nome: " +p.nome+ "\nTelefone: " +p.telefone+ "\nIdade: " +p.idade);
        p.fazAniversario();
        p.atualizaTelefone(JOptionPane.showInputDialog("Novo telefone:"));
        System.out.println("Idade depois do aniversário: " + p.idade);
        System.out.println("Telefone atualizado: " +p.telefone);
    }
}

