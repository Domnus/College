using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using ClickJogos.Models;

namespace ClickJogos.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class JogosController : ControllerBase
    {
        private readonly JogoContext _context;

        public JogosController(JogoContext context)
        {
            _context = context;
        }

        // GET: api/Jogos
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Jogo>>> GetJogos()
        {
          if (_context.Jogos == null)
          {
              return NotFound();
          }
            return await _context.Jogos.ToListAsync();
        }

        // GET: api/Jogos/5
        [HttpGet("{id}")]
        public async Task<ActionResult<Jogo>> GetJogo(long? id)
        {
          if (_context.Jogos == null)
          {
              return NotFound();
          }
            var jogo = await _context.Jogos.FindAsync(id);

            if (jogo == null)
            {
                return NotFound();
            }

            return jogo;
        }

        // PUT: api/Jogos/5
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPut("{id}")]
        public async Task<IActionResult> PutJogo(long? id, Jogo jogo)
        {
            if (id != jogo.id)
            {
                return BadRequest();
            }

            _context.Entry(jogo).State = EntityState.Modified;

            try
            {
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!JogoExists(id))
                {
                    return NotFound();
                }
                else
                {
                    throw;
                }
            }

            return NoContent();
        }

        // POST: api/Jogos
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPost]
        public async Task<ActionResult<Jogo>> PostJogo(Jogo jogo)
        {
          if (_context.Jogos == null)
          {
              return Problem("Entity set 'JogoContext.Jogos'  is null.");
          }
            _context.Jogos.Add(jogo);
            await _context.SaveChangesAsync();

            return CreatedAtAction(nameof(GetJogo), new { id = jogo.id }, jogo);
            //return CreatedAtAction("GetJogo", new { id = jogo.id }, jogo);
        }

        // DELETE: api/Jogos/5
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteJogo(long? id)
        {
            if (_context.Jogos == null)
            {
                return NotFound();
            }
            var jogo = await _context.Jogos.FindAsync(id);
            if (jogo == null)
            {
                return NotFound();
            }

            _context.Jogos.Remove(jogo);
            await _context.SaveChangesAsync();

            return NoContent();
        }

        private bool JogoExists(long? id)
        {
            return (_context.Jogos?.Any(e => e.id == id)).GetValueOrDefault();
        }
    }
}
