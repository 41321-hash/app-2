package model;

public class ContaCorente extends Conta{
    private double tarifaMensal = 12.90;

    public ContaCorente(int numero, String titular){
        super(numero, titular);
    }

    public void descontarTarifa(){
        
    }
}
