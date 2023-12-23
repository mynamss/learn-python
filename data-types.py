# integer
int_num = 10
# float
float_num = 3.14
# string
str_country = "Indonesia"
# boolean
is_active = True

# --------- TIPE DATA KHUSUS
# complex
data_complex = complex(5,6)

# tipe data dari bahada C
from ctypes import c_double, c_long, c_short
data_c_double = c_double(10.5)

# print
print("Nilai:", int_num, "bertipe:", type(int_num))
print("Nilai:", float_num, "bertipe:", type(float_num))
print("Nilai:", str_country, "bertipe:", type(str_country))
print("Nilai:", is_active, "bertipe:", type(is_active))
print("Nilai:", data_complex, "bertipe:", type(data_complex))
print("Nilai:", data_c_double, "bertipe:", type(data_c_double))