class Dagangan:
    jumlah_barang = 0
    list_barang = []

    def __init__(self, nama, stok, harga):
        self.__nama = nama
        self.__stok = stok
        self.__harga = harga

        Dagangan.jumlah_barang += 1
        Dagangan.list_barang.append((nama, stok, harga))

    @classmethod
    def lihat_barang(cls):
        print(f"Jumlah barang dagangan pada toko: {cls.jumlah_barang} buah")
        for barang in cls.list_barang:
            nama, stok, harga = barang
            print(f"{nama} seharga Rp {harga} (stok: {stok})")

    def __del__(self):
        Dagangan.jumlah_barang -= 1
        for i, barang in enumerate(Dagangan.list_barang):
            if barang[0] == self.__nama:
                print(f"{self.__nama} dihapus dari toko!")
                del Dagangan.list_barang[i]
                break


Dagangan1 = Dagangan("Galon Aqua 19L", 32, 17000)
Dagangan2 = Dagangan("Gas LPG 5 kg", 22, 88000)
Dagangan3 = Dagangan("Beras Ramos 5 kg", 13, 68000)

Dagangan.lihat_barang()

del Dagangan1

Dagangan.lihat_barang()