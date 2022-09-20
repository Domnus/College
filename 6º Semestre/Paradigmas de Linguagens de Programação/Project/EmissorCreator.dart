import 'Emissor.dart';
import 'EmissorEmail.dart';
import 'EmissorSMS.dart';

class EmissorCreator{
  Emissor create(tipoEmissor) {
    switch (tipoEmissor) {
      case 'SMS':
        return new EmissorSMS();
      case 'Email':
        return new EmissorEmail();
      case 'SM':
        return new EmissorSMS();
      default:
        throw new Exception('Tipo de emissor não suportado');
    }
  }
}