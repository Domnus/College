start_time = NaiveDateTime.utc_now

carrinho = [
	%{"produto" => "iPhone", "preco" => 499}, 
	%{"produto" => "Kindle", "preco" => 179}, 
	%{"produto" => "Macbook Pro", "preco" => 1199}
]

total = Enum.sum(Enum.map(carrinho, fn item -> item["preco"] end))

IO.puts "O Total do carrinho é: #{total}"

end_time = NaiveDateTime.utc_now
time_total = NaiveDateTime.diff(end_time, start_time, :millisecond)

IO.puts "Tempo de execução: #{time_total}ms"