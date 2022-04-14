using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.DependencyInjection;
using System;
using System.Linq;

namespace PetShopApp.Models
{
	public static class SeedData
	{
		public static void Inicializar(IServiceProvider serviceProvider)
		{
			using(var context = new PetShopAppContext(
				serviceProvider.GetRequiredService<
				DbContextOptions<PetShopAppContext>>()))
			{
				// verificar se há dados no banco
				if (context.Proprietario.Any()) 
				{

				} 
				else 
				{
					context.Proprietario.AddRange(
						new Proprietario
						{
							Nome = "Frederico Hanai",  
							CPF = "47406812850",
							Endereco = "Rua dos bobo",
							Telefone = "14 999040460",
							Email = "frerderico.hanai@univem,edu",
							DtNascimento = DateTime.Parse("08/01/1998")
						},
						new Proprietario
						{
							Nome = "Bento do deidecosta",  
							CPF = "2424242424",
							Endereco = "Av.Brasil",
							Telefone = "14 999043212",
							Email = "bentocarlos@univem.edu",
							DtNascimento = DateTime.Parse("11/02/2003")
						},
						new Proprietario
						{
							Nome = "Hugo gado",  
							CPF = "4077892123",
							Endereco = "Av.dos Gado",
							Telefone = "14 999323212",
							Email = "hugoseiti@univem.edu",
							DtNascimento = DateTime.Parse("03/02/2003")
						},
						new Proprietario
						{
							Nome = "Andressa dos Reis",  
							CPF = "33023812773",
							Endereco = "Av.XV de Novembro",
							Telefone = "14 998633242",
							Email = "andressareis@univem.edu",
							DtNascimento = DateTime.Parse("08/15/2000")
						}
					);
				}

				if (context.Produto.Any()) 
				{

				} 
				else 
				{
					context.Produto.AddRange(
						new Produto
						{
							Nome = "Shampoo",
							Descricao = "Shampoo",
							QuantidadeEstoque = 3,
							PrecoCompra = 3.99f, 
							PrecoVenda = 5.99f
						},
						new Produto
						{
							Nome = "Ração Dogshow",
							Descricao = "Ração",
							QuantidadeEstoque = 6,
							PrecoCompra = 7.99f, 
							PrecoVenda = 14.99f
						},
						new Produto
						{
							Nome = "Coleira Anti-pulgas",
							Descricao = "Coleira",
							QuantidadeEstoque = 9,
							PrecoCompra = 5.99f, 
							PrecoVenda = 8.99f
						}
					);
				}
				context.SaveChanges();
			}
		}
	}
}