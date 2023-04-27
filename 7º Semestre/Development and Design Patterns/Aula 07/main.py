from NotaFiscalBuilder import NotaFiscalBuilder
from EnviaEmail import EnviaEmail
from EnviaSMS import EnviaSMS
from Impressora import Impressora
from Item import Item

notafiscalBuilder = NotaFiscalBuilder()
notafiscalBuilder.com_razao_social('UNIVEM')
notafiscalBuilder.com_cnpj('123.456.789/0001-10')
notafiscalBuilder.com_itens(Item('item1', 100))
notafiscalBuilder.com_itens(Item('item2', 200))
notafiscalBuilder.com_itens(Item('item3', 400))
notafiscalBuilder.com_detalhes('detalhes')
notafiscalBuilder.com_data_de_emissao("11/02/2002")
notafiscalBuilder.com_observacoes('observacoes')

notafiscalBuilder.adiciona_acao(EnviaEmail())
notafiscalBuilder.adiciona_acao(EnviaSMS())
notafiscalBuilder.adiciona_acao(Impressora())

notafiscal = notafiscalBuilder.constroi()

print(notafiscal.razao_social)
print(notafiscal.cnpj)
for item in notafiscal.itens:
	print(item.nome)
print(notafiscal.detalhes)
print(notafiscal.data_de_emissao)
print(notafiscal.observacoes)
print(notafiscal.valor_bruto)
print(notafiscal.impostos)
