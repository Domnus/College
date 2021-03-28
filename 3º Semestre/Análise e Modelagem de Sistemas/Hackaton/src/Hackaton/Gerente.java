package Hackaton;

import java.io.*;
import java.util.*;
import java.util.ArrayList;

public class Gerente {

    public void gerente(int numEts) throws IOException, ClassNotFoundException {
        ArrayList<Etiqueta> etiquetas = new ArrayList<>();
        ArrayList<String> problema;
        int numLinhas = 6;
        Hashtable<Integer, Float> porcentagemLinhas = new Hashtable<>();

        for (int i = 0; i < numEts; i++) {
            LerEtiqueta etiqueta = new LerEtiqueta();
            Etiqueta et = etiqueta.lerEtiqueta(i);
            etiquetas.add(et);
        }

        NumProblemas problemas = new NumProblemas();
        problema = problemas.numProblemas(numEts, etiquetas);

        System.out.println("----------------------------------------------------------");
        System.out.println("Máquina com maior problemas: " +problema.get(0)+ "\nNúmero de etiquetas criadas: " +problema.get(1));
        System.out.println("----------------------------------------------------------");

        PorcentagemLinhas porLinhas = new PorcentagemLinhas();
        porcentagemLinhas = porLinhas.porcentagemLinhas(etiquetas, numEts, numLinhas);


        System.out.println("Porcentagem de problemas por linha:");
        for (int i = 0; i < numLinhas; i++){
            System.out.format("Linha %d: "+" %.2f", (i+1),porcentagemLinhas.get(i));
            System.out.println("%");
        }
        System.out.println("----------------------------------------------------------");
    }
}
