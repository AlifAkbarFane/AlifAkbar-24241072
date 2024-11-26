#Operasi Aritmatika

#Variabel dengan nilai awal
a = 10
b = 3

# Operasi Penjumlahan (+)
hasil = a + b
print(a, "+", b, "=", hasil )

# Operasi Pengurangan (-)
hasil = a - b
print(a, "-", b, "=", hasil )

# Operasi Perkalian (*)
hasil = a * b
print(a, "*", b, "=", hasil )

#Operasi Pembagian (/)
hasil = a / b
print(a, "/", b, "=", hasil )

#Operasi Perpangkatan (**)
hasil = a ** b
print(a, "**", b, "=", hasil )

#Operasi Modulus (%)
hasil = a % b
print(a, "%", b, "=", hasil )

#Operasi Floor division (//)
hasil = a // b
print(a, "//", b, "=", hasil )

# prioritas operasi 
"""
1. ()
2. perkalian, pembagian, dll -> * / ** % //
3. penjumlahan dan pengurangan 
"""
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,"**",y ,"*", z, "+", x, "/", y ,"-", y, "%", z, "//", x, "=",hasil)








