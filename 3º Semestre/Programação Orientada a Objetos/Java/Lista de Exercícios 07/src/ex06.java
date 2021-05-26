/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author nakamura
 */
class Transporte{
    private boolean ligado;
    private int velocidade;
    public void ligar(){
        this.ligado=true;
    }
    public void desligar(){
        this.ligado=false;
        this.velocidade=0;
    }
    public void setVelocidade(int v){
        this.velocidade=v;
    }
    public boolean getLigado(){
        return this.ligado;
    }
    public int getVelocidade(){
        return this.velocidade;
    }
}//Transporte
class Carro extends Transporte{
    private int quilometragem;
    public int getQuilometragem(){
        return this.quilometragem;
    }
    public void setQuilometragem(int q){
        this.quilometragem=q;
    }
    public void setVelocidade(int v){
        if(v>200)
            super.setVelocidade(200);
        else super.setVelocidade(v);
    }
}//Carro
public class ex06 {
    public static void main(String args[]){
        Carro fusca=new Carro();
        fusca.ligar();
        fusca.setVelocidade(400);
        fusca.setQuilometragem(200);
        if(fusca.getLigado())
            System.out.println("Velocidade: "+fusca.getVelocidade()+
                               "\nKM: "+fusca.getQuilometragem());
    }
}
