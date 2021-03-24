package Hackaton;

import java.io.Serializable;
import java.time.LocalDate;
import java.time.LocalTime;

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

    public void writeMaquina(String nomeMaq){
        nomeMaquina = nomeMaquina;
    }

    public void writeLinha(int l) {
        linha = l;
    }

    public void writePrioridade(String p){
        prioridade = prioridade;
    }

    public void writeParada(boolean prd){
        houveParada = prd;
    }

    public void writeData(String date){
        data = date;
    }

    public void writeHorario(String hora){
        horario = hora;
    }

    public void writeDescricao(String desc){
        descricao = desc;
    }

    public void writeOperador(String nome){
        nomeOperador = nome;
    }

    public String getDescricao(){
        return descricao;
    }
}
