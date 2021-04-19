class Veiculo{
    private String placa;
    private String marca;
    private String modelo;
    private String cor;

    public Veiculo(String placa, String marca, String modelo, String cor) {
        this.placa = placa;
        this.marca = marca;
        this.modelo = modelo;
        this.cor = cor;
    }

    public String getPlaca(){
        return this.placa;
    }

    public String getMarca(){
        return this.marca;
    }

    public String getModelo() {
        return modelo;
    }

    public String getCor() {
        return cor;
    }
}

class Motorista{
    private String cnh;
    private String categoria;
    private String nome;
    private Veiculo carro;

    public Motorista(String cnh, String categoria, String nome) {
        this.cnh = cnh;
        this.categoria = categoria;
        this.nome = nome;
    }

    public String getCnh() {
        return cnh;
    }

    public String getCategoria() {
        return categoria;
    }

    public String getNome() {
        return nome;
    }

    public Veiculo getCarro() {
        return carro;
    }

    public void setCarro(Veiculo carro) {
        this.carro = carro;
    }
}

public class ex01 {
    public static void main(String[] args){
        Veiculo v1, v2;
        v1 = new Veiculo("FXR9915", "Volksvagen", "Fusca", "Vermelho");
        v2 = new Veiculo("BRA4486", "Ford", "Ka", "Branco");

        Motorista m1 = new Motorista("000123456789", "A", "Bento Carlos");
        m1.setCarro(v1);

        System.out.println("Motorista: " +m1.getNome()+ "\nNRO da CNH: " +m1.getCnh()+ "\nModelo do carro: " +m1.getCarro().getModelo()+ "\nNRO da placa: " +m1.getCarro().getPlaca());
    }
}
