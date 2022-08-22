public class Item{
    
    String product;
    int quant;
    int price;
    
    public Item(String product, int quant, int price){
        this.product = product;
        this.quant = quant;
        this.price = price;
    }
    
    public int getQuant(){ return this.quant;}
    
    public int getPrice(){ return this.price;}
    
}
