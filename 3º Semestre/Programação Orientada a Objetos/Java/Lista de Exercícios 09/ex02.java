class Pessoa{
    protected String nome;
    protected int idade;

    public Pessoa (String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }

    public String getNome() {
        return this.nome;
    }

    public int getIdade() {
        return this.idade;
    }
}

abstract class PessoaIMC extends Pessoa{
    protected float peso;
    protected float altura;

    public PessoaIMC (String nome, int idade, float peso, float altura) {
        super(nome, idade);
        this.peso = peso;
        this.altura = altura;
    }

    public float getPeso() {
        return this.peso;
    }
    
    public float getAltura() {
        return this.altura;
    }

    public void setPeso(float peso) {
        this.peso = peso;
    }

    public void setAltura(float altura) {
        this.altura = altura;
    }

    public float calculaIMC(float altura, float peso) {
        return peso / (altura * altura);
    }

    public abstract String resultadoIMC();
}

class Homem extends PessoaIMC {
    protected String time;

    public Homem (String time, String nome, int idade, float peso, float altura) {
        super(nome, idade, peso, altura);

        this.time = time;
    }

    public void setTime(String time) {
        this.time = time;
    }

    public String getTime() {
        return time;
    }

    public String resultadoIMC () {
        float IMC = calculaIMC(this.altura, this.peso);
        if (IMC > 26.4) {
            return "Acima do peso ideal";
        } else if (IMC < 20.7) {
            return "Abaixo do peso ideal";
        } else {
            return "Peso ideal";
        }
    }
}

class Mulher extends PessoaIMC {
    protected String signo;

    public Mulher (String signo, String nome, int idade, float peso, float altura) {
        super(nome, idade, peso, altura);

        this.signo = signo;
    }

    public void setSigno(String signo) {
        this.signo = signo;
    }

    public String getSigno() {
        return this.signo;
    }

    public String resultadoIMC () {
        float IMC = calculaIMC(this.altura, this.peso);
        if (IMC > 25.8) {
            return "Acima do peso ideal";
        } else if (IMC < 19) {
            return "Abaixo do peso ideal";
        } else {
            return "Peso ideal";
        }
    }
}

public class ex02 {
    public static void main(String[] args) {
        Homem homem = new Homem("Vasco", "Fernando", 20, 75f, 1.80f);
        Mulher mulher = new Mulher("Aquário", "Milena", 20, 50f, 1.90f);

        System.out.println("Nome: " + homem.getNome());
        System.out.println("Idade: " + homem.getIdade());
        System.out.println("Peso: " +homem.getPeso()+ " kg");
        System.out.println("Altura: " +homem.getAltura()+ " m");
        System.out.println("Time: " +homem.getTime());
        System.out.println("Resultado IMC: " +homem.resultadoIMC());

        System.out.println();

        System.out.println("Nome: " + mulher.getNome());
        System.out.println("Idade: " + mulher.getIdade());
        System.out.println("Peso: " +mulher.getPeso()+ " kg");
        System.out.println("Altura: " +mulher.getAltura()+ " m");
        System.out.println("Time: " +mulher.getSigno());
        System.out.println("Resultado IMC: " +mulher.resultadoIMC());

        System.out.println();

        System.out.println("Pessoa mais pesada: " + (homem.getPeso() > mulher.getPeso() ? homem.getNome() : mulher.getNome()));
        System.out.println("Pessoa mais alta: " + (homem.getAltura() > mulher.getAltura() ? homem.getNome() : mulher.getNome()));
    }
}