/* Desenvolva um programa que inicialize um vetor de 10 números inteiros com seguintes números
{5, 7, 9, 11, 6, 4, 8, 16, 13, 1} e exiba os números localizados nas posições ímpares (lembre-se que
num vetor de 10 posições os índices são entre 0 e 9).
 */
public class ex05 {
    public static void main(String[] args) {
        int[] a = {5, 7, 9, 11, 6, 4, 8, 16, 13, 1};

        for (int i = 0; i < a.length; i++) {
            if (i % 2 == 1) {
               System.out.println(a[i]);
            }
        }
    }
}
