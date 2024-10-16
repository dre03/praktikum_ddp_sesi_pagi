angka = 10
angka /= 3 # angka = angka / 3
print(f'Hasil Pembagian, {angka}')
print('=========')
angka_B = 10
angka_B //= 3 # angka_B = angka_B // 2
print(f'Hasil Flopr D/pembulatan, {angka_B}')

print('=========')
angka *= 3 # angka = angka + 3
print(f'Hasil Perkalian, {int(angka)}')

print('=========')
angkaC = 2
angkaC %= 4 # angka = angka % 3
print(f'Hasil Modulus/sisa bagi, {angkaC}')

x = 10
print(format(x, '08b'))
x &= 2
print(format(x, '08b'))