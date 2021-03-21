package ex01;

public class Principal {
    public static void main(String[] args) {
        Retangulo ret = new Retangulo(3,5);

        int area = ret.calculaArea();
        int perimetro = ret.calculaPerimetro();

        System.out.println("A base do retângulo é: " + ret.base);
        System.out.println("A altura do retângulo é: " + ret.altura);
        System.out.println("A área do retângulo é: " + area);
        System.out.println("O perímetro do retângulo é: " + perimetro);
    }
}
