import 'Emissor.dart';
import 'EmissorCreator.dart';

void main() {
  Emissor emissor = EmissorCreator().create('SMS');

  emissor.envia('Teste');
}
