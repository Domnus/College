/*
Desenvolva um programa que retire todas as vogais da frase “Bacharelado em Ciência da
Computação” e exiba-a novamente.
 */
public class ex08 {
    public static void main(String[] args) {
        String frase = "Bacharelado em Ciência da Computação";

        frase = frase.replaceAll("[aãeêiou]", "");

        System.out.println(frase);
    }
}
