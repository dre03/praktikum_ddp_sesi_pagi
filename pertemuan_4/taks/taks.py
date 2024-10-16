# Buat variabel list dengan value : [namaKendaraan, JenisKendaraan, ccKendaraan, warna kendaraan, rodakendaraan]
myList = ['Honda Beat', 'Sepeda Motor', 120, 'Hitam', 2]
print(myList)

# tambahkan dari list tersebut di belakang dengan value : [harga kendaraan, tipe kendaraan]
myList.extend([20000000, 'Metic'])
print(myList)

# tambahkan setelah jenis kendaraan dengan value [merk kendaraan]
myList.insert(2, 'Honda')
print(myList)

print('=============================')

# Buat program python dengan match case untuk
# menghitung luas bangun datar :
# jika pilih 1, maka menghitung luas persegi
# jika pilih 2, maka menghitung luas lingkaran
# jika pilih 3, maka menghitung luas segitiga
# Kalau pilihannya tidak ada maka ada keterangan : salah pilih

print("Ini adalah program untuk menghitung luas bangun datar")
print("Pilih Menu angka 1-3 :\n1. Persegi\n2. Lingkaran\n3. Segitiga\n')")
pilihMenu = int(input("Silahkan Pilih Menu dengan mengetikkan angka 1-3 :"))

match pilihMenu:
    case 1:
        print("Ini adalah menu untuk menghitung luas persegi")
        sisi = int(input("Silahkan masukan nilai yang mau di hitung :"))
        hitung = sisi * sisi
        print(f"Luas persegi adalah: {hitung}")
    case 2:
        print("Ini adalah menu untuk menghitung luas lingkaran")
        phi = 3.14
        jariJari = int(input("Silahkan masukan nilai yang mau dihitung :"))
        hitung = phi * jariJari * jariJari
        print(f"Luas lingkaran adalah: {hitung}")
    case 3:
        print("Ini Menu menu untuk menghitung luas segitiga")
        alas = int(input("Silahkan masukan alasnya : "))
        tinggi = int(input("Silahkan masukan tingginya : "))
        hitung = 1/2 * alas * tinggi
        print("Berikut adalah luas segitignya", hitung)
    case _:
        print("Pilihan tidak valid. Silakan pilih antara 1, 2, atau 3.")