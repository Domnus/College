/* Desenvolva um programa que conte quantas vogais fazem parte da frase “Bacharelado em Ciência
da Computação” e exiba este valor.
 */

import java.lang.*;

public class ex07 {
    public static void main(String[] args ) {
        String frase = "Bacharelado em Ciência da Computação";
        String novaFrase;
        novaFrase = frase.replaceAll("[^aãeêiou]", "");
        int cont = novaFrase.length();

        System.out.println(cont);
        System.out.println(novaFrase);
    }
}
