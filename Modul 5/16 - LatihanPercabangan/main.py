# percabangan bersarang
# data dalam data

# masukan nilai 
#  >, or and

print(20*"=")
print("data dalam data")
print(20*"=")

nilai = float(input("masukan bilangan 1 = :"))
operator = (input("operator >, and, <=, >= = "))

if operator == '>' :
    hasil = nilai > 90
    print('nilai huruf = A')
elif operator == '<=' :
    hasil = nilai <= 90 and nilai >= 85
    print('nilai huruf = A-')
elif operator == '<=' :
    hasil = nilai <= 85 and nilai >= 80
    print('nilai huruf B+')
elif operator == '<=' :
    hasil = nilai <= 79 and nilai >= 75
    print('nilai huruf B')
elif operator == '<=' :
    hasil = nilai <= 74 and nilai >= 70
    print('nilai huruf B- ')
elif operator == '<=' :
    hasil = nilai <= 69 and nilai >= 65
    print('nilai huruf C+ ')
elif operator == '<=' :
    hasil = nilai <= 64 and nilai >= 60
    print('nilai huruf C ')
elif operator == '<=' :
    hasil = nilai <= 59 and nilai >= 55 
    print('nilai huruf D ')
elif operator == '<' :
    hasil = nilai < 55 
    print('nilai huruf E ')