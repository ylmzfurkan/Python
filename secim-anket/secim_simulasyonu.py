from tkinter import messagebox
import tkinter as tk
from PIL import Image, ImageTk

class SecimSimulasyonu:
    def __init__(self, master):
        self.master = master
        self.master.title('Cumhurbaşkanlığı Seçim Simülasyonu')

        # Adayların isimleri ve oy sayıları
        self.adaylar = {"R.Tayyip Erdoğan": tk.IntVar(), "Kemal Kılıçdaroğlu": tk.IntVar(), "Sinan Oğan": tk.IntVar()}

        # Adayların fotoğrafları
        self.aday_fotograflari = {"R.Tayyip Erdoğan": ImageTk.PhotoImage(Image.open("secim-anket/aday1.jpeg").resize((300, 300))),
                                  "Kemal Kılıçdaroğlu": ImageTk.PhotoImage(Image.open("secim-anket/aday2.jpeg").resize((300, 300))),
                                  "Sinan Oğan": ImageTk.PhotoImage(Image.open("secim-anket/aday3.jpeg").resize((300, 300)))}
        row = 0
        for aday, fotograflar in zip(self.adaylar.items(), self.aday_fotograflari.items()):
            aday_ismi, oy_sayisi = aday
            fotograflar_ismi, foto = fotograflar

            # Aday fotoğraflarını ekleme
            tk.Label(master, image=foto).grid(row=row, column=0)
            tk.Label(master, text=aday_ismi, font=("Arial", 14)).grid(row=row+1, column=0)

            # Oy butonlarını ekleme
            tk.Button(master, text="Oy Ver", command=lambda aday=aday_ismi: self.oy_ver(aday)).grid(row=row, column=1)

            # Oy sayısını gösterme
            tk.Label(master, textvariable=oy_sayisi).grid(row=row, column=2)

            row += 2

        # Kazananı gösterme butonu
        tk.Button(master, text="Kazananı Göster", command=self.kazanani_bul).grid(row=row, column=0, columnspan=3)

    def oy_ver(self, aday):
        self.adaylar[aday].set(self.adaylar[aday].get() + 1)

    def kazanani_bul(self):
        kazanan_aday = max(self.adaylar, key=lambda k: self.adaylar[k].get())
        messagebox.showinfo("Seçim Sonuçları", f"Seçimlerin kazananı: {kazanan_aday}")

root = tk.Tk()
app = SecimSimulasyonu(root)
root.mainloop()