public class Customer{
    String nome;
    int pontos;
    
    Customer(String nome, int pontos){
        this.nome = nome;
        this.pontos = pontos;
    }
    
    public String getNome(){ return this.nome;}
    
    public int getPonto(){ return this.pontos;}
}
