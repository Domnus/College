package main

import (
	"fmt"
	"time"
)

type produto struct {
	nome string
	preco int
}

func somaCarrinho(carrinho []produto) int {
	total := 0
	for _, item := range carrinho {
		total += item.preco
	}
	return total
}

func executaCarrinho(numero int) {
	var carrinho []produto

	carrinho = append(carrinho, produto{"Iphone", 499})
	carrinho = append(carrinho, produto{"Kindle", 179})
	carrinho = append(carrinho, produto{"Macbook Pro", 1199})

	total := somaCarrinho(carrinho)

	fmt.Printf("[%d] Total do carrinho é: R$%d\n", numero, total)
}

func main() {
	start := time.Now()

	go executaCarrinho(1)
	go executaCarrinho(2)
	go executaCarrinho(3)
	go executaCarrinho(4)
	go executaCarrinho(5)
	
	final := time.Now()
	time.Sleep(time.Millisecond * 1)
	elapsed := final.Sub(start)

	fmt.Println("Tempo de execução: ", elapsed)
}