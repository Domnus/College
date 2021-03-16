/*Desenvolva um programa que leia preço de custo de um produto qualquer, calcule e exiba o preço
  de venda sabendo que as percentagens de lucro e de impostos são respectivamente 12% e 26,95%.
 */

import java.util.Scanner;

public class ex01 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        float p_custo, p_venda;
        System.out.print("Informe o preço de custo: ");

        p_custo = scan.nextFloat();
        p_venda = p_custo + p_custo*0.12f + p_custo*0.2695f;

        System.out.println("O preço de venda será: R$%" +p_venda);
    }
}
