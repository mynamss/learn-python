# Setiap data yang diinputkan pasti akan menjadi string

user_name = input("Masukkan nama: ")
print("Input:", user_name, ",type:", type(user_name))

# Jika ingin mengambil int, maka: 
angka_int = int(input("Masukkan angka int: "))
print("Input:", angka_int, ",type:", type(angka_int))

# Jika ingin mengambil float, maka: 
angka_float = float(input("Masukkan angka desimal: "))
print("Input:", angka_float, ",type:", type(angka_float))

# Jika ingin mengambil boolean
biner = bool(int(input("Masukkan nilai bool: ")))
print("Input:", biner, ",type:", type(biner))