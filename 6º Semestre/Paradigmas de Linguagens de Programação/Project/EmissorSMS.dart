import 'Emissor.dart';

class EmissorSMS extends Emissor {
  @override
  void envia(String mensagem) {
    print('Enviando por SMS a mensagem: ');
    print(mensagem);
  }
}