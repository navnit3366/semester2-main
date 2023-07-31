package com.fazrigading.productivity;

public class Main {
    public static void main(String[] args) {
        Todo to_do1 = new Todo();
        Todo to_do2 = new Todo();
        Calendar cal1 = new Calendar();
        Calendar cal2 = new Calendar();
        
        to_do1.setNomor(1);
        to_do1.setIsi("Tugas SCT SO");
        to_do2.setNomor(2);
        to_do2.setIsi("Tugas Post-test JKK");
        
        cal1.setNomor(1);
        cal1.setTanggal(13);
        cal1.setBulan(4);
        cal1.setTahun(2021);
        cal1.setIsi("Kumpul Post-test 2 PBO");
        
        cal2.setNomor(2);
        cal2.setTanggal(14);
        cal2.setBulan(4);
        cal2.setTahun(2021);
        cal2.setIsi("Praktikum SO & APL #2");
        
        System.out.println("To-Do:");
        to_do1.tampil(to_do1.getNomor(), to_do1.getIsi());
        to_do2.tampil(to_do2.getNomor(), to_do2.getIsi());
        System.out.println("Calendar:");
        cal1.tampil(cal1.getNomor(), cal1.getTanggal(), cal1.getBulan(), cal1.getTahun(), cal1.getIsi());
        cal2.tampil(cal2.getNomor(), cal2.getTanggal(), cal2.getBulan(), cal2.getTahun(), cal2.getIsi());
    }
}