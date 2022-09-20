import 'ObserverAcao.dart';

class Acao {
  String codigo = '';
  double valor = 0;
  ObserverAcao observadorAcao = ObserverAcao();

  Acao(this.codigo, this.valor);

  void updateValor(double novoValor) {
    valor = novoValor;
    observadorAcao.notifica(this);
  }
}
