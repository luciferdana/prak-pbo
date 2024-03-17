class Mahasiswa:
    def __init__(self, nim, nama, angkatan, isMahasiswa=True):
        self.__nim = nim
        self.__nama = nama
        self.angkatan = angkatan
        self.isMahasiswa = isMahasiswa

    def get_nim(self):
        return self.__nim

    def set_nim(self, nim):
        self.__nim = nim

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        self.__nama = nama

    def info_mahasiswa(self):
        return f"NIM: {self.__nim}\nNama: {self.__nama}\nAngkatan: {self.angkatan}\nStatus: {'Mahasiswa' if self.isMahasiswa else 'Bukan Mahasiswa'}"

    def is_lulus(self, sks):
        if sks >= 144:
            return True
        else:
            return False

    def hitung_sks(self, ipk):
        return ipk

    # Getter untuk nim
    def get_nim(self):
        return self.__nim

    # Setter untuk nim
    def set_nim(self, nim):
        self.__nim = nim

    # Getter untuk nama
    def get_nama(self):
        return self.__nama

    # Setter untuk nama
    def set_nama(self, nama):
        self.__nama = nama


mahasiswa1 = Mahasiswa("122140012", "Ferdana", 2022)
print("Mahasiswa 1:")
print(mahasiswa1.info_mahasiswa())
print("")

mahasiswa2 = Mahasiswa("120140088", "Bayu", 2022)
mahasiswa2.isMahasiswa = False
print("Mahasiswa 2:")
print(mahasiswa2.info_mahasiswa())
print("")

print("Apakah Mahasiswa 1 lulus? ", mahasiswa1.is_lulus(61))
print("Apakah Mahasiswa 2 lulus? ", mahasiswa2.is_lulus(144))
print("")

print("IPK Mahasiswa 1 : ", mahasiswa1.hitung_sks(3.35))
print("IPK Mahasiswa 2 : ", mahasiswa2.hitung_sks(3.5))

# Penggunaan setter dan getter
print("\nMenggunakan setter dan getter:")
print("NIM Mahasiswa 1:", mahasiswa1.get_nim())
mahasiswa1.set_nim("122140011")  # Mengubah NIM Mahasiswa 1
print("NIM Mahasiswa 1 setelah diubah:", mahasiswa1.get_nim())

print("Nama Mahasiswa 2:", mahasiswa2.get_nama())
mahasiswa2.set_nama("Bambang")  # Mengubah Nama Mahasiswa 2
print("Nama Mahasiswa 2 setelah diubah:", mahasiswa2.get_nama())
