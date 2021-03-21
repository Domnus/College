package ex05;

public class Aluno {
    String RA;
    String Nome;
    float  p1;
    float  p2;
    float  media;

    public Aluno(String RA, String Nome) {
        this.RA   = RA;
        this.Nome = Nome;
    }

    void atribuirNotas(float notaP1, float notaP2) {
        p1 = notaP1;
        p2 = notaP2;
    }

    void calcularMedia(){
        media = (p1 + p2) / 2;
    }

    String verificarSituacao() {
        if (media >= 7) {
            return "Aprovado";
        } else if (media < 7 && media >= 4){
            return "Exame";
        } else {
            return "Reprovado";
        }
    }
}
