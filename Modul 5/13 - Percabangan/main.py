# Percabangan 
# struktur
"""
1. if -nya
2. Kondisi
3. aksi
"""
nama = input("masukan nama : ")

# Percabangan yang inline (satu baris)
if nama == "akbar" : print("selamat datang" )
print("terimakasih")

# percabangan indentasi
# if nama == "akbar" :
#    print("selamat datang")
#    print("selamat belajar python")
#print("bukan bagian percabangan")

# percabangan 1 kondisi dengan 2 aksi
# pakai kata kunci 'else'

if nama == "akbar":
    print("selamat datang")
else: 
    print(f' anda {nama}, bukan adam')
print("terimakasih")