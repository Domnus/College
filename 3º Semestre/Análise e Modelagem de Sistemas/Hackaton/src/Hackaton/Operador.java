package Hackaton;

import javax.swing.*;
import java.io.*;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;

public class Operador {
    public void operador() throws FileNotFoundException {
        Etiqueta et = new Etiqueta();
        String x;
        et.writeMaquina(JOptionPane.showInputDialog("Digite o nome da máquina: "));
        et.writeLinha(Integer.parseInt(JOptionPane.showInputDialog("Informe a linha: [1-6]")));
        et.writePrioridade(JOptionPane.showInputDialog("Informe a prioridade: [Baixa/Média/Alta]"));
        x = JOptionPane.showInputDialog("Houve parada? [S/N]");
        et.writeParada(x.toUpperCase().equals("S"));
        et.writeData(LocalDate.now().format(DateTimeFormatter.ofPattern("dd-MM-yyyy")));
        et.writeHorario(LocalTime.now().format(DateTimeFormatter.ofPattern("HH:mm:ss")));
        et.writeDescricao(JOptionPane.showInputDialog("Informe a descrição da etiqueta: "));
        et.writeOperador(JOptionPane.showInputDialog("Nome do operador: "));

        try {
            FileOutputStream fout = new FileOutputStream("etiqueta.txt");
            ObjectOutputStream oos = new ObjectOutputStream(fout);
            oos.writeObject(et);
            oos.close();
            JOptionPane.showMessageDialog(null,"Etiqueta criada com sucesso!");
        } catch (IOException e) {
            JOptionPane.showMessageDialog(null,"Não foi possível criar a etiqueta!");
        }
    }
}
