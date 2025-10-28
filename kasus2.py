angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

operator = input("Masukkan operator (+, -, *, /): ")

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

print(f"\n Hasil {operasi}")
print(f"Hasil: {hasil}")
