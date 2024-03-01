batas_bawah = int(input("Batas bawah: "))
batas_atas = int(input("Batas atas: "))

if batas_bawah < 0 or batas_atas < 0:
    print("Batas bawah dan atas yang dimasukkan tidak boleh di bawah Nol")
else:

    jumlah_ganjil = 0

    for i in range(batas_bawah, batas_atas):
        
        if i % 2 != 0:
            print(i)
            jumlah_ganjil += i

    print("Total:", jumlah_ganjil)