
import javax.swing.JOptionPane;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author nakamura
 */

class Empregado{
    private int nro;
    private String nome;
    public Empregado(){
        this.nro=Integer.parseInt(JOptionPane.showInputDialog("Nro funcional"));
        this.nome=JOptionPane.showInputDialog("Nome");
    }
    public int getNro(){
        return this.nro;
    }
    public String getNome(){
        return this.nome;
    }
}//Empregado
class Vendedor extends Empregado{
    private float salarioBase, valorVendasMes, percComissao;
    public Vendedor(){
        this.salarioBase=Float.parseFloat(
                JOptionPane.showInputDialog("Salário base"));
        this.valorVendasMes=Float.parseFloat(
                JOptionPane.showInputDialog("Valor de vendas no mês"));
        this.percComissao=Float.parseFloat(
                JOptionPane.showInputDialog("Percentagem de comissão"));
    }
    public float getSalario(){
        return this.salarioBase+this.valorVendasMes*this.percComissao/100;
    }
}//Vendedor
class Gerente extends Empregado{
    private float salarioMensal;
    public Gerente(){
        this.salarioMensal=Float.parseFloat(
                 JOptionPane.showInputDialog("Salário mensal"));
    }
    public float getSalario(){
        return this.salarioMensal;
    }
}//Gerente
class Horista extends Empregado{
    private float valorHora;
    private int totalHorasTrabalhadas;
    public Horista(){
        this.valorHora=Float.parseFloat(
                JOptionPane.showInputDialog("Valor da hora de trabalho"));
        this.totalHorasTrabalhadas=Integer.parseInt(
                JOptionPane.showInputDialog("Total de horas trabalhadas"));
    }
    public float getSalario(){
        return this.valorHora*this.totalHorasTrabalhadas;
    }
}//Horista

public class ex02 {
    public static void main(String args[]){
        Empregado e1=new Vendedor();
        Empregado e2=new Gerente();
        Empregado e3=new Horista();
        float s1, s2, s3;
        s1=((Vendedor) e1).getSalario();
        s2=((Vendedor) e2).getSalario();
        s3=((Vendedor) e3).getSalario();
        System.out.println("Empregado com o maior salário: ");
        if(s1>s2 && s1>s3)
            System.out.println("Nro: "+ e1.getNro()+
                               "\nNome: "+e1.getNome()+
                               "\nSalario: R$ "+s1);
        else if(s2>s3)
            System.out.println("Nro: "+ e2.getNro()+
                               "\nNome: "+e2.getNome()+
                               "\nSalario: R$ "+s2);
        else 
            System.out.println("Nro: "+ e3.getNro()+
                               "\nNome: "+e3.getNome()+
                               "\nSalario: R$ "+s3);

    }
}
