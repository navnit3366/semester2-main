import csv
import os
from datetime import date

kalender = {"No":[],"Tanggal":[],"Kegiatan":[]}
todo = []
currentDate = str(date.today())
sekarang = currentDate.split(sep="-")
class WaktuSalah(ValueError): "Kesalahan dalam format waktu."
class BukanKabisat(ValueError): "Kesalahan dalam tahun bukan kabisat."

def cekKabisat(tahun):
    if tahun % 400 == 0: return 1
    elif tahun % 100 == 0: return 0
    elif tahun % 4 == 0: return 1
    else: return 0

def cekBulan(bulan):
    bln30 = [4,6,9,11]
    if bulan == 2: return 28
    for data in bln30:
        if data == bulan: return 30
    return 31

def inputDate(status):
    while True:
        try:
            while status == 3:
                tahun = int(input("Thn> "))
                if tahun == 0: status = -1
                elif tahun < int(sekarang[0]): raise WaktuSalah
                elif tahun >= int(sekarang[0]) and tahun < 10000:
                    tahunSkrg = True if tahun == int(sekarang[0]) else False
                    kabisat = cekKabisat(tahun)
                    status = 2
                else: raise ValueError
            while status == 2:
                bulan = int(input("Bln> "))
                if bulan == 0: status = -1
                if 0 < bulan <= 12:
                    if tahunSkrg == True and bulan < int(sekarang[1]): raise WaktuSalah
                    else:
                        bulanSkrg = True if bulan == int(sekarang[1]) else False
                        thnblnSkrg = tahunSkrg and bulanSkrg
                        maxBulan = cekBulan(bulan)
                        status = 1
                else: raise ValueError
            while status == 1:
                tanggal = int(input("Tgl> "))
                if tanggal == 0: status = -1
                if 0 < tanggal <= int(maxBulan):
                    if kabisat == 0 and bulan == 2 and tanggal >= 29: raise BukanKabisat
                    elif thnblnSkrg == True and tanggal < int(sekarang[2]): raise WaktuSalah
                    else: status = 0
                else: raise ValueError
            
            if status == -1: break
            if len(str(bulan)) == 1: bulan = "0" + str(bulan)
            if len(str(tanggal)) == 1: tanggal = "0" + str(tanggal)
            joinedDate = str(tahun) + "-" + str(bulan) + "-" + str(tanggal)
        except WaktuSalah:
            input("Sayangnya waktu tidak bisa diputar kembali, bro.\nTekan Enter untuk ulang...")
        except BukanKabisat:
            input("Tidak ada tanggal 29 di bulan Februari tahun itu, bro.\nTekan Enter untuk ulang...")
        except ValueError:
            if status == 3: input("Format tahun salah.\nTekan Enter untuk ulang...")
            if status == 2: input("Format bulan salah.\nTekan Enter untuk ulang...")
            if status == 1: input("Format tanggal salah.\nTekan Enter untuk ulang...")
        else: break
    return 0 if status == -1 else joinedDate

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def quicksort(arr, kiri, kanan, tipe):
    if len(arr) == 1: return arr
    if kiri < kanan:
        pivot = arr[kanan]
        i = kiri - 1
        for j in range(kiri, kanan):
            if tipe == 0:
                if arr[j][0] <= pivot[0]:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            if tipe == 1:
                if arr[j][0] >= pivot[0]:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[kanan] = arr[kanan], arr[i+1]
        pi = i+1
        quicksort(arr, kiri, pi - 1, tipe)
        quicksort(arr, pi + 1, kanan, tipe)

def aturIndex(kategori, temp_index, n_temp_index):
    temp = kalender[kategori].copy()
    kalender[kategori].clear()
    for i in range(n_temp_index): 
        kalender[kategori].append(temp[temp_index[i][1]])
    temp.clear()

def shellsort(arr, tipe):
    n = len(arr)
    gap = n//2
    while gap > 0:
        for i in range(gap,n):
            temp_index = arr[i]
            j = i
            if tipe == 0:
                while j >= gap and arr[j-gap] > temp_index:
                    arr[j] = arr[j-gap]
                    j -= gap
            elif tipe == 1:
                while j >= gap and arr[j-gap] < temp_index:
                    arr[j] = arr[j-gap]
                    j -= gap
            arr[j] = temp_index
        gap //= 2

def fibonacciSearch(array, x, n):
    def banding(a,b): return a if a < b else b
    F0 = 0
    F1 = 1
    F = 1
    offset = -1

    while (F < n):
        F0 = F1
        F1 = F
        F = F0 + F1
    
    while (F > 1):
        i = banding(offset + F0, n-1)
        if array[i] < x:
            F = F1
            F1 = F0
            F0 = F - F1
            offset = i
        elif array[i] > x:
            F = F0
            F1 = F1 - F0
            F0 = F - F1
        else:
            return i

    if array[n-1] == x:
        return offset + 1
    return -1

def menu(tipe):
    cls()
    if tipe == 0:
        print("============== Productivity App v5.0 ==============")
        print("[1] To-Do Lists")
        print("[2] Kalender Kegiatan")
        print("[0] Keluar")
        print("===================================================")
    elif tipe == 1:
        print("=================== To-Do Lists ===================")
        agenda(1)
        print("[1] Tambah Kegiatan")
        print("[2] Ubah Kegiatan")
        print("[3] Hapus Kegiatan")
        print("[4] Urutkan Kegiatan")
        print("[5] Cari Kegiatan")
        print("[0] Kembali")
        print("===================================================")
    elif tipe == 2:
        print("================ Kalender Kegiatan ================")
        agenda(2)
        print("[1] Tambah Jadwal")
        print("[2] Ubah Jadwal")
        print("[3] Hapus Jadwal")
        print("[4] Urutkan Jadwal")
        print("[5] Cari Jadwal")
        print("[0] Kembali")
        print("===================================================")
    submenu = input("Select> ")
    return select(tipe, submenu)

def select(tipe, submenu):
    if tipe == 0:
        if submenu == '1': return menu(1)
        if submenu == '2': return menu(2)
        if submenu == '0': return exit(0)
        else:
            input("Menu tidak tersedia.\nTekan Enter untuk lanjut...")
            return menu(tipe)
    elif tipe == 1:
        if submenu == '1': return tambah(1)
        if submenu == '2': return ubah(1)
        if submenu == '3': return hapus(1)
        if submenu == '4': return urut(1)
        if submenu == '5': return cari(1)
        if submenu == '0': return menu(0)
        else:
            input("Menu tidak tersedia.\nTekan Enter untuk lanjut...")
            return menu(tipe)
    elif tipe == 2:
        if submenu == '1': return tambah(2)
        if submenu == '2': return ubah(2)
        if submenu == '3': return hapus(2)
        if submenu == '4': return urut(2)
        if submenu == '5': return cari(2)
        if submenu == '0': return menu(0)
        else:
            input("Menu tidak tersedia.\nTekan Enter untuk lanjut...")
            return menu(tipe)

def tambah(tipe):
    print("Ketik 0 untuk kembali.")
    if tipe == 1:
        while True:
            try:
                n = int(input("Sebanyak> "))
                if n < 0: raise ValueError 
                if n == 0: break
            except ValueError: input("Masukkan angka positif.\nTekan Enter untuk lanjut...")
            except: input("Masukkan angka.\nTekan Enter untuk lanjut...")
            else:
                while n > 0:
                    tambah = input("Add> ")
                    with open('todo.csv', 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([tambah])
                    n -= 1
                break
    if tipe == 2:
        joinedDate = inputDate(3)
        if joinedDate == 0: return menu(tipe)
        while True:
            try:
                n = int(input("Sebanyak> "))
                if n == 0: break
            except:
                if n < 0 : input("Masukkan angka positif.\nTekan Enter untuk lanjut...") 
                else: input("Masukkan angka.\nTekan Enter untuk lanjut...")
            else:
                nextIndex = len(kalender['No'])
                while n != 0:
                    nextIndex += 1
                    tambah = input("Add> ")
                    with open('kalender.csv', 'a', newline='') as file:
                        fieldnames = ['No', 'Tanggal', 'Kegiatan']
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writerow({"No":nextIndex, "Tanggal":joinedDate, "Kegiatan":tambah})
                    n -= 1
                break
    return menu(tipe)

def ubah(tipe):
    print("Ketik 0 untuk kembali.")
    while True:
        try:
            nomor = int(input("No> "))
            selectedIndex = nomor-1
            if nomor == 0: break
            if nomor < 0: raise ValueError
            if tipe == 1: 
                if selectedIndex not in range(len(todo)): raise IndexError
            if tipe == 2: 
                if selectedIndex not in range(len(kalender['No'])): raise IndexError
        except ValueError: input("Masukkan angka positif.\nTekan Enter untuk lanjut...")
        except IndexError: input("Pilihan tidak ditemukan.\nTekan Enter untuk lanjut...")
        except: input("Masukkan angka.\nTekan Enter untuk lanjut...")
        else:
            if tipe == 1:
                ganti = input("New> ")
                todo[selectedIndex] = [ganti]
                with open('todo.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(todo)
            if tipe == 2:
                joinedDate = inputDate(3)
                if joinedDate == 0: break
                ganti = input("New> ")
                kalender['Tanggal'][selectedIndex] = joinedDate
                kalender['Kegiatan'][selectedIndex] = ganti
                with open('kalender.csv', 'w', newline='') as file:
                    fieldnames = ['No', 'Tanggal', 'Kegiatan']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    for i in range(len(kalender['No'])):
                        writer.writerow({'No': kalender['No'][i], 'Tanggal': kalender['Tanggal'][i], 'Kegiatan': kalender['Kegiatan'][i]})
            break
    return menu(tipe)

def hapus(tipe):
    ada1 = tipe == 1 and len(todo) > 0
    ada2 = tipe == 2 and len(kalender['No']) > 0
    ada = ada1 or ada2
    while ada == True:
        try:
            nomor = int(input("No> "))
            selectedIndex = nomor-1
            if nomor == 0: break
            if nomor < 0: raise ValueError
            if tipe == 1: 
                if selectedIndex not in range(len(todo)): raise IndexError
            if tipe == 2: 
                if selectedIndex not in range(len(kalender['No'])): raise IndexError
        except ValueError: input("Masukkan angka positif.\nTekan Enter untuk lanjut...")
        except IndexError: input("Pilihan tidak ditemukan.\nTekan Enter untuk lanjut...")
        except: input("Masukkan angka.\nTekan Enter untuk lanjut...")
        else:
            if tipe == 1:
                todo.pop(selectedIndex)
                with open('todo.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(todo)
                break

            if tipe == 2:
                kalender['No'].clear()
                for i in range(len(kalender['Tanggal'])-1): kalender['No'].append(i+1)
                kalender['Tanggal'].pop(selectedIndex)
                kalender['Kegiatan'].pop(selectedIndex)
                with open('kalender.csv', 'w', newline='') as file:
                    fieldnames = ['No', 'Tanggal', 'Kegiatan']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    for i in range(len(kalender['No'])):
                        writer.writerow({'No': kalender['No'][i], 'Tanggal': kalender['Tanggal'][i], 'Kegiatan': kalender['Kegiatan'][i]})
                break
    else:
        input("Tidak ada kegiatan yang dapat dihapus.\nTekan Enter untuk kembali...")
    return menu(tipe)

def urut(tipe):
    if tipe == 2:
        status = 2
        print("Sorting berdasarkan:")
        print("[1] Tanggal")
        print("[2] Kegiatan")
        print("[0] Kembali")
        while status == 2:
            select_kategori = input("Select> ")
            if select_kategori == '0': status = -1
            elif select_kategori == '1' or select_kategori == '2': break
            else: input("Pilihan tidak tersedia.\nTekan Enter untuk lanjut...")
    status = 1
    print("Sorting secara:")
    print("[1] Ascending")
    print("[2] Descending")
    print("[0] Kembali")
    while status == 1:
        select_sorting = input("Select> ")
        if select_sorting == '0': break
        if select_sorting == '1' or select_sorting == '2':
            if tipe == 1:
                if select_sorting == '1': shellsort(todo, 0)
                elif select_sorting == '2': shellsort(todo, 1)
                else: input("Pilihan tidak tersedia.\nTekan Enter untuk lanjut...")
                with open('todo.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(todo)
                break
            if tipe == 2:
                kategori = 'Tanggal' if select_kategori == '1' else 'Kegiatan'
                temp_index = []
                for i in range(len(kalender[kategori])): 
                    temp_index.append([kalender[kategori][i], i])
                n_temp_index = len(temp_index)
                tipeSort = 0 if select_sorting == '1' else 1
                quicksort(temp_index, 0, n_temp_index-1, int(tipeSort))
                aturIndex('Tanggal', temp_index, n_temp_index)
                aturIndex('Kegiatan', temp_index, n_temp_index)
                with open('kalender.csv', 'w', newline='') as file:
                    fieldnames = ['No', 'Tanggal', 'Kegiatan']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    for i in range(len(kalender['No'])):
                        writer.writerow({'No': kalender['No'][i], 'Tanggal': kalender['Tanggal'][i], 'Kegiatan': kalender['Kegiatan'][i]})
                break
        else: input("Pilihan tidak tersedia\nTekan Enter untuk lanjut...")
    if status == -1: return menu(tipe)
    return menu(tipe)

def cari(tipe):
    cari = input("Find> ")
    jenis = 'kata' if len(cari) > 1 else 'huruf'
    if tipe == 1:
        for data in todo:
            arr = list(data[0])
            arr.sort()
            n = len(arr)
            ketemu = 0
            hurufKetemu = []
            for huruf in cari:
                foundIndex = fibonacciSearch(arr, huruf, n)
                if foundIndex >= 0:
                    ketemu += 1
                    if ketemu >= 0:
                        hurufKetemu.append(huruf)
            nomorKetemu = todo.index(data) + 1
            if ketemu == len(cari):
                print("Ditemukan", jenis, cari, "pada nomor ke-" + str(nomorKetemu))
            elif ketemu > 0:
                print("Ditemukan huruf", hurufKetemu, "pada nomor ke-" + str(nomorKetemu))
            elif ketemu <= 0:
                print("Tidak ditemukan", jenis, cari, "pada nomor ke-" + str(nomorKetemu))
    if tipe == 2:
        for data in kalender['Kegiatan']:
            arr = list(data)
            arr.sort()
            n = len(arr)
            ketemu = 0
            hurufKetemu = []
            for huruf in cari:
                foundIndex = fibonacciSearch(arr, huruf, n)
                if foundIndex >= 0:
                    ketemu += 1
                    if ketemu >= 0:
                        hurufKetemu.append(huruf)
            nomorKetemu = kalender['Kegiatan'].index(data) + 1
            if ketemu == len(cari):
                print("Ditemukan", jenis, cari, "pada nomor ke-" + str(nomorKetemu))
            elif ketemu > 0:
                print("Ditemukan huruf", hurufKetemu, "pada nomor ke-" + str(nomorKetemu))
            elif ketemu <= 0:
                print("Tidak ditemukan", jenis, cari, "pada nomor ke-" + str(nomorKetemu))
    input("Tekan Enter untuk kembali...")
    return menu(tipe)

def agenda(tipe):
    global todo, kalender
    todo = []
    kalender = {"No":[], "Tanggal":[],"Kegiatan":[]}
    if tipe == 1:
        with open('todo.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader: todo.append(row)
        if len(todo) > 0:
            print(f"No\tKegiatan")
            print("-"*51)
            nomor = 1
            for data in todo:
                print(f"{nomor}\t{data[0]}")
                nomor += 1
            print("")
        else: print("Tidak ada kegiatan yang tercatat.\n")

    elif tipe == 2:
        with open('kalender.csv', 'r') as file:
            reader = csv.DictReader(file, delimiter=',')
            for row in reader: 
                kalender['No'].append(row['No'])
                kalender['Tanggal'].append(row['Tanggal'])
                kalender['Kegiatan'].append(row['Kegiatan'])
        if len(kalender) > 0:
            print("No\tTanggal\t\tKegiatan")
            print("-"*51)
            for i in range(len(kalender['No'])):
                print(kalender['No'][i] + "\t" + kalender['Tanggal'][i] + "\t" + kalender['Kegiatan'][i])
            print("")
        else: print("Tidak ada jadwal yang tercatat.\n")

menu(0)