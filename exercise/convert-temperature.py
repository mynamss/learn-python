# Converting Celcius to other temperature


print("\nPROGRAM TO CONVERT TEMPERATURE")
print("1. Celcius")
print("2. Reamur")
print("3. Fahrenheit")
print("4. Kelvin")
num_type = input("Pilih tipe suhu(dalam angka): ")
temp_type = ""
unit = ""

# choose temperature
if num_type == "1":
    temp_type = "Celcius"
    unit = "°C"
elif num_type == "2":
    temp_type = "Reamur"
    unit = "°R"
elif num_type == "3":
    temp_type = "Fahrenheit"
    unit = "°F"
elif num_type == "4":
    temp_type = "Kelvin"
    unit = "°K"
else :
    print("Your input not match")

# print the input
print("Your choice:", temp_type)

# input number
number = float(input("Input temp: ")) 
# print the input
print("Your input:", number, unit)
print("\nRESULT:")


# Convert CELCIUS to other temp
if temp_type == "Celcius": 
    # Celcius
    print("Celcius:", number,"°C")

    # Reamur
    reamur = (4 / 5) * number
    print("Reamur:", reamur,"°R") 

    # Fahrenheit 
    fahrenheit = ((9 / 5) * number) + 32
    print("Fahrenheit:", fahrenheit,"°F")

    # Kelvin 
    kelvin = number + 273
    print("Kelvin:", kelvin,"°K")

elif temp_type == "Reamur":
    # Reamur
    print("Reamur:", number,"°R") 
    
    # Celcius
    celcius = (5 / 4) * number
    print("Celcius:", celcius,"°C") 

    # Fahrenheit 
    fahrenheit = ((9 / 4) * number) + 32
    print("Fahrenheit:", fahrenheit,"°F")

    # Kelvin 
    kelvin = ((5 / 4) * number) + 273
    print("Kelvin:", kelvin,"°K")

elif temp_type == "Fahrenheit":
    # Fahrenheit
    print("Fahrenheit:", number,"°F")
    
    # Celcius
    celcius = (5 / 9) * (number - 32)
    print("Celcius:", celcius,"°C")

    # Reamur
    reamur = (4 / 9) * (number - 32)
    print("Reamur:", reamur,"°R") 

    # Kelvin 
    kelvin = celcius + 273
    print("Kelvin:", kelvin,"°K")

elif temp_type == "Kelvin":
    # Kelvin 
    print("Kelvin:", number,"°K")
    
    # Celcius 
    celcius = number - 273
    print("Celcius:", celcius,"°C")
    
    # Reamur
    reamur = (4 / 5) * (number - 273)
    print("Reamur:", reamur,"°R") 

    # Fahrenheit 
    fahrenheit = ((9 / 5) * celcius) + 32
    print("Fahrenheit:", fahrenheit,"°F")
