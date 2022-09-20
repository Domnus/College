import 'Acao.dart';
import 'Corretora.dart';
import 'Interessados/Banco.dart';
import 'Interessados/PessoaFisica.dart';

main() {
  Acao acao = Acao("011", 10.0);

  Corretora corretora = Corretora("XP Investimentos");
  PessoaFisica pessoaFisica = PessoaFisica("João");
  Banco banco = Banco("Bradesco");

  acao.observadorAcao.addObservador(corretora);
  acao.observadorAcao.addObservador(pessoaFisica);

  acao.updateValor(150);

  acao.observadorAcao.addObservador(banco);
  acao.observadorAcao.removeObservador(pessoaFisica);

  acao.updateValor(70);
}
