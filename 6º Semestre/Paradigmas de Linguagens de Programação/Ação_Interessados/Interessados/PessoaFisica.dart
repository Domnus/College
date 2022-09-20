import '../Acao.dart';
import '../Observer.dart';

class PessoaFisica extends Observer {
  String nome;
  PessoaFisica(this.nome);

  @override
  void update(Acao acao) {
    print('Pessoa Física $nome: A ação ${acao.codigo} '
        'teve seu valor alterado para ${acao.valor}');
  }
}
