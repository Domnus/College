using System.ComponentModel.DataAnnotations;
using System;

namespace PetShopApp.Models
{
    public class Proprietario
    {
        public int Id {get; set;}

        public string Nome {get; set;}

        public string CPF {get; set;}

        public string Endereco {get; set;}

        public string Telefone {get; set;}

        public string Email {get; set;}

        [Display(Name = "Data de Nascimento")]
        [DataType(DataType.Date)]
        public DateTime DtNascimento {get; set;}
    }
}
