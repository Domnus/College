package Hackaton;

import java.util.ArrayList;

public class MediaProblemas {
    public float media(ArrayList<Etiqueta> etiquetas, int numEts){
        ArrayList<String> numDias = new ArrayList<>();
        String[] dias = new String[numEts];

        for (int i = 0; i < numEts; i++){
            String dia = etiquetas.get(i).getDate();
            dias[i] = dia;
        }

        for (String dia : dias){
            if (!numDias.contains(dia)){
                numDias.add(dia);
            }
        }

        return (float)numEts / numDias.size();

    }
}
