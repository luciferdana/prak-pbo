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
        print(f"Kucing {self.nama} bersuara: Miaww!")

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


hewan1 = Kucing("Jarwo", "Betina")
hewan2 = Anjing("Dini", "Jantan")

print(hewan1.nama)  
print(hewan2.nama)  

hewan1.bersuara()  
hewan1.makan()  
hewan1.minum()  

hewan2.bersuara()  
hewan2.makan() 
hewan2.minum()  
