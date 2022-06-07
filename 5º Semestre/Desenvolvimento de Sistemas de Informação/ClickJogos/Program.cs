using Microsoft.EntityFrameworkCore;
using ClickJogos.Models;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.

builder.Services.AddControllers();
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddDbContext<JogoContext>(opt => opt.UseInMemoryDatabase("JogoList"));

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment()) { }

app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();

app.Run();
