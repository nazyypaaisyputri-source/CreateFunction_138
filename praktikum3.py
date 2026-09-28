def converts_temperature(value, unit):
    "Fungsi konversi suhu Celsius dan Fahrenheit"
    if unit == 'C' or unit == 'c':
        return (value * 9/5) + 32
    elif unit == 'F' or unit == 'f':
        return (value - 32) * 5/9
    else:
        return None

input_value = float(input("Masukkan value : "))
input_unit = input("Masukkan unit  : ")
konversi = converts_temperature(input_value, input_unit)

# Menampilkan Hasil
if input_unit == 'C' or input_unit == 'c':
    print("Hasil konversi ke Fahrenheit:", konversi)
elif input_unit == 'F' or input_unit == 'f':
    print("Hasil konversi ke Celsius   :", konversi)
else:
    print("Unit tidak valid!")

print("\n" + "="*40 + "\n")