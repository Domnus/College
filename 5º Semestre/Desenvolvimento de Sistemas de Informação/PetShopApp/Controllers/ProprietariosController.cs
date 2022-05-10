using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using PetShopApp.Models;

namespace PetShopApp.Controllers
{
    public class ProprietariosController : Controller
    {
        private readonly PetShopAppContext _context;

        public ProprietariosController(PetShopAppContext context)
        {
            _context = context;
        }

        // GET: Proprietarios
        public async Task<IActionResult> Index(string searchString)
        {
            var props = from p in _context.Proprietario
                select p;

            if (!String.IsNullOrEmpty(searchString))
            {
                props = props.Where(s => s.Nome!.Contains(searchString));
            }

            return View(await props.ToListAsync());
        }

        // GET: Proprietarios/Details/5
        public async Task<IActionResult> Details(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var proprietario = await _context.Proprietario
                .Include(r => r.Animais)
                .FirstOrDefaultAsync(m => m.Id == id);
            if (proprietario == null)
            {
                return NotFound();
            }

            return View(proprietario);
        }

        // GET: Proprietarios/Create
        public IActionResult Create()
        {
            return View();
        }

        // POST: Proprietarios/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Id,Nome,Cpf,Endereco,Telefone,Email,DtNascimento")] Proprietario proprietario)
        {
            if (ModelState.IsValid)
            {
                _context.Add(proprietario);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Index));
            }
            return View(proprietario);
        }

        // GET: Proprietarios/Edit/5
        public async Task<IActionResult> Edit(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var proprietario = await _context.Proprietario.FindAsync(id);
            if (proprietario == null)
            {
                return NotFound();
            }
            return View(proprietario);
        }

        // POST: Proprietarios/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("Id,Nome,Cpf,Endereco,Telefone,Email,DtNascimento")] Proprietario proprietario)
        {
            if (id != proprietario.Id)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Update(proprietario);
                    await _context.SaveChangesAsync();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!ProprietarioExists(proprietario.Id))
                    {
                        return NotFound();
                    }
                    else
                    {
                        throw;
                    }
                }
                return RedirectToAction(nameof(Index));
            }
            return View(proprietario);
        }

        // GET: Proprietarios/Delete/5
        public async Task<IActionResult> Delete(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var proprietario = await _context.Proprietario
                .FirstOrDefaultAsync(m => m.Id == id);
            if (proprietario == null)
            {
                return NotFound();
            }

            return View(proprietario);
        }

        // POST: Proprietarios/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            var proprietario = await _context.Proprietario.FindAsync(id);
            _context.Proprietario.Remove(proprietario);
            await _context.SaveChangesAsync();
            return RedirectToAction(nameof(Index));
        }

        private bool ProprietarioExists(int id)
        {
            return _context.Proprietario.Any(e => e.Id == id);
        }
    }
}
