function somar()
{
    var n1 = document.getElementById("numero1");
    var n2 = document.getElementById("numero2");
    
    var valor1 = Number(n1.value);
    var valor2 = Number(n2.value);

    var soma = valor1 + valor2;

    alert("O valor da soma é: " + soma);
}