/* Desenvolva um programa que leia através do teclado o sexo (“m” ou “f”) e a altura, calcule e exiba
o seu peso ideal em função (atribuídos às respectivas variáveis), de acordo com as fórmulas:
    • P/ homem – peso ideal = 72.7*.altura – 58
    • P/ mulher – peso ideal = 62.1*altura – 44.7
*/

import java.util.Scanner;

public class ex02 {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        String sexo;
        float altura, peso_ideal;
        System.out.print("Informe o seu sexo: [m/f] ");
        sexo = scan.next();

        System.out.print("Informe a sua altura: ");
        altura = scan.nextFloat();

        if (sexo.equals("m")){
            peso_ideal = 72.7f * altura - 58;
        }
        else{
            peso_ideal = 62.1f * altura - 44.7f;
        }

        System.out.println("Seu peso ideal é " + peso_ideal);
    }
}
