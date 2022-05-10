using System.ComponentModel.DataAnnotations.Schema;
using System.ComponentModel.DataAnnotations;
using System;

namespace PetShopApp.Models
{
	public class Produto 
	{
        public int Id {get; set;}

        public string? Nome {get; set;}

        [Display(Name = "Descrição")]
        public string? Descricao {get; set;}

        [Display(Name = "Quantidade Estoque")]
        public int? QuantidadeEstoque {get; set;}

        [Display(Name = "Preço de Compra")]
        [DataType(DataType.Currency)]
        [Column(TypeName = "decimal(18,2)")]
        public float? PrecoCompra {get; set;}

        [Display(Name = "Preço de Venda")]
        [DataType(DataType.Currency)]
        [Column(TypeName = "decimal(18,2)")]
        public float? PrecoVenda {get; set;}

	}
}