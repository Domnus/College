import 'Emissor.dart';

class EmissorSM extends Emissor {
  @override
  void envia(String mensagem) {
    print('Enviando por SM a mensagem: $mensagem');
  }
}