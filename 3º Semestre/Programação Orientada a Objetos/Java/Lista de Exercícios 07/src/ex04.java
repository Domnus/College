
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
class Pessoa{
    private String nome, sobrenome;
    public Pessoa(){
        nome=JOptionPane.showInputDialog("Primeiro nome");
        sobrenome=JOptionPane.showInputDialog("Sobrenome");
    }
    public Pessoa(String nome, String sobrenome){
        this.nome=nome;
        this.sobrenome=sobrenome;
    }
    public String getNome(){
        return this.nome;
    }
    public String getSobrenome(){
        return this.sobrenome;
    }
    public String getNomeCompleto(){
        return this.nome+" "+this.sobrenome;
    }
}//Pessoa
class Funcionario extends Pessoa{
    private int nroMatricula;
    private float salario;
    public Funcionario(String nome, String sobrenome, int nro, 
            float salario){
        //super();
        super(nome, sobrenome);        
        this.nroMatricula=nro;
        this.salario=salario;
    }
    public void setSalario(float s){
        this.salario=s;
    }
    public int getNroMatricula(){
        return this.nroMatricula;
    } 
    public float getPrimeiraParcelaSalario(){
        return this.salario*0.6f;
    }
    public float getSegundaParcelaSalario(){
        return this.salario*0.4f;
    }
}//Funcionario
class Professor extends Funcionario{
    private String formacao;
    public Professor(String nome, String sobrenome, int nro, 
            float salario, String formacao){
        super(nome, sobrenome, nro, salario);
        this.formacao=formacao;
    }
    public String getFormacao(){
        return this.formacao;
    }
    public float getPrimeiraParcelaSalario(){
        return super.getPrimeiraParcelaSalario()+super.getSegundaParcelaSalario();
    }
    public float getSegundaParcelaSalario(){
        return 0;
    }    
}//Funcionario
public class ex04 {
    public static void main(String args[]){
        Funcionario f=new Funcionario("João", "da Silva", 1, 3000);
        Professor p=new Professor("José", "da Silva", 2, 2000, "Engenharia");
        System.out.println("Nome: "+f.getNomeCompleto()
                + "\nSalário (1ª parcela): R$ "+f.getPrimeiraParcelaSalario()
                + "\nSalário (2ª parcela): R$ "+f.getSegundaParcelaSalario());
        System.out.println("Nome: "+p.getNomeCompleto()
                + "\nSalário (1ª parcela): R$ "+p.getPrimeiraParcelaSalario()
                + "\nSalário (2ª parcela): R$ "+p.getSegundaParcelaSalario());
    }
}
