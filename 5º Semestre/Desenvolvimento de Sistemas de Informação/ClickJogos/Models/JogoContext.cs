using Microsoft.EntityFrameworkCore;

namespace ClickJogos.Models
{
    public class JogoContext : DbContext
    {
        public JogoContext(DbContextOptions<JogoContext> options) : base(options)
            { }
        public DbSet<Jogo> ?Jogos { get; set; }
    }
}