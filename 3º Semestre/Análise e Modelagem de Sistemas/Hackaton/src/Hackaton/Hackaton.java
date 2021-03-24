package Hackaton;

import javax.swing.*;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;

public class Hackaton {
    public static void main(String[] args) throws IOException, ClassNotFoundException {
        int op;

        do {
            op = Integer.parseInt(JOptionPane.showInputDialog("ETIQUETAS ADODAS\n1 - Operador\n2 - Gerente\n0 - Finalizar"));

            switch (op) {
                case 1 -> {
                    Operador opr = new Operador();
                    opr.operador();
                }
                case 2 -> {
                    Gerente ger = new Gerente();
                    ger.gerente();
                }
            }
        } while (op != 0);
    }
}
