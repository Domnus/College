import java.util.Date;

interface Radio {
    int getBanda();
    void setBanda(int banda);

    float getSintonia();
    void setSintonia(float frequencia);

    int getVolumeRadio();
    void setVolumeRadio(int vol);

    void ligaRadio();
    void desligaRadio();
}

interface Relogio {
    String getHorario();
    String getAlarme();

    void setAlarme(int hora, int min);
    void ligaAlarme();

    void desligaAlarme();
    int getStatusAlarme();

    int getVolumeAlarme();
    void setVolumeAlarme(int vol);
}

class RadioRelogio implements Radio, Relogio {
    private int banda;
    private int volumeRadio;
    private int volumeAlarme;
    private float frequencia;
    private int horaAlarme;
    private int minutoAlarme;
    private boolean alarmeLigado;
    private boolean radioLigado;

    RadioRelogio (int banda, int volRadio, int volAlarme, float frequencia) {
        this.banda = banda;
        this.volumeRadio = volRadio;
        this.volumeAlarme = volAlarme;
        this.frequencia = frequencia;
        this.alarmeLigado = false;
        this.radioLigado = false;
    }

    public void ligaRadio() {
        this.radioLigado = true;
    }

    public void desligaRadio() {
        this.radioLigado = false;
    }

    public void ligaAlarme() {
        this.alarmeLigado = true;
    }

    public void desligaAlarme() {
        this.alarmeLigado = false;
    }


    public String getHorario() {
        Date hoje = new Date();
        if (hoje.getMinutes() > 9) {
            return hoje.getHours()+":"+hoje.getMinutes();
        } 
        else {
            return hoje.getHours()+":0"+hoje.getMinutes();
        }
    }

    public String getAlarme() {
        if (this.minutoAlarme > 9)
            return ""+this.horaAlarme+ ':' +this.minutoAlarme;
        else 
            return ""+this.horaAlarme+ ":0" +this.minutoAlarme;
    }

    public int getBanda() {
        return this.banda;
    }

    public float getSintonia() {
        return this.frequencia;
    }

    public int getVolumeRadio() {
        return this.volumeRadio;
    }

    public int getVolumeAlarme() {
        return this.volumeAlarme;
    }

    public int getStatusAlarme() {
        if (this.alarmeLigado)
            return 1;
        else 
            return 0;
    }

    public void setVolumeRadio(int vol) {
        this.volumeRadio = vol;
    }

    public void setVolumeAlarme(int vol) {
        this.volumeAlarme = vol;
    }

    public void setSintonia(float frequencia) {
        this.frequencia = frequencia;
    }

    public void setAlarme(int hora, int min) {
        this.horaAlarme   = hora;
        this.minutoAlarme = min;
    }

    public void setBanda(int banda) {
        this.banda = banda;
    }
}

public class ex01 {
    public static void main(String[] args) {
        RadioRelogio radioRelogio = new RadioRelogio(0, 0, 0, 0f);
        radioRelogio.ligaRadio();
        radioRelogio.setVolumeRadio(50);
        radioRelogio.setSintonia(55.5f);
        radioRelogio.setAlarme(10, 30);
        radioRelogio.ligaAlarme();
        radioRelogio.setVolumeAlarme(80);
        
        System.out.print("Banda: "); 
        System.out.println(radioRelogio.getBanda() > 1 ? "AM" : "FM"); 
        System.out.println("Frequência: " +radioRelogio.getSintonia());
        System.out.println("Volume rádio: " +radioRelogio.getVolumeRadio());
        System.out.println("Hora: " +radioRelogio.getHorario());
        System.out.print("Status alarme: " );
        System.out.println(radioRelogio.getStatusAlarme() > 1 ? "Desligado" : "Ligado" ); 
        System.out.println("Hora alarme: " +radioRelogio.getAlarme());
        System.out.println("Volume alarme: " +radioRelogio.getVolumeAlarme());
    }
}
