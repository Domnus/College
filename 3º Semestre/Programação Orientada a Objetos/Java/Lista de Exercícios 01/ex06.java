/* Desenvolva um programa que leia através do teclado uma matriz 4x4 de valores inteiros e exiba a
soma dos elementos da diagonal principal.
 */
import java.util.Scanner;

public class ex06 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int i = 4, j = 4, soma = 0;
        int[][] array = new int[i][j];

        System.out.println("Digite os valores da matriz: ");

        for(int x = 0; x < i; x++)
            for(int y = 0; y < j; y++) {
                //System.out.print("-> ");
                array[x][y] = (int) (Math.random()*10);
            }

        System.out.println("Matriz: ");

        for (int[] row : array) {
            for (int item : row) {
                System.out.print("\t" + item);
            }
            System.out.println();
        }

        System.out.println("Diagonal principal da matriz: ");

        for (int x = 0; x < i; x++){
            for (int y = 0; y < j; y++){
                if (x == y){
                    System.out.print("\t" + array[x][y]);
                    soma += array[x][y];
                }
                else {
                    System.out.print("\t ");
                }
            }
            System.out.println();
        }
        System.out.println("Soma da diagonal principal: " + soma);
    }
}