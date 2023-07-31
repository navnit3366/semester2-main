package com.fazrigading.productivity;

public class Todo {
    protected int nomor;
    protected String isi;

    protected int getNomor() {return nomor;}
    protected void setNomor(int nomor) {this.nomor = nomor;}

    protected String getIsi() {return isi;}
    protected void setIsi(String isi) {this.isi = isi;}
    
    public void tampil(int nomor, String isi){
        System.out.println("[" + nomor + "] " + isi);
    }
    
    protected void tampil(int nomor, int tanggal, int bulan, int tahun, String isi){
        System.out.println("[" + nomor + "] " + tanggal + "/" + bulan + "/" + tahun + " " + isi);
    }
    
}
