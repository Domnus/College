using Microsoft.EntityFrameworkCore;

namespace ClickJogos.Models
{
	public class Jogo
	{
		public long? id {get; set;}
		public string? Titulo {get; set;}
		public string? Genero {get; set;}
		public string? Distribuidora {get; set;}
		public string? Capa {get; set;}
		public string? Descricao {get; set;}
		public string? Plataforma {get; set;}
		public DateTime? DataLancamento {get; set;}
	}

}