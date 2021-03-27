package Hackaton;

import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Objects;

public class Gerente {

    public void gerente(int numEts) throws IOException, ClassNotFoundException {
        ArrayList<Etiqueta> etiquetas = new ArrayList<>();
        ArrayList<String> problema;
        int cont1, cont2 = 0;
        int numLinhas = 6;

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


        Map<String, Integer> linhas = new HashMap<String, Integer>();
        Map<String, Float> linhasPorcentagem = new HashMap<>();

        for (int i = 0; i < numEts; i++){
            cont1 = 0;
            int linha = etiquetas.get(i).getLinha();
            for (int j = 0; j < numEts; j++){
                if (linha == etiquetas.get(j).getLinha()){
                    cont1++;
                }
            }
            linhas.put(String.valueOf(linha), cont1);
        }

        System.out.println(linhas);

        /*
        for (int i = 0; i < numLinhas ; i++){
            try {
                float numProblemas = Float.parseFloat(linhas.get(String.valueOf(i + 1)));
                float porcentagem = numEts * (numProblemas / 100);
                linhasPorcentagem.put(String.valueOf(i), porcentagem);
            } catch (NullPointerException ignored){
            }
        }


        for (int i = 0; i < numLinhas; i++){
            System.out.println("Linha " +i+ ": " +linhasPorcentagem.get(String.valueOf(i+1))+ "%");
        }
         */

        System.out.println(linhas.get("1"));
    }
}
