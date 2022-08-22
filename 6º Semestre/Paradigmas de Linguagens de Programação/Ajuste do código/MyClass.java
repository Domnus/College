public class MyClass {
    public static void main(String args[]) {
   
      Customer customer = new Customer("Pedro",1000);

      Order order = new Order(customer, new FidelityPromo());
      order.addItem(new Item("Coca Cola 350", 1, 200));
      order.addItem(new Item("Coca Cola 600", 1, 800));
      
      System.out.println("Total = " + order.total());
      System.out.println("Com Desconto = " + order.due());
        
    }
}