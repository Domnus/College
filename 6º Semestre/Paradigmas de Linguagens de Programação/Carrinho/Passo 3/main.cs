using System;
using System.Collections.Generic;
using System.Linq;

public class Item{  
    public int Id { get; set; }  
	public string Produto { get; set; }    
	public decimal Preco { get; set; }  
		
	public Item(int id, string produto, decimal preco){  
		this.Id = id;  
		this.Produto = produto;  
		this.Preco = preco;  
	}

}

public class Carrinho  
{  
	public List<Item> Itens { get; set; }  
	public Carrinho()  
	{  
		this.Itens = new List<Item>();  
	}  
	public void AdicionarItem(Item item)  
	{  
		Itens.Add(item);  
	}  
	public void RemoverItem(Item item)  
	{  
		Itens.Remove(item);  
	}  

	public static double Soma(int x, int y){
		return x + y;
	}

	public decimal Total()  
	{  
		return Itens.Select(item => item.Preco).Sum();
	}  
}
				
public static class Program
{
	public static void Passo3()
{
		Carrinho carrinho = new Carrinho();
		carrinho.AdicionarItem(new Item(1, "Produto 1", 499));
		carrinho.AdicionarItem(new Item(2, "Produto 2", 179));
		carrinho.AdicionarItem(new Item(3, "Produto 3", 1199));

		double total = (double) carrinho.Total();

		Console.WriteLine("O total do carrinho é: R$" + total);
	}

	public static void Main()
	{
		var watch = new System.Diagnostics.Stopwatch();
		watch.Start();
		Passo3();
		watch.Stop();
		Console.WriteLine("Tempo de execução: " + watch.ElapsedMilliseconds + "ms");
	}
}