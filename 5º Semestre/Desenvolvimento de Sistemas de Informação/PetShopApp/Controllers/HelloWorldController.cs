using Microsoft.AspNetCore.Mvc;
using System.Text.Encodings.Web;

namespace PetShopApp.Controllers
{
    public class HelloWorldController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }

        public IActionResult Welcome(string name, int vezes = 1)
        {
            ViewData["Mensagem"] = "Olá " + name;
            ViewData["vezes"] = vezes;

            return View();
        }
    }
}
