package Hackaton;

import java.util.ArrayList;

public class NumProblemas {
    public ArrayList<String> numProblemas(int numEts, ArrayList<Etiqueta> etiquetas) {
        ArrayList<String> maquinas = new ArrayList<>();
        ArrayList<String> problemas = new ArrayList<>();
        String m = "";
        int cont1, cont2 = 0;

        for (int i = 0; i < numEts; i++){
            maquinas.add(etiquetas.get(i).getNomeMaquina());
        }

        for (int i = 0; i < numEts; i++){
            cont1 = 0;
            String maquina = maquinas.get(i);
            for (int j = 0; j < numEts; j++){
                if (maquina.equals(etiquetas.get(j).getNomeMaquina())){
                    cont1++;
                }
                if (cont1 > cont2){
                    m = etiquetas.get(j) .getNomeMaquina();
                    cont2 = cont1;
                }
            }
        }

        problemas.add(m);
        problemas.add(String.valueOf(cont2));

        return problemas;
    }
}
