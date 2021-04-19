import java.util.Date;

class Comprador {
    private String nome;
    private String endereco;
    private String telefone;

    public Comprador(String nome, String endereco, String telefone) {
        this.nome = nome;
        this.endereco = endereco;
        this.telefone = telefone;
    }

    public String getNome() {
        return nome;
    }

    public String getEndereco() {
        return endereco;
    }

    public String getTelefone() {
        return telefone;
    }
}

class Produto {
    private String descricao;
    private float preco;
    private int qtde_disp;

    public Produto(String descricao, float preco, int qtde_disp) {
        this.descricao = descricao;
        this.preco = preco;
        this.qtde_disp = qtde_disp;
    }

    public String getDescricao() {
        return descricao;
    }

    public float getPreco() {
        return preco;
    }

    public int getQtde_disp() {
        return qtde_disp;
    }

    public void repor(int qtde){
        this.qtde_disp += qtde;
    }

    public boolean vender(int qtde){
        if (this.qtde_disp < qtde)
                return false;
        else
            this.qtde_disp -= qtde;
            return true;
    }
}

class Venda {
    private Date data;
    private Comprador cliente;
    private Produto produto;
    private int qtde_v;
    private float valorTotal;

    public Venda(Date data) {
        this.data = data;
    }

    public Comprador getCliente() {
        return cliente;
    }

    public Produto getProduto() {
        return produto;
    }

    public float getValorTotal() {
        return valorTotal;
    }

    public void setCliente(Comprador cliente) {
        this.cliente = cliente;
    }

    public boolean venderProduto(Produto produto, int qtde){
        if (produto.vender(qtde)){
            this.produto = produto;
            this.qtde_v += qtde;
            this.valorTotal = qtde * produto.getPreco();

            return true;
        }
        return false;
    }
}

public class ex04 {
    public static void main(String[] args){
        Comprador comprador = new Comprador("Bento", "Av. Brasil", "40028922");
        Produto produto = new Produto("Cubo magico", 25.9f, 100);
        Venda venda = new Venda(new Date());

        venda.setCliente(comprador);

        if (venda.venderProduto(produto, 50)){
            System.out.println("Venda realizada!");
            System.out.println("Valor da venda: " +venda.getValorTotal());
            System.out.println("Cliente: " +venda.getCliente().getNome());
            System.out.println("Produto: " +venda.getProduto().getDescricao());
        } else {
            System.out.println("Ocorreu um problema na venda!");
        }
    }
}
