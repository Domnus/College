package Hackaton;

import javax.swing.*;
import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class Hackaton {
    public static void main(String[] args) throws IOException, ClassNotFoundException {
        Scanner scan = new Scanner(System.in);
        int op;
        int numEts = 0;
        do {
            System.out.println("ETIQUETAS ADODAS\n1 - Operador\n2 - Gerente\n0 - Finalizar");
            System.out.print("-> ");
            op = scan.nextInt();

            switch (op) {
                case 1 -> {
                    Operador opr = new Operador();
                    if (opr.operador(numEts)) {
                        System.out.println("Etiqueta criada com sucesso!");
                        numEts++;
                    } else {
                        System.out.println("Não foi possível criar a etiqueta!");
                    }
                }
                case 2 -> {
                    Gerente ger = new Gerente();
                    ger.gerente(numEts);
                }
            }
        } while (op != 0);

        for (int i = 0; i < numEts; i++) {
            File file = new File("etiqueta" + i + ".ser");
            file.delete();
        }
    }
}
