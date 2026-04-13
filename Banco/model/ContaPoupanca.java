package model;

public class ContaPoupanca {

      public ContaPoupanca(int numero, String titular){
        super(numero, titular);
      }
    
    public void renderjuros(){
        double juros = getSaldo() *0.01;
        depositar(juros);
    }
}
