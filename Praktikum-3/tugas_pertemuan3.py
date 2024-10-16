# Jawaban No 1
nama = 'Andre'
nim = '0110221111'
kelas = 'TI04'
no_telp = '08934856934'
alamat = 'Bogor'

# print('Nama saya', nama, '\nnim saya', nim, '\nkelas saya', kelas, '\nNo Telpon saya', no_telp, '\ndan alamat saya', alamat)


# Soal no 4, 
# buat program python untuk mencari nilai konversi dari celcius ke fahreinheit 
# Jawaban No 4

# niali celcius
celcius = int(input('Masukan Suhu dalam Celcius:'))
hasil_fahrenheit = (celcius * 9/5) + 32

print('Suhu dalam Celscius:', celcius,'C')
print('Suhu dalam Fahrenheit:', hasil_fahrenheit,'F')


print('==================')
# Soal no 1 buat program python untuk mencari nilai berat badan ideal sederhana dengan menggunakan variabel saja

berat_badan = int(input('Masuakan Berat badan :'))
tinggBadan = int(input("Masuakn Tinggi Badan :"))
rumus = (tinggBadan/100)**2
hitung_berat_ideal = berat_badan/rumus
print(int(hitung_berat_ideal))


print('==================')


# No 5

# Menghitung Luas Permukaan
jari2 = 20
tinggi =  40
phi =  3.14
luas_permukaan = 2 * phi * jari2 * (jari2 + tinggi)
print("Luas Permukaan Adalah:" , int(luas_permukaan))

# Menghitung Keliling Alas
