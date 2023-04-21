import json

class NotDefteri:
    def __init__(self):
        self.data_file = 'data.json'
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.data_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_data(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f)

    def add_not(self, ders, notlar):
        if ders not in self.data:
            self.data[ders] = []
        self.data[ders].append(notlar)
        self.save_data()

    def get_notlar(self, ders):
        if ders in self.data:
            return self.data[ders]
        else:
            return None

    def tüm_notlar(self):
        return self.data

def menu():
    print("1. Yeni not ekle")
    print("2. Ders notlarını göster")
    print("3. Tüm notları göster")
    print("4. Çıkış")

def main():
    nd = NotDefteri()
    while True:
        menu()
        secim = input("Seçim yapınız: ")
        if secim == '1':
            ders = input("Ders adı: ")
            notlar = input("Notlar: ")
            nd.add_not(ders, notlar)
        elif secim == '2':
            ders = input("Ders adı: ")
            notlar = nd.get_notlar(ders)
            if notlar:
                for n in notlar:
                    print(n)
            else:
                print("Ders bulunamadı")
        elif secim == '3':
            for ders, notlar in nd.tüm_notlar().items():
                print(ders)
                for n in notlar:
                    print(f"- {n}")
        elif secim == '4':
            break
        else:
            print("Geçersiz seçim")

if __name__ == '__main__':
    main()
