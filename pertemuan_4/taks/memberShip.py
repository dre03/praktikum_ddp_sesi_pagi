# Contoh 1: Menggunakan 'in' pada list
buah = ["apel", "jeruk", "pisang"]

print("apel" in buah)   # Output: True, karena "apel" ada di dalam list 'buah'
print("mangga" in buah) # Output: False, karena "mangga" tidak ada di dalam list 'buah'

# Contoh 2: Menggunakan 'not in' pada string
kalimat = "Saya suka makan pisang"

print("pisang" in kalimat)       # Output: True, karena "pisang" ada di dalam string 'kalimat'
print("pisang" not in kalimat)     # Output: True, karena "apel" tidak ada di dalam string 'kalimat'

# Contoh 3: Menggunakan 'in' pada dictionary (memeriksa key)
data_mahasiswa = {"nama": "Andi", "umur": 21, "jurusan": "Teknik Informatika"}

print("nama" in data_mahasiswa)    # Output: True, karena "nama" adalah key di dictionary 'data_mahasiswa'
print("alamat" not in data_mahasiswa)  # Output: True, karena "alamat" bukan key di dictionary 'data_mahasiswa'


# Kesimpulan:
# in digunakan untuk memeriksa apakah elemen tertentu ada dalam urutan atau koleksi.
# not in digunakan untuk memeriksa apakah elemen tertentu tidak ada dalam urutan atau koleksi.
# Operator ini sangat berguna saat bekerja dengan data seperti list, string, atau dictionary, karena memungkinkan Anda memeriksa keberadaan elemen dengan sangat mudah.