import java.util.Scanner;

public class MyClass {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String nome;
        int idade;
        System.out.println("Informe o seu nome: ");
        nome = scan.next();

        System.out.println("Informe a sua idade: ");
        idade = scan.nextInt();

        System.out.println("Olá, " +nome+ " daqui a um ano você terá " +(idade + 1)+ " anos");
    }
}
