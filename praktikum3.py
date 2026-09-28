# TUGAS 1
def converts_temperature(value, unit):
    if unit == 'C':
        return value * 9/5 + 32
    elif unit == 'F':
        return (value - 32) * 5/9

input_value = int(input("Masukkan value : "))
input_unit = input("Masukkan unit : ")

konversi = converts_temperature(input_value, input_unit)

if input_unit == 'C':
    print("Hasil:", konversi)
else:
    print("Hasil:", konversi)


# TUGAS 2
luas_lingkaran = lambda r: 3.14 * r ** 2
input_r = float(input("\nMasukkan r : "))
print("Luas :", luas_lingkaran(input_r))