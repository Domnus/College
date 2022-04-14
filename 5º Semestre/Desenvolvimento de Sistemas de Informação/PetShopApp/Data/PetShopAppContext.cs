#nullable disable
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using PetShopApp.Models;

    public class PetShopAppContext : DbContext
    {
        public PetShopAppContext (DbContextOptions<PetShopAppContext> options)
            : base(options)
        {
        }

        public DbSet<PetShopApp.Models.Proprietario> Proprietario { get; set; }

        public DbSet<PetShopApp.Models.Produto> Produto { get; set; }
    }
