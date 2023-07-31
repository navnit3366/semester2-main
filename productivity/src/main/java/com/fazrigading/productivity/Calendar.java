package com.fazrigading.productivity;

public class Calendar extends Todo {
    private int tanggal;
    private int bulan;
    private int tahun;
    
    public int getBulan() {return bulan;}
    public void setBulan(int bulan) {this.bulan = bulan;}

    public int getTahun() {return tahun;}
    public void setTahun(int tahun) {this.tahun = tahun;}

    public int getTanggal() {return tanggal;}
    public void setTanggal(int tanggal) {this.tanggal = tanggal;}
    
    @Override
    public void tampil(int nomor, int tanggal, int bulan, int tahun, String isi){
        System.out.println("[" + nomor + "] " + tanggal + "/" + bulan + "/" + tahun + " " + isi);
    }
}
