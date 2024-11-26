# String adalah kumpulan dari karakter

data = "ini adalah string"
print(data)
print("panjang karakter : ", len (data))
print("type data : ", type (data))

# 1. cara membuat string 

"""
1. dengan menggunakan single quote
2. dengan menggunakan double quote
"""

data = 'menggunakan single quote'
print(data)

data = 'menggunakan double qoute'
print(data)

print("ini adalah hari jum'at")
print("nama saya ma'ruf")

# 2. kekuatan tanda /

# membuat tanda ' menjadi string 
print('mari sholat jum\'at')
print('nama saya ma\'ruf')

# double backslash 
print('C:\\user\\adam')
print("MU\t\tjuara")

# tab (\t)
print("MU\tjuara")

# backspace (\b)
print("MU\bjuara")

# new line (enter)
print("baris satu.\ baris dua.") # lf -> line feed # macOS
print("baris satu.\ baris dua. ") # CRLF -> windows

# raw string 
print("r C:\user\adam")