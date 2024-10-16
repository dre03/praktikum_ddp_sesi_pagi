# Contoh 1: Membandingkan dua objek yang sama
a = [1, 2, 3]
b = a  # 'b' menunjuk ke objek yang sama dengan 'a'

# Menggunakan 'is' untuk memeriksa apakah 'a' dan 'b' adalah objek yang sama
print(a is not b)  # Output: True, karena 'b' adalah referensi yang sama dengan 'a'

# Contoh 2: Membandingkan dua objek yang berbeda, tetapi memiliki nilai yang sama
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)  # Output: True, karena nilai dari 'x' dan 'y' sama
print(x is y)  # Output: False, karena 'x' dan 'y' adalah objek yang berbeda

# Contoh 3: Menggunakan 'is not'
z = x

print(x is not z)  # Output: False, karena 'z' adalah referensi yang sama dengan 'x'


# is memeriksa apakah dua variabel menunjuk ke objek yang sama di memori.
# is not memeriksa apakah dua variabel menunjuk ke objek yang berbeda di memori.
# Berbeda dengan == yang hanya membandingkan nilai, bukan apakah mereka adalah objek yang sama.
