# Operasi Komperasi

# Setiap hasil komperasi selalu bertipe boolean (TRUE/FALSE)

# >, <, =, !=, >=, <=, is, dan is not

#deklarasi variabel
a = 4
b = 2 

#lebih besar dari (>)
print("=== Lebih besar dari (>)")
hasil = a > 2 # true
print(a, ">", 2, "=", hasil)
hasil = b > 3 # false
print(a, ">", 3, "=", hasil)
hasil = b > 2 # false
print(a, ">", 2, "=", hasil)

#kurang dari (<)
print("=== kurang dari (<)")
hasil = a < 2 # true
print(a, "<", 2, "=", hasil)
hasil = b < 3 # false
print(a, "<", 3, "=", hasil)
hasil = b < 2 # false
print(a, "<", 2, "=", hasil)

#lebih dari sama dengan (=)
print("=== kurang dari (>=)")
hasil = a >= 2 # true
print(a, ">=", 2, "=", hasil)
hasil = b >= 3 # false
print(a, ">=", 3, "=", hasil)
hasil = b >= 2 # false
print(a, ">=", 2, "=", hasil)

#kurang dari sama dengan (<=)
print("=== kurang dari (<=)")
hasil = a <= 2 # true
print(a, "<=", 2, "=", hasil)
hasil = b <= 3 # false
print(a, "<=", 3, "=", hasil)
hasil = b <= 2 # false
print(a, "<=", 2, "=", hasil)

#sama dengan (==)
print("=== kurang dari (==)")
hasil = a == 2 # true
print(a, "==", 2, "=", hasil)
hasil = b == 2 # false
print(b, "==", 2, "=", hasil)

#tidak sama dengan (!=)
print("=== kurang dari (!=)")
hasil = a != 2 # true
print(a, "!=", 2, "=", hasil)
hasil = b != 2 # false
print(b, "!=", 2, "=", hasil)

# is sebagai komparasi objek 
x = 5
y = 5
hasil = x is y 
print("nilai x : ", x, "id", hex (id(x)))
print("nilai y : ", y, "id", hex (id(y)))
print(x, "is", y, "=", hasil)






