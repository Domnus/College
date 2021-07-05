package gui;


import java.util.ArrayList;
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
class Contato{
    private String nome, fone, dt_aniversario;

    public Contato(String nome, String fone, String dt_aniversario) {
        this.nome = nome;
        this.fone = fone;
        this.dt_aniversario = dt_aniversario;
    }
    public String getNome() {
        return nome;
    }
    public String getFone() {
        return fone;
    }
    public String getDt_aniversario() {
        return dt_aniversario;
    }
    public void setFone(String fone) {
        this.fone = fone;
    }
}//Contato

class Agenda{
    private ArrayList<Contato> listaContatos;
    public Agenda(){
        this.listaContatos=new ArrayList<Contato>();
    }
    public void incluiContato(String nome, String fone, String dt){
        this.listaContatos.add(new Contato(nome, fone, dt));
    }
    public void incluiContato(Contato c){
        this.listaContatos.add(c);
    }
    public boolean atualizaContato(String nome, String novoFone){
        for(int i=0; i<this.listaContatos.size(); i++){
           Contato c=this.listaContatos.get(i); 
           if(c.getNome().equals(nome)){
               c.setFone(novoFone);
               return true;
           }
        }
            /*
            for(Contato c: this.listaContatos)
            if(c.getNome().equals(nome)){
               c.setFone(novoFone);
               return true;
            }*/
        return false;
    }
    public boolean excluiContato(String nome){
        /*for(int i=0; i<this.listaContatos.size(); i++){
           Contato c=this.listaContatos.get(i); 
           if(c.getNome().equals(nome))
               this.listaContatos.remove(c);
               return true;
        }
        */


        for(Contato c: this.listaContatos)
            if(c.getNome().equals(nome)){
                this.listaContatos.remove(c);
                return true;
            }
        return false;
    }
    public Contato consultaContato(String nome){
        for(Contato c: this.listaContatos)
            if(c.getNome().equals(nome))
                return c;
        return null;
    }
}//Agenda
public class agenda {
    public static void main(String args[]){
        Agenda agenda=new Agenda();
        String menu[]={"Cadastrar", "Atualizar", "Excluir","Consultar","Finalizar"};
        String opcao;
        do{
            opcao=JOptionPane.showInputDialog(null, "Escolha uma opcao", 
                                                "Agenda", 
                                                JOptionPane.QUESTION_MESSAGE, null, 
                                                menu, menu[0]).toString();
            switch(opcao){
                case "Cadastrar": cadastrar(agenda); break;     
                case "Atualizar": atualizar(agenda); break;
                case "Excluir": excluir(agenda); break;
                case "Consultar": consultar(agenda); break;
                case "Finalizar": break;
            }//switch
        }while(!opcao.equals(menu[4]));
    }
    
    private static void cadastrar(Agenda agenda){
        String nome, fone, dt_aniv;
        nome=JOptionPane.showInputDialog("Nome do contato");
        fone=JOptionPane.showInputDialog("Telefone do contato");
        dt_aniv=JOptionPane.showInputDialog("dia/mes do aniversario");
        agenda.incluiContato(nome, fone, dt_aniv);
    }//cadastrar
    
    private static void atualizar(Agenda agenda){
        String nome, fone;
        nome=JOptionPane.showInputDialog("Nome do contato para atualizar");
        fone=JOptionPane.showInputDialog("Novo telefone");
        if(agenda.atualizaContato(nome, fone))
            JOptionPane.showMessageDialog(null, "Contato atualizado!");
        else JOptionPane.showMessageDialog(null, "Contato inexistente!");
    }
    
    private static void excluir(Agenda agenda){
        String nome;
        nome=JOptionPane.showInputDialog("Nome do contato para excluir");
        if(agenda.excluiContato(nome))
            JOptionPane.showMessageDialog(null, "Contato excluído!");
        else JOptionPane.showMessageDialog(null, "Contato inexistente!");
    }
    
    private static void consultar(Agenda agenda){
        String nome;
        nome=JOptionPane.showInputDialog("Nome do contato para consultar");
        Contato c=agenda.consultaContato(nome);
        if(c!=null)
            JOptionPane.showMessageDialog(null, "Nome: "+c.getNome()+
                                    "\nFone: "+c.getFone()+
                                    "\nAniversario: "+c.getDt_aniversario());
        else JOptionPane.showMessageDialog(null, "Contato inexistente!");
    }
}
