package Hackaton;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.ObjectInputStream;

public class LerEtiqueta {
    public Etiqueta lerEtiqueta(int numEt) throws IOException, ClassNotFoundException {
        Etiqueta et = new Etiqueta();
        FileInputStream fin = null;
            try {
                fin = new FileInputStream("etiqueta" + numEt + ".ser");
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
            ObjectInputStream ois = null;
            try {
                ois = new ObjectInputStream(fin);
            } catch (IOException e) {
                e.printStackTrace();
            }
            assert ois != null;

            et = (Etiqueta) ois.readObject();

            return et;
    }
}
