import javax.swing.JOptionPane;

class Conta{
    private int nro;
    private String nomeTitular;
    private float saldo;
    public Conta(int nro, String nome, float saldo){
        this.nro=nro;
        this.nomeTitular=nome;
        this.saldo=saldo;
    }
    public Conta(){
        this.nro=Integer.parseInt(JOptionPane.showInputDialog("Nro da conta"));
        this.nomeTitular=JOptionPane.showInputDialog("Nome do titular");
        this.saldo=Float.parseFloat(JOptionPane.showInputDialog("Saldo inicial"));
    }
    public void depositar(float valor){
        this.saldo+=valor;
    }
    public boolean sacar(float valor){
        if(valor > this.saldo) return false;
        this.saldo-=valor;
        return true;
    }
    public float getSaldo(){//retornaSaldo
        return this.saldo;
    }
    public String getNomeTitular(){
        return this.nomeTitular;
    }
}//Conta

public class ex01 {
    public static void main(String []args){
        Conta cliente=new Conta(123, "João da Silva", 300);
        String opcao="0";
        do{
            opcao=JOptionPane.showInputDialog("Conta Corrente\n"+
                    "1 - Depósito\n"+
                    "2 - Saque\n"+
                    "3 - Consulta saldo\n"+
                    "4 - Finalizar");
            switch(opcao){
                case "1": float valor;
                    valor=Float.parseFloat(JOptionPane.showInputDialog("Valor do depósito"));
                    cliente.depositar(valor);
                    break;
                case "2": valor=Float.parseFloat(
                        JOptionPane.showInputDialog("Valor do saque"));
                    if(cliente.sacar(valor))
                        JOptionPane.showMessageDialog(null, "Saque efetuado!");
                    else
                        JOptionPane.showMessageDialog(null, "saldo insuficiente!");
                    break;
                case "3": JOptionPane.showMessageDialog(null,
                        "Nome do titular: "+cliente.getNomeTitular()+
                                "\nSaldo atual: R$ "+cliente.getSaldo());
//break;
                case "4": break;
                default: JOptionPane.showMessageDialog(null, "Opção inválida!");
            }//
        }while(!opcao.equals("4"));
    }//main
}
