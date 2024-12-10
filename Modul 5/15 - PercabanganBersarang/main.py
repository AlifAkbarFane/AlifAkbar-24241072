# percabangan bersarang / Nested If

# kalkulator
# +,-,x,/,mod,//,pangkat(exponen)

print(20*"=")
print("kalkulator sederhana")
print(20*"=")

angka_1 = float(input("masukan bilangan 1 = : "))
operator = input("operator (+,-,/,x,mod,//,pangkat)")
angka_2 = float(input("masukan bilangan 2 = "))

# percabangan bersarang (elif statement)

if operator == '+' :
    hasil = angka_1 + angka_2
    print(f' hasilnya adalah = {hasil}')
elif operator == '-' :
    hasil = angka_1 - angka_2
    print(f' hasilnya adalah = {hasil}')
elif operator == 'x' or operator == '*':
    hasil = angka_1 * angka_2
    print(f' hasilnya adalah = {hasil}')
elif operator == '/' :
    hasil = angka_1 / angka_2
    print(f' hasilnya adalah = {hasil}')
elif operator == '%' :
    hasil = angka_1 % angka_2
    print(f' hasilnya adalah = {hasil}')
elif operator == '//' :
    hasil = angka_1 // angka_2
    print(f' hasilnya adalah = {hasil}')
elif operator == '**' :
    hasil = angka_1 ** angka_2
    print(f' hasilnya adalah = {hasil}')
print("terimakasih")
