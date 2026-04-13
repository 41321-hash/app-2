package model;

public class Conta {
    

    private int numero;

    private String titular;

    private double saldo;


    public Conta(int numero, String titular){
        this.numero = numero;
        this.titular = titular;
        this.saldo = 0;
    }
}
