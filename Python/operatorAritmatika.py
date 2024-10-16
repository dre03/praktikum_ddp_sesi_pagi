# Operator Aritmatika yang ada di python :
#  Penjumalah simbolnya pake  +
#  Pengurangan simbolnya pake -
#  Pembagian simbolnya peke /
# Perkalian simbolnya pake *
# Modulus simbolnya pake %
# Eksponen/pengkat simbolnya pake **
# Floor Division pembulatan kebawah dari yang angkanya  berupa pecahan simbolnya pake // 

angka_A = 100
angka_B = 2

# Contoh Penggunaan Penjumlahan
print('Penjumlahan ===========')
jumlah = angka_A + angka_B
print(f'Hasilnya, {jumlah}')

# Contoh Penggunaan Perkalian
perkalian = angka_A * angka_B
print(f'Hasilnya, {perkalian}')

# Contoh Penggunaan Pembagian
print('Pembagian ===========')
pembagian = angka_A / angka_B
print(f'Hasilnya, {pembagian}')

# Contoh Penggunaan Floor Division/Pembulatan
print('Floor Division ===========')
floorDivision = angka_A // angka_B
print(f'Hasilnya, {floorDivision}')

# Contoh Penggunaan Modulus/sisa bagi
print('Modulus ===========')
_modulus = 15 % 3
print(f'Hasilnya, {_modulus}')

# Contoh Penggunaan Eksponen/pangkat
print('Pangkat ===========')
pangkat = 5**2
print(f'Hasilnya, {pangkat}')

#Prioritas Operasional
'''
    1. ()
    2. eksponen **
    3. perkalian and teman" *, /, %, //
    4. pertambahan dan pengurangan 
'''

print('Prioritas Operasi')
hitung =  3 ** 2 * (10 + 10)
print(hitung)