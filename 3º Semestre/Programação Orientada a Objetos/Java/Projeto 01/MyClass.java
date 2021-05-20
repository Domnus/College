import javax.swing.*;

class Empregado {
    private int nro;
    private String nome;

    public Empregado() {
        this.nome = JOptionPane.showInputDialog("Nome do empregado: ");
        this.nro = Integer.parseInt(JOptionPane.showInputDialog("Número do empregado: "));
    }

    public int getNro() {
        return this.nro;
    }

    public String getNome() {
        return this.nome;
    }
}

class Vendedor extends Empregado {
    private float salarioBase;
    private float valorVendasMes;
    private float porcentagemComissao;

    public Vendedor() {
        this.salarioBase = Float.parseFloat(JOptionPane.showInputDialog("Salário base: "));
        this.valorVendasMes = Float.parseFloat(JOptionPane.showInputDialog("Valor de vendas no mês: "));
        this.porcentagemComissao = Float.parseFloat(JOptionPane.showInputDialog("Porcentagem de comissão: "));
    }

    public float getSalario() {
        return this.salarioBase + this.valorVendasMes * this.porcentagemComissao / 100;
    }
}

class Gerente extends Empregado {
    private float salarioMensal;

    public Gerente() {
        this.salarioMensal = Float.parseFloat(JOptionPane.showInputDialog("Salário mensal: "));
    }

    public float getSalario() {
        return this.salarioMensal;
    }
}

class Horista extends Empregado {
    private float valorHora;
    private int totalHorasTrabalhadas;

    public Horista() {
        this.valorHora = Float.parseFloat(JOptionPane.showInputDialog("Valor da hora: "));
        this.totalHorasTrabalhadas = Integer.parseInt(JOptionPane.showInputDialog("Horas trabalhadas: "));
    }

    public float getSalario() {
        return this.valorHora * totalHorasTrabalhadas;
    }
}

public class MyClass {
    public static void main(String[] args) {
        Vendedor e1 = new Vendedor();
        Gerente e2  = new Gerente();
        Horista e3  = new Horista();

        float s1, s2, s3;
        s1 = e1.getSalario();
        s2 = e2.getSalario();
        s3 = e3.getSalario();

        System.out.println("Empregado com o maior salário: ");

        if (s1 > s2 && s1 > s3)
            System.out.println("Número: " +e1.getNro()+ "\nNome : " +e1.getNome()+ "\nSalário: " +e1.getSalario());
        else if (s2 > s3)
            System.out.println("Número: " +e2.getNro()+ "\nNome : " +e2.getNome()+ "\nSalário: " +e2.getSalario());
        else
            System.out.println("Número: " +e3.getNro()+ "\nNome : " +e3.getNome()+ "\nSalário: " +e3.getSalario());
    }
}