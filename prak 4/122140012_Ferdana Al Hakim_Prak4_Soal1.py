class Hewan:
    def __init__(self, nama, jenis_kelamin):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin

    def bersuara(self):
        pass

    def makan(self):
        pass

    def minum(self):
        pass


class Kucing(Hewan):
    def bersuara(self):
        print(f"Kucing {self.nama} bersuara: Meong!")

    def makan(self):
        print(f"Kucing {self.nama} sedang makan: ikan")

    def minum(self):
        print(f"Kucing {self.nama} sedang minum: susu")


class Anjing(Hewan):
    def bersuara(self):
        print(f"Anjing {self.nama} bersuara: Guk Guk!")

    def makan(self):
        print(f"Anjing {self.nama} sedang makan: daging")

    def minum(self):
        print(f"Anjing {self.nama} sedang minum: air")


hewan1 = Kucing("Kiki", "Betina")
hewan2 = Anjing("Ichi", "Jantan")

print(hewan1.nama)  # Output: Kiki
print(hewan2.nama)  # Output: Ichi

hewan1.bersuara()  # Output: Kucing Kiki bersuara: Meong!
hewan1.makan()  # Output: Kucing Kiki sedang makan: ikan
hewan1.minum()  # Output: Kucing Kiki sedang minum: susu

hewan2.bersuara()  # Output: Anjing Ichi bersuara: Guk Guk!
hewan2.makan()  # Output: Anjing Ichi sedang makan: daging
hewan2.minum()  # Output: Anjing Ichi sedang minum: air
