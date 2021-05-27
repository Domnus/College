interface MeuHorario {
    int getHora();
    int getMinuto();
    int getSegundo();

    void setHora(int hora);
    void setMinuto(int minuto);
    void setSegundo(int segundo);

    String toString();
}

class Horario implements MeuHorario {
    private int hora, minuto, segundo;

    public int getHora() {
        return hora;
    }

    public int getMinuto() {
        return minuto;
    }

    public int getSegundo() {
        return segundo;
    }

    public void setHora(int hora) {
        this.hora = hora;
    }

    public void setMinuto(int minuto) {
        this.minuto = minuto;
    }

    public void setSegundo(int segundo) {
        this.segundo = segundo;
    }

    public String toString() {
        return this.hora+":" +this.minuto+":"+this.segundo;
    }
}

public class ex01 {
    public static void main(String[] args) {
        Horario h = new Horario();
        h.setHora(21);
        h.setMinuto(18);
        h.setSegundo(47);

        System.out.println("Hora: " +h.toString());
    }
}
