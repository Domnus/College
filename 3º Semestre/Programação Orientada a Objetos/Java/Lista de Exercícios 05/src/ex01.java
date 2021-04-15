import javax.swing.*;
import java.util.ArrayList;

class Contato {
    private String nome, fone, dt_aniversario;

    public Contato(String nome, String fone, String dt_aniversario) {
        this.nome = nome;
        this.fone = fone;
        this.dt_aniversario = dt_aniversario;
    }

    public String getNome() {
        return nome;
    }

    public String getFone() {
        return fone;
    }

    public String getDt_aniversario() {
        return dt_aniversario;
    }

    public void setFone(String fone) {
        this.fone = fone;
    }

} // Contato

class Agenda {
    private ArrayList<Contato> listaContatos;

    public Agenda() {
        this.listaContatos = new ArrayList<Contato>();
    }

    public void incluiContato(String nome, String fone, String dt) {
        this.listaContatos.add(new Contato(nome, fone, dt));
    }

    public void incluiContato(Contato c) {
        this.listaContatos.add(c);
    }

    public boolean atualizaContato(String nome, String novoFone) {
        for (Contato c : this.listaContatos) {
            if (c.getNome().equals(nome)) {
                c.setFone(novoFone);
                return true;
            }
        }
        return false;
    }

    public boolean excluirContato(String nome) {
        for (Contato c : this.listaContatos) {
            if (c.getNome().equals(nome)) {
                this.listaContatos.remove(c);
                return true;
            }
        }
        return false;
    }

    public Contato consultaContato(String nome) {
        for (Contato c : this.listaContatos) {
            if (c.getNome().equals(nome)) {
                return c;
            }
        }
        return null;
    }
}

public class ex01 {
    public static void main(String[] args) {
        Agenda agenda = new Agenda();
        String op;
        String[] menu = {"Cadastrar", "Atualizar", "Excluir", "Consultar", "Finalizar"};

        do {
            op = JOptionPane.showInputDialog(null, "Escolha uma opção", "Agenda", JOptionPane.QUESTION_MESSAGE, null, menu, menu[0]).toString();

            switch (op) {
                case "Cadastrar": 
                    cadastrar(agenda);
                    break;

                case "Atualizar":
                    atualizar(agenda);
                    break;

                case "Excluir":
                    excluir(agenda);
                    break;

                case "Consultar":
                    consultar(agenda);
                    break;
           }
        } while (!op.equals(menu[4]));
    }

    private static void cadastrar(Agenda agenda) {
        String nome, fone, dt_aniversario;

        nome = JOptionPane.showInputDialog("Nome do contato");
        fone = JOptionPane.showInputDialog("Telefone do contato");
        dt_aniversario = JOptionPane.showInputDialog("Data de aniversário do contato");

        agenda.incluiContato(nome, fone, dt_aniversario);
    }

    private static void atualizar(Agenda agenda) {
        String nome, fone;

        nome = JOptionPane.showInputDialog("Nome do contato para atualizar");
        fone = JOptionPane.showInputDialog("Novo telefone");

        if (agenda.atualizaContato(nome, fone)) {
            JOptionPane.showMessageDialog(null, "Contato atualizado!");
        } else {
            JOptionPane.showMessageDialog(null, "Contato inexistente!");
        }
 
    }

    private static void excluir(Agenda agenda) {
        String nome;

        nome = JOptionPane.showInputDialog("Nome do contato para excluir");

        if (agenda.excluirContato(nome)) {
            JOptionPane.showMessageDialog(null, "Contato excluído!");
        } else {
            JOptionPane.showMessageDialog(null, "Contato inexistente!");
        }
    }

    private static void consultar(Agenda agenda) {
        String nome;

        nome = JOptionPane.showInputDialog("Nome do contato para consultar");

        Contato c = agenda.consultaContato(nome);

        if (c != null) {
            JOptionPane.showMessageDialog(null, "Nome: " +c.getNome()+ "\nTelefone: " +c.getFone()+ "\nAniversário: " +c.getDt_aniversario());
        } else {
            JOptionPane.showMessageDialog(null, "Contato inexistente!");
        }
    }
}
