class Departamento{
    private int codigo;
    private String nome;
    private String sigla;

    public Departamento(int codigo, String nome, String sigla){
        this.codigo = codigo;
        this.nome = nome;
        this.sigla = sigla;
    }

    public int getCodigo() {
        return codigo;
    }

    public String getNome() {
        return nome;
    }

    public String getSigla() {
        return sigla;
    }
}

class Funcionario{
    private int codigo;
    private String nome;
    private float salario;
    private Departamento depto;

    public Funcionario(int codigo, String nome, float salario) {
        this.codigo = codigo;
        this.nome = nome;
        this.salario = salario;
    }

    public int getCodigo() {
        return codigo;
    }

    public String getNome() {
        return nome;
    }

    public float getSalario() {
        return salario;
    }

    public Departamento getDepto() {
        return depto;
    }

    public void setSalario(float salario) {
        this.salario = salario;
    }

    public void setDepto(Departamento depto) {
        this.depto = depto;
    }
}

public class ex02 {
    public static void main(String[] args){
        Departamento d1, d2;
        d1 = new Departamento(0001, "Recebimento", "RE");
        d2 = new Departamento(0002, "Estoque", "ES");

        Funcionario f1, f2;
        f1 = new Funcionario(0001, "Bento Carlos", 850f);
        f1.setDepto(d1);
        f2 = new Funcionario(0002, "Kennedy Daniel", 1500f);
        f2.setDepto(d2);

        if (f1.getSalario() > f2.getSalario()){
            System.out.println("Nome do funcionário: " +f1.getNome()+ "\nDepartamento: " +f1.getDepto().getNome());
        } else {
            System.out.println("Nome do funcionário: " +f2.getNome()+ "\nDepartamento: " +f2.getDepto().getNome());
        }
    }
}
