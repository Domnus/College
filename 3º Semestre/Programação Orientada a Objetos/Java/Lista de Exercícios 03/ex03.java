class Professor{
    private String nome, formacao, titulacao;

    public Professor(String nome, String formacao, String titulacao){
        this.nome = nome;
        this.formacao = formacao;
        this.titulacao = titulacao;
    }

    public String getNome(){
        return this.nome;
    }
}

class Disciplina{
    private int codigo;
    private String nome;
    private int cargaHoraria;
    private Professor prof;

    public Disciplina(int codigo, String nome, int cargaHoraria) {
        this.codigo = codigo;
        this.nome = nome;
        this.cargaHoraria = cargaHoraria;
    }

    public String getNome(){
        return nome;
    }

    public Professor getProfessor(){
        return prof;
    }

    public void setProfessor(Professor p){
        this.prof = p;
    }
}

public class ex03 {
    public static void main(String[] args){
        Disciplina d1 = new Disciplina(1234, "Programação Orientada a Objetos", 80);
        Professor p1, p2;
        p1 = new Professor("Adriano Nakamura", "Ciência da Computação", "Doutor");
        p2 = new Professor("Maurício Duarte", "Ciência da Computação", "Mestre");

        d1.setProfessor(p1);

        System.out.println("A disciplina " +d1.getNome()+ " tem como professor " + d1.getProfessor().getNome());
    }
}
