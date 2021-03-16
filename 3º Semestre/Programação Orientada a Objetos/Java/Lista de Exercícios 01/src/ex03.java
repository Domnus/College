/* Desenvolva um programa que exiba todos os números divisíveis por 3 e 4 entre 1 a 1000. */

public class ex03 {
    public static void main(String[] args) {
        for (int i = 1; i <=1000; i++) {
            if (i % 3 == 0 && i % 4 == 0){
                System.out.println(i);
            }
        }
    }
}
