import 'Acao.dart';
import 'Observer.dart';

class Corretora implements Observer {
  String name;

  Corretora(this.name);

  @override
  void update(Acao acao) {
    print('Corretora $name: A ação ${acao.codigo} '
        'teve seu valor alterado para ${acao.valor}');
  }
}
