# Input : apakah pelanggan memiliki kartu member, dan total belanja
member = input("apakah member(ya/tidak): ").strip().lower()
total_belanja = float (input("masukan total belanja RP: "))

# Menentukan diskon berdasarkan kondisi yang ada
if member == "ya": # jika pelanggan memiliki kartu member
    if total_belanja > 500000:
        diskon_persen = 20
        diskon_rp = total_belanja * (diskon_persen/ 100)
    else:
        diskon_persen = 10 
        diskon_rp = total_belanja * (diskon_persen)
else : # Jika pelanggan tidak memiliki kartu member 
    if total_belanja > 500000:
        diskon_persen = 5
        diskon_rp = total_belanja * (diskon_persen / 100)
    else:
        diskon_persen = 0
        diskon_rp = 0

# menghitung total bayar setelah diskon
total_bayar = total_belanja - diskon_rp

# Output Hasil perhitungan 
print(f"total belanja :{total_belanja:,.0f}")
print(f"diskon persen :{diskon_persen}%")
print(f"diskon RP     :{diskon_rp:,.0f}%")
print(f"bayar RP      :{total_bayar:,.0F}")
