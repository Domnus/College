package Hackaton;

import java.io.Serializable;

@SuppressWarnings("ALL")
public class Etiqueta implements Serializable {
    private String nomeMaquina;
    private int linha;
    private String prioridade;
    private boolean houveParada;
    private String data;
    private String horario;
    private String descricao;
    private String nomeOperador;

    public void setMaquina(String nomeMaq){
        nomeMaquina = nomeMaq;
    }

    public void setLinha(int l) {
        linha = l;
    }

    public void setPrioridade(String p){
        prioridade = p;
    }

    public void setParada(boolean prd){
        houveParada = prd;
    }

    public void setData(String date){
        data = date;
    }

    public void setHorario(String hora){
        horario = hora;
    }

    public void setDescricao(String desc){
        descricao = desc;
    }

    public void setOperador(String nome){
        nomeOperador = nome;
    }

    public String getNomeMaquina(){
        return nomeMaquina;
    }

    public int getLinha(){
        return linha;
    }

    public String Prioridade(){
        return prioridade;
    }

    public boolean getParada(){
        return houveParada;
    }

    public String getDate(){
        return data;
    }

    public String getHora(){
        return horario;
    }

    public String getDescricao(){
        return descricao;
    }

    public String getOperador(){
        return nomeOperador;
    }
}
