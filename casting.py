# CASTING: changing from a data type to another data type

# ============INTEGER
num_int = 90

# int to float
num_float = float(num_int)
# int to string
num_str = str(num_int)
# int to boolean
# if num_int = 0 then false, otherwise num_int<0>num_int then true
num_bool = bool(num_int)

# ============FLOAT
phi = 3.14

# float to int
# Akan selalu dibulatkan ke bawah
phi_int = int(phi)
# float to string
phi_str = str(phi)
# float to boolean
phi_bool = bool(phi)

# ============BOOLEAN
status = True

# boolean to int
status_int = int(status)
# boolean to string
status_str = str(status)
# boolean to float
status_float = float(status)

# ============BOOLEAN
city = "Semarang"
# city = "10"

# string to int
# string harus angka
city_int = int(city)
# string to boolean
# false jika string kosong
city_bool = bool(city)
# string to float
# string harus angka
city_float = float(city)


print("====INTEGER====")
print("Data:", num_int, ",Type:", type(num_int))
print("Data:", num_float, ",Type:", type(num_float))
print("Data:", num_str, ",Type:", type(num_str))
print("Data:", num_bool, ",Type:", type(num_bool))
print("====FLOAT====")
print("Data:", phi, ",Type:", type(phi))
print("Data:", phi_int, ",Type:", type(phi_int))
print("Data:", phi_str, ",Type:", type(phi_str))
print("Data:", phi_bool, ",Type:", type(phi_bool))
print("====BOOLEAN====")
print("Data:", status, ",Type:", type(status))
print("Data:", status_int, ",Type:", type(status_int))
print("Data:", status_float, ",Type:", type(status_float))
print("Data:", status_str, ",Type:", type(status_str))
print("====STRING====")
print("Data:", city, ",Type:", type(city))
print("Data:", city_int, ",Type:", type(city_int))
print("Data:", city_float, ",Type:", type(city_float))
print("Data:", city_bool, ",Type:", type(city_bool))
