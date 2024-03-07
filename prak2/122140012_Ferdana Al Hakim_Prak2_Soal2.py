import random

class TebakNegara:
    def __init__(self):
        self.negara = {
            "Indonesia": "Jakarta",
            "Amerika Serikat": "Washington D.C.",
            "Jepang": "Tokyo",
            "Prancis": "Paris",
            "Inggris": "London",
            "Italia": "Roma",
            "Jerman": "Berlin",
            "Australia": "Canberra",
            "Brasil": "Brasilia",
            "Kanada": "Ottawa",
            "Thailand": "Bangkok",
            "Spanyol": "Madrid",
            "Argentina": "Buenos Aires",
            "Rusia": "Moskow",
            "India": "New Delhi",
            "China": "Beijing",
            "Mesir": "Kairo",
            "Afrika Selatan": "Pretoria",
            "Nigeria": "Abuja",
            "Swedia": "Stockholm",
            "Belanda": "Amsterdam"
        }

    def __del__(self):
        print("Terima kasih telah bermain kuis Tebak Negara!")

    def start_game(self):
        print("=== Selamat Datang di Kuis Tebak Negara ===")
        print("Tebak ibu kota negara berikut ini:")
        negara = random.choice(list(self.negara.keys()))
        jawaban_benar = self.negara[negara]
        jawaban_user = input(f"Ibu kota negara {negara} adalah: ").strip()

        if jawaban_user.lower() == jawaban_benar.lower():
            print("Selamat! Jawaban kamu benar.")
        else:
            print(f"Maaf, jawaban kamu salah. Ibu kota negara {negara} adalah {jawaban_benar}.")

    def main_menu(self):
        print("=== Kuis Tebak Negara ===")
        print("1. Mulai Permainan")
        print("2. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            self.start_game()
        elif pilihan == "2":
            del self
            exit()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def main():
    game = TebakNegara()
    while True:
        game.main_menu()

if __name__ == "__main__":
    main()
