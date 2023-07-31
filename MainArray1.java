package com.gading.fazrigading031;

public class MainArray1 {
    public static void main(String[] args){
        Array1 obj = new Array1();
        int bilangan[] = {-5, -3, -6, -3, -4};
        // bilangan
        obj.tampil("Bilangan: ");
        obj.setBilangan(bilangan);
        obj.tampil(obj.getBilangan());
        // max
        obj.tampil("Maksimum:");
        obj.setMax(bilangan);
        System.out.println(obj.getMax());
        // min
        obj.tampil("Minimum:");
        obj.setMin(bilangan);
        obj.tampil(obj.getMin());
        // rata-rata
        obj.tampil("Rata-Rata:");
        obj.setRata2(bilangan);
        obj.tampil(obj.getRata2());
        // index nilai -3
        obj.tampil("Angka -3 terletak di:");
        obj.setIndex(bilangan, -3);
        // optimasi
        obj.clear();
        bilangan = null;
        obj = null;
    }
}
