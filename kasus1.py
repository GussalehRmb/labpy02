tipe = input("Masukkan tipe tiket (reguler/vip): ").lower()

harga = 50000 if tipe == "reguler" else 100000 if tipe == "vip" else 0

member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").lower()

if member == "ya":
    total = harga * 0.8 
else:
    total = harga

if harga == 0:
    print("Tipe tiket tidak valid.")
else:
    print(f"Harga tiket sebelum diskon: Rp{harga:,}")
    print(f"Total yang harus dibayar: Rp{int(total):,}")
