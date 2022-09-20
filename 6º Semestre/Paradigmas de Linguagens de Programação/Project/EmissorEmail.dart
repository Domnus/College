import 'Emissor.dart';

class EmissorEmail implements Emissor {
  @override
  void envia(String mensagem) {
    print('Enviando por email a mensagem: $mensagem');
  }
}