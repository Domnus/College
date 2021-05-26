/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author nakamura
 */
class Equipamento{
    private boolean ligado;
    public void ligar(){
        this.ligado=true;
    }
    public void desligar(){
        this.ligado=false;
    }
    public boolean getLigado(){
        return this.ligado;
    }
}//Equipamento
class EquipamentoSonoro extends Equipamento{
    private int volume;
    private boolean stereo;
    public int getVolume(){
        return this.volume;
    }
    public boolean getStereo(){
        return this.stereo;
    }
    public void setVolume(int v){
        this.volume=v;
    }
    public void setMono(){
        this.stereo=false;
    }
    public void setStereo(){
        this.stereo=true;
    }
    public void ligar(){
        super.ligar();
        this.volume=5;
    }
}//EquipamentoSonoro
public class ex05 {
    public static void main(String args[]){
        EquipamentoSonoro radio=new EquipamentoSonoro();
        radio.ligar();
        radio.setStereo();
        radio.setVolume(8);
        radio.desligar();
        if(radio.getLigado()){
            System.out.println("Volume: "+radio.getVolume());
            if(radio.getStereo())
                System.out.println("Modo Stereo");
            else System.out.println("Modo Mono");
        }else System.out.println("Equipamento desligado");
        radio.ligar();
        radio.setVolume(8);
        if(radio.getLigado()){
            System.out.println("Volume: "+radio.getVolume());
            if(radio.getStereo())
                System.out.println("Modo Stereo");
            else System.out.println("Modo Mono");
        }else System.out.println("Equipamento desligado");

    }
}
