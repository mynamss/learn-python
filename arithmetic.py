# Operasi Aritmetika

input_a = int(input("Masukkan a:"))
input_b = int(input("Masukkan b:"))

# Penjumlahan
result =  input_a + input_b
print(input_a, "+", input_b, "=", result)
# Pengurangan
result =  input_a - input_b
print(input_a, "-", input_b, "=", result)
# Perkalian
result =  input_a * input_b
print(input_a, "*", input_b, "=", result)
# Pembagian
# Otomatis akan menjadi float
result =  input_a / input_b
print(input_a, "/", input_b, "=", result)

# Eksponen (pangkat) **
result = input_a ** input_b
print(input_a, "**", input_b, "=", result)

# Modulus %
result = input_a % input_b
print(input_a, "%", input_b, "=", result)

# Floor Division //
# Dibulatkan kebawah
result = input_a // input_b
print(input_a, "//", input_b, "=", result)

# Prioritas Operasi / Precedence
'''
Urutan: 
1. ()
2. eksponen
3. perkalian
4. penjumlahan
'''
