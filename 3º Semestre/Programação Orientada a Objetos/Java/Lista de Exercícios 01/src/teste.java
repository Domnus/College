import java.util.Scanner;

class teste {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        int[][] matrix = new int[4][4]; //*declarou a matriz
        // preenchimento da matriz
        System.out.println("Digite os valores para completar a matriz: ");
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                matrix[i][j] = console.nextInt();
            }
        }
        for (int l = 0; l < 4; l++) {
            for (int c = 0; c < 4; c++) {
                    System.out.print(matrix[l][c] + " ");
                }
            System.out.println();
        }
    }
}
