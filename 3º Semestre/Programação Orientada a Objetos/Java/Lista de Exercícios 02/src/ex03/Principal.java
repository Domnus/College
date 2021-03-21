package ex03;

import javax.swing.*;
import java.util.Scanner;

public class Principal {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Conta cliente = new Conta(0);
        int op;

        do {
            op = Integer.parseInt(JOptionPane.showInputDialog("CONTA CORRENTE\n1 - Depósito\n2 - Saque\n3 - Consulta Saldo\n4 - Finalizar"));
            switch(op) {
                case 1:
                    cliente.depositar(Float.parseFloat(JOptionPane.showInputDialog("Digite o valor a ser depositado: ")));
                    JOptionPane.showMessageDialog(null,"Depósito realizado com sucesso!");
                    break;
                case 2:
                    if (cliente.sacar(Float.parseFloat(JOptionPane.showInputDialog("Digite o valor a ser sacado: ")))) {
                        JOptionPane.showMessageDialog(null, "Saque realizado com sucesso!");
                    }
                    else {
                        JOptionPane.showMessageDialog(null, "Você não tem saldo suficiente!");
                    }
                    break;
                case 3:
                    JOptionPane.showMessageDialog(null,"Saldo atual: R$" + cliente.retornaSaldo());
                    break;
            }
        } while (op !=4);
        /*
        do {
            System.out.println("CONTA CORRENTE");
            System.out.println("1 - Depósito");
            System.out.println("2 - Saque");
            System.out.println("3 - Consulta Saldo");
            System.out.println("4 - Finalizar");
            System.out.print("--> ");
            op = scan.nextInt();

            switch(op) {

                case 1:
                    System.out.println("Digite o valor a ser depositado: ");
                    cliente.depositar(scan.nextFloat());
                    System.out.println("Depósito realizado com sucesso!");
                case 2:
                    System.out.println("Digite o valor a ser sacado: ");
                    if (cliente.sacar(scan.nextFloat())) {
                        System.out.println(("Saque realizado com sucesso!"));
                    }
                    else {
                        System.out.println("Você não tem saldo suficiente!");
                    }
                case 3:
                    System.out.println("Saldo atual: " + cliente.retornaSaldo());
            }
        } while (op != 4);
         */
    }
}

