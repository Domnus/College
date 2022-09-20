import 'Acao.dart';
import 'Observer.dart';

class ObserverAcao {
  List<Observer> observadores = [];

  void notifica(Acao acao) {
    observadores.forEach((observador) => observador.update(acao));
  }

  void addObservador(Observer observador) {
    observadores.add(observador);
  }

  void removeObservador(Observer observador) {
    observadores.remove(observador);
  }
}
