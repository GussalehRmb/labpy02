# Program Kalkulator Sederhana

# Meminta dua angka dari pengguna
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Meminta operator aritmatika dari pengguna
operator = input("Masukkan operator (+, -, *, /): ")

# Menentukan operasi aritmatika menggunakan if elif else
if operator == '+':
    hasil = angka1 + angka2
    operasi = "Penjumlahan"
elif operator == '-':
    hasil = angka1 - angka2
    operasi = "Pengurangan"
elif operator == '*':
    hasil = angka1 * angka2
    operasi = "Perkalian"
elif operator == '/':
    if angka2 != 0:
        hasil = angka1 / angka2
        operasi = "Pembagian"
    else:
        hasil = "Error: Tidak bisa dibagi dengan nol!"
        operasi = "Pembagian (tidak valid)"
else:
    hasil = "Operator tidak valid!"
    operasi = "-"

# Menampilkan hasil perhitungan
print(f"\n Hasil {operasi}")
print(f"Hasil: {hasil}")
