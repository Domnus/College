import java.util.Scanner;

class Fabricante{
    private String nome, endereco, telefone;

    public Fabricante(String nome, String endereco, String telefone) {
        this.nome = nome;
        this.endereco = endereco;
        this.telefone = telefone;
    }
    public String getTelefone() {
        return telefone;
    }
    public void setTelefone(String telefone) {
        this.telefone = telefone;
    }
}//Fabricante

class Produto{
    private String descricao;
    private float preco;
    private int qtdeDisp=0, qtdeVend=0;
    private Fabricante fabrica;
    public Produto(String descricao, float preco){
        this.descricao=descricao;
        this.preco=preco;
    }
    public Fabricante getFabrica() {
        return fabrica;
    }
    public void setFabrica(Fabricante fabrica) {
        this.fabrica = fabrica;
    }
    public void repor(int qtde){
        this.qtdeDisp+=qtde;
    }
    public boolean vender(int qtde){
        if(qtde>this.qtdeDisp) return false;
        this.qtdeDisp-=qtde;
        this.qtdeVend+=qtde;
        return true;
    }
    public void exibirDados(){
        System.out.println("Descrição: "+this.descricao+
                "\nPreço: R$ "+this.preco+
                "\nQtde disponível: "+this.qtdeDisp+
                "\nQtde vendida: "+this.qtdeVend);
    }
}//Produto

public class ex02 {
    public static void main(String args[]){
        Scanner teclado=new Scanner(System.in);
        Produto p=new Produto("Pendrive 64Gb", 50.80f);
        Fabricante f=new Fabricante("Kingston", "endereco do fabricante","111111111111");
        p.setFabrica(f);
        System.out.println("Telefone do fabricante: "+p.getFabrica().getTelefone());
        p.getFabrica().setTelefone("222222222222");
        System.out.println("Telefone do fabricante: "+p.getFabrica().getTelefone());
        /* System.out.print("Quantidade a ser reposta: ");
        int q=teclado.nextInt();
        p.repor(q);
        p.exibirDados();
        System.out.println("Quantidade a ser vendida: ");
        q=teclado.nextInt();
        if(p.vender(q))
        System.out.println("Venda realizada!");
        else System.out.println("Quantidade insuficiente!");
        p.exibirDados();
        */
    }
}