public class ex11 {
    static int [][] readArray() {
        int[][] m = new int[3][3];

        for (int i = 0; i < m.length; i++) {
            for(int j = 0; j < m[0].length; j++) {
                m[i][j] = (int) (Math.random() * 10 + 1);
                System.out.print("\t" + m[i][j]);
            }
            System.out.println();
        }
        return m;
    }

    static int sumArray(int[][] m) {
        int soma = 0;
        for (int[] ints : m) {
            for (int j = 0; j < m[0].length; j++) {
                soma += ints[j];
            }
        }
        return soma;
    }

    public static void main(String[] args) {
        System.out.println("Soma da matriz: " + sumArray((readArray())));
    }
}
