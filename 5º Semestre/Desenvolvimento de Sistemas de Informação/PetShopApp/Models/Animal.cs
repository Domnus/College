
using System.ComponentModel.DataAnnotations;
using System;

namespace PetShopApp.Models
{
	public class Animal 
	{
        public int Id {get; set;}

        public string? Nome {get; set;}

        [Display(Name = "Data de Nascimento")]
        [DataType(DataType.Date)]
        public DateTime DtNascimento {get; set;}

        [Display(Name = "Raça")]
        public string? Raca {get; set;}

        public string? Porte {get; set;}

        public string? Sexo {get; set;}

        [Display(Name = "Espécie")]
        public string? Especie {get; set;}
		
        public int ProprietarioID {get; set;}

        [Display(Name = "Proprietário")]
		public virtual Proprietario? proprietario {get; set;} 
 
        private TimeSpan _idadeAnimal => DateTime.Now - this.DtNascimento;

        [Display(Name = "Idade")]
        public int IdadeAnimal => ((int)_idadeAnimal.TotalDays / 365);

	}
}