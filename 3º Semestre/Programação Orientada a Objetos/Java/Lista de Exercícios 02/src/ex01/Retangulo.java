package ex01;

class Retangulo {
    int base;
    int altura;

    public Retangulo(int a, int b) {
        altura = a;
        base = b;
    }

    public int calculaArea() {
        return altura * base;
    }

    public int calculaPerimetro() {
        return (altura * 2) + (base * 2);
    }
}
