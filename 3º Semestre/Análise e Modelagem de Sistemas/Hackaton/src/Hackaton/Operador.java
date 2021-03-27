package Hackaton;

import javax.swing.*;
import java.io.*;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;

public class Operador {
    public boolean operador(int numEts) throws FileNotFoundException {
        Scanner scan = new Scanner(System.in);
        Etiqueta et = new Etiqueta();
        String maquina, parada, prioridade, descricao, operador;
        int linha;
        char firstChar;

        while (true)
        {
            System.out.print("Nome da máquina: ");
            maquina= scan.nextLine();
            et.setMaquina(maquina);



            System.out.print("Linha [1-6]: ");
            if (scan.hasNextInt()){
                linha = scan.nextInt();
                if (linha >= 1 && linha <= 6){
                    et.setLinha(linha);
                } else {
                    System.out.println("Digite um número de 1 a 6!");
                    break;
                }
            } else {
                System.out.println("Digite um número!");
                break;
            }

            scan.nextLine();

            /*

            System.out.print("Prioridade [Baixa/Média/Alta]: ");
            prioridade = scan.nextLine();
            et.setPrioridade(prioridade);

            System.out.print("Houve parada? [S/N]: ");
            parada = scan.nextLine();
            firstChar = parada.charAt(0);
            et.setParada(firstChar == 'S');

            et.setData(LocalDate.now().format(DateTimeFormatter.ofPattern("dd-MM-yyyy")));
            et.setHorario(LocalTime.now().format(DateTimeFormatter.ofPattern("HH:mm:ss")));

            System.out.print("Descrição: ");
            descricao = scan.nextLine();
            et.setDescricao(descricao);

            System.out.print("Operador: ");
            operador = scan.nextLine();
            et.setOperador(operador);

             */


            try {
                FileOutputStream fout = new FileOutputStream("etiqueta" + numEts + ".ser");
                ObjectOutputStream oos = new ObjectOutputStream(fout);
                oos.writeObject(et);
                fout.close();
                oos.close();
                return true;
            } catch (IOException e) {
                return false;
            }
        }
        return false;
    }
}
