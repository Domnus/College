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
				if (context.Proprietario.Any()) {
					return;
				}

				context.Proprietario.AddRange(
					new Proprietario
					{
						Nome = "",  
						CPF = "",
						Endereco = "",
						Telefone = "",
						Email = "",
						DtNascimento = DateTime.Parse("")
					}
				);
			}
		}
	}
}