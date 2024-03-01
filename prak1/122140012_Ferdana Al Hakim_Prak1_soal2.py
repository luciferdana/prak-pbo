# Nilai phi
phi = 3.14

# Input jari-jari lingkaran dari pengguna
jari_jari = float(input("Jari-jari lingkaran: "))

# Validasi jari-jari tidak negatif
if jari_jari < 0:
    print("Jari-jari lingkaran tidak boleh negatif")
else:
    # Menghitung luas lingkaran
    luas = phi * (jari_jari ** 2)

    # Menghitung keliling lingkaran
    keliling = 2 * phi * jari_jari

    # Menampilkan hasil
    print("Luas lingkaran:", luas)
    print("Keliling lingkaran:", keliling)
