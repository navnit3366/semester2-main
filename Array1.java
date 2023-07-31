package com.gading.fazrigading031;

public class Array1 {
    private int[] bilangan;
    private int n;
    private int max;
    private int min;
    private double jumlah;
    private double rata2;
    private int[] index;
    //=========================//
    // getter bilangan
    public int[] getBilangan() {
        return bilangan;
    }
    // setter bilangan
    public void setBilangan(int[] bilangan) {
        this.bilangan = bilangan;
    }
    //=========================//
    // setter jumlah elemen
    public void setN(int n) {
        this.n = n;
    }
    // getter jumlah elemen
    public int getN() {
        return n;
    }
    //=========================//
    // setter nilai maksimum
    public void setMax(int[] bilangan) {
        max = bilangan[0];
        for (int i = 0; i < bilangan.length; i++){
            if (max < bilangan[i]){
                max = bilangan[i];
            }
        }
    }
    // getter nilai maksimum
    public int getMax() {
        return max;
    }
    //=========================//
    // setter nilai minimum
    public void setMin(int[] bilangan) {
        min = bilangan[0];
        for (int i = 0; i < bilangan.length; i++) {
            if (min > bilangan[i]) {
                min = bilangan[i];
            }
        }
    }
    // getter nilai minimum
    public int getMin() {
        return min;
    }
    //=========================//
    // setter jumlah bilangan
    public void setJumlah(double jumlah) {
        this.jumlah = jumlah;
    }
    // getter jumlah bilangan
    public double getJumlah() {
        return jumlah;
    }
    //=========================//
    // setter rata-rata
    public void setRata2(int[] bilangan) {
        rata2 = 0;
        for (int i = 0; i < bilangan.length; i++) {
            jumlah += bilangan[i];
            n++;
        }
        rata2 = jumlah/n;
    }
    // getter rata-rata
    public double getRata2() {
        return rata2;
    }
    //=========================//
    // setter index
    public void setIndex(int[] bilangan, int a){
        String data = "";
        for (int i = 0; i < bilangan.length; i++){
            if (a == bilangan[i]) {
                data += "Index Ke-"+i+"\n";
            }
        }
        System.out.println(data);
    }
    // getter index
    public int[] getIndex(){
        return index;
    }
    //=========================//
    // object tampil
    public void tampil(int a[]) {
        String data = "";
        for (int i = 0; i < a.length; i++) {
            if (i == 0) {
                data += a[i];
            }
            else {
                data += ", "+a[i];
            }
        }
        System.out.println(data);
        a = null;
        data = null;
    }
    // object tampil untuk String
    public void tampil(String a) {
        System.out.println(a);
        a = null;
    }
    // object tampil untuk integer
    public void tampil(int a) {
        System.out.println(a);
    }
    // object tampil untuk double
    public void tampil(double a) {
        System.out.println(a);
    }
    // object hapus
    public void clear(){
        bilangan = null;
        rata2 = 0;
        max = 0;
        min = 0;
        jumlah = 0;
        n = 0;
    }
}

