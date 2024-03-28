import math

class Bentuk:
    def hitungLuas(self):
        pass

class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def hitungLuas(self):
        return self.sisi ** 2

class Lingkaran(Bentuk):
    def __init__(self, radius):
        self.radius = radius

    def hitungLuas(self):
        return math.pi * self.radius ** 2


def hitung_dan_cetak_luas(bentuk):
    luas = bentuk.hitungLuas()
    print(f"Luas: {luas}")


persegi = Persegi(5)
lingkaran = Lingkaran(3)

hitung_dan_cetak_luas(persegi)  
hitung_dan_cetak_luas(lingkaran)
