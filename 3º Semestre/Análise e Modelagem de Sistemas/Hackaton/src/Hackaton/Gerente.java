package Hackaton;

import java.io.*;

public class Gerente {
    public void gerente() throws IOException, ClassNotFoundException {
        Etiqueta et;
        FileInputStream fin = null;
        try {
            fin = new FileInputStream("etiqueta.txt");
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

        System.out.println(et.getDescricao());
    }
}
