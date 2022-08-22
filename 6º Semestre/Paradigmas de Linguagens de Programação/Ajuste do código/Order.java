import java.util.List;
import java.util.ArrayList;

public class Order {
    
    Customer customer;
    List<Item> itens;
    FidelityPromo fidelityOrder;
    
    public Order(Customer customer, FidelityPromo fidelityOrder){
        this.customer = customer;
        this.fidelityOrder = fidelityOrder;
    }
    
    public void addItem(Item item){
        if(itens == null)
          itens = new ArrayList<Item>();
          
        itens.add(item);
    }
    
    public int total(){
        int total = 0;

        if (itens != null){
            for(int i=0; i<itens.size(); i++){
                total += itens.get(i).getPrice() * itens.get(i).getQuant();
            }
        }

        return total;
    }
    
    public int due(){
        return total() - fidelityOrder.discount(this);
    }
    
    public Customer getCustomer(){
        return customer;
    }
}
