using System.ComponentModel.DataAnnotations;
using System;

namespace PetShopApp.Models
{
	public class Produto 
	{
        public int Id {get; set;}

        public string Nome {get; set;}

        public string Descricao {get; set;}

        public int QuantidadeEstoque {get; set;}

        [Display(Name = "Preço de Compra")]
        public float PrecoCompra {get; set;}

        [Display(Name = "Preço de Venda")]
        public float PrecoVenda {get; set;}

	}
}