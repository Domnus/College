use std::collections::HashMap;
use std::thread;
use std::time::Duration;
use std::thread::sleep;

fn executar_carrinho(numero: i8) {
	let mut carrinho = HashMap::new();

    carrinho.insert("Iphone", 499);
    carrinho.insert("Kindle", 179);
    carrinho.insert("Macbook Pro", 1199);

    let total = somar_carrinho(&mut carrinho);

    println!("[{}] O valor do carrinho é: {}", numero, total);
}

fn somar_carrinho(carrinho: &mut HashMap<&str, i32>) -> i32 {
    let mut total = 0;

    for (_produto, quantidade) in carrinho.iter() {
        total += quantidade;
    }

    return total;
}

fn main() {
    let now = std::time::Instant::now();

    thread::spawn(|| executar_carrinho(1));
    thread::spawn(|| executar_carrinho(2));
    thread::spawn(|| executar_carrinho(3));
    thread::spawn(|| executar_carrinho(4));
    thread::spawn(|| executar_carrinho(5));

    let elapsed = now.elapsed();
    sleep(Duration::from_millis(200));
    println!("Tempo de execução: {:#.2?}", elapsed);
}