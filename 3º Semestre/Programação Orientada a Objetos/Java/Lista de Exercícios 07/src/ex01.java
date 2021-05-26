
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

class Animal{
    private String tipo, cor;
    public Animal(){
        this.tipo=JOptionPane.showInputDialog("Tipo do animal");
        this.cor=JOptionPane.showInputDialog("Cor do animal");
    }
    public void exibirTipoCor(){
        System.out.println("Eu sou "+this.tipo+" de cor "+this.cor);
    }
}//Animal

class Cachorro extends Animal{
    private String nome, raca;
    public Cachorro(){
        super();
        this.nome=JOptionPane.showInputDialog("Nome ");
        this.raca=JOptionPane.showInputDialog("Raça ");
    }
    public void exibirNomeRaca(){
        System.out.println(this.nome+ " é da raça "+this.raca);
    }
}//Cachorro
public class ex01 {
    public static void main(String args[]){
        Cachorro toto=new Cachorro();
        toto.exibirTipoCor();
        toto.exibirNomeRaca();
    }
}
