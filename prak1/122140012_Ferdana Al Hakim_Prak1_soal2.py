phi = 3.14

jari_jari = float(input("Jari-jari lingkaran: "))
\
if jari_jari < 0:
    print("Jari-jari lingkaran tidak boleh negatif")
else:
    luas = phi * (jari_jari ** 2)

    keliling = 2 * phi * jari_jari

    print("Luas lingkaran:", luas)
    print("Keliling lingkaran:", keliling)
