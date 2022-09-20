import '../Acao.dart';
import '../Observer.dart';

class PessoaJuridica extends Observer {
  String nome;
  PessoaJuridica(this.nome);

  @override
  void update(Acao acao) {
    print('Pessoa Jurídica $nome: A ação ${acao.codigo} '
        'teve seu valor alterado para ${acao.valor}');
  }
}
