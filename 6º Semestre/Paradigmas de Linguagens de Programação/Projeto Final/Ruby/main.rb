starting = Process.clock_gettime(Process::CLOCK_MONOTONIC)

class Item
    attr_reader :produto, :preco
    attr_writer :produto, :preco

    def initialize(produto, preco)
      @produto = produto
      @preco = preco
    end
  
    def self.preco
      return @preco
    end
  
  end
  
class Carrinho
    @@total = 0
    
    attr_reader :itens
    attr_writer :itens

    def initialize()
      @itens = []
    end

    def adicionar(item)
      @itens.append(item)
      @@total += item.preco
    end

    def remover(item)
      @itens.delete(item)
      @@total -= item.preco
    end
  
    def total()
      return itens.map{|item|item.preco}.sum
    end
end

def executaCarrinho(numero)
  carrinho = Carrinho.new()

  carrinho.adicionar(Item.new("Iphone", 499))
  carrinho.adicionar(Item.new("Kindle", 179))
  carrinho.adicionar(Item.new("Macbook Pro", 1199))
  puts "#{numero} O total do carrinho é: R$#{carrinho.total()}"
end

Thread.new{executaCarrinho(1)}
Thread.new{executaCarrinho(2)}
Thread.new{executaCarrinho(3)}
Thread.new{executaCarrinho(4)}
Thread.new{executaCarrinho(5)}

ending = Process.clock_gettime(Process::CLOCK_MONOTONIC) 
sleep(0.5)
puts "Tempo de execução: %0.2f ms" % [(ending - starting) * 1000] 
#feito por hugo ATE Q ENFIM 