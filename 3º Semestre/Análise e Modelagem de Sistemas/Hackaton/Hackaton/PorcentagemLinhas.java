package Hackaton;

import java.util.*;

public class PorcentagemLinhas {
    public Hashtable<Integer, Float> porcentagemLinhas(ArrayList<Etiqueta> etiquetas, int numEts, int numLinhas){
        float cont1;

        Hashtable<Integer, Float> linhas = new Hashtable<>();
        Hashtable<Integer, Float> linhasPorcentagem = new Hashtable<>();

        for (int i = 0; i < numEts; i++){
            cont1 = 0;
            int linha = etiquetas.get(i).getLinha();
            for (int j = 0; j < numEts; j++){
                if (linha == etiquetas.get(j).getLinha()){
                    cont1++;
                }
            }
            linhas.put(linha, cont1);
        }

        for (int i = 0; i < numLinhas ; i++){
            if (linhas.get(i + 1) != null) {
                float numProblemas = linhas.get(i + 1);
                float porcentagem = ( numProblemas / numEts ) * 100;
                linhasPorcentagem.put(i, porcentagem);
            } else {
                linhasPorcentagem.put(i, 0f);
            }
        }

        return linhasPorcentagem;
    }
}
