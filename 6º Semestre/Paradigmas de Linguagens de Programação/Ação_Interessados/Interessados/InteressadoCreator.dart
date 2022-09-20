import 'Banco.dart';
import 'InteressadoType.dart';
import 'PessoaFisica.dart';
import 'PessoaJuridica.dart';

class InteressadoCreator {
  create(interessadoType) {
    switch (interessadoType) {
      case Interessado.Banco:
        return Banco('XP Investimentos');
      case Interessado.PessoaFisica:
        return PessoaFisica('João');
      case Interessado.PessoaJuridica:
        return PessoaJuridica('Empresa X');
      default:
        return null;
    }
  }
}