# Meminta input dari dalam fahrenheit
fahrenheit = float(input("Masukkan temperatur dalam Fahrenheit: "))

# Mengonversi Fahrenheit ke Celcius
celsius = (fahrenheit - 32) * 5/9

# Menampilkan hasil konversi 
print(f"{fahrenheit}derajat Fahrenheit = {celsius:.2f}derajat Celcius")