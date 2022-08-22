public class FidelityPromo{
    
    public int discount(Order order){
        if (order != null) {
            if(order.getCustomer().getPonto()>1000)
                // Retornar 5% do valor total
                return order.total() * 0.05;
        }

        return 0;
    }
    
}
