import '../Acao.dart';
import '../Observer.dart';

class Banco extends Observer {
  String nome;

  Banco(this.nome);

  @override
  void update(Acao acao) {
    print('Banco $nome: A ação ${acao.codigo} '
        'teve seu valor alterado para ${acao.valor}');
  }
}
