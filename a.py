import tkinter as tk
from tkinter import messagebox

class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 5000)

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 8000)

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def add_foglalas(self, foglalas):
        self.foglalasok.append(foglalas)

    def foglalas_ar(self, szoba, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba == szoba and foglalas.datum == datum:
                return "A foglalás már megtörtént!"
        for sz in self.szobak:
            if sz.szobaszam == szoba:
                return sz.ar

    def lemondas(self, szoba, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba == szoba and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                return "A foglalás sikeresen törölve!"
        return "Nem található ilyen foglalás!"

    def list_foglalasok(self):
        foglalasok = ""
        for foglalas in self.foglalasok:
            foglalasok += f"Szoba: {foglalas.szoba}, Dátum: {foglalas.datum}\n"
        return foglalasok

def init_hotel():
    hotel = Szalloda("Pihenő Hotel")
    hotel.add_szoba(EgyagyasSzoba("101"))
    hotel.add_szoba(EgyagyasSzoba("102"))
    hotel.add_szoba(KetagyasSzoba("201"))
    for i in range(5):
        hotel.add_foglalas(Foglalas("101", f"2024-05-0{i+1}"))
    return hotel

def foglalas_felulet():
    def foglalas():
        szoba = szoba_entry.get()
        datum = datum_entry.get()
        if szoba and datum:
            ar = hotel.foglalas_ar(szoba, datum)
            if ar:
                messagebox.showinfo("Foglalás", f"A foglalás ára: {ar} Ft")
                hotel.add_foglalas(Foglalas(szoba, datum))
            else:
                messagebox.showerror("Hiba", "A megadott szoba vagy dátum nem megfelelő!")
        else:
            messagebox.showerror("Hiba", "Kérlek töltsd ki mindkét mezőt!")

    def lemond():
        szoba = szoba_entry.get()
        datum = datum_entry.get()
        if szoba and datum:
            messagebox.showinfo("Lemondás", hotel.lemondas(szoba, datum))
        else:
            messagebox.showerror("Hiba", "Kérlek töltsd ki mindkét mezőt!")

    def listaz():
        szobak_szama = ", ".join(sz.szobaszam for sz in hotel.szobak)
        foglalasok_listaja = hotel.list_foglalasok()
        messagebox.showinfo("Foglalások", f"A szálloda összes szobája: {szobak_szama}\n\nFoglalások:\n{foglalasok_listaja}")

    hotel = init_hotel()

    root = tk.Tk()
    root.title("Szoba foglalás")

    szoba_label = tk.Label(root, text="Szoba száma:")
    szoba_label.grid(row=0, column=0, padx=10, pady=5)
    szoba_entry = tk.Entry(root)
    szoba_entry.grid(row=0, column=1, padx=10, pady=5)

    datum_label = tk.Label(root, text="Dátum (pl. 2024-05-06):")
    datum_label.grid(row=1, column=0, padx=10, pady=5)
    datum_entry = tk.Entry(root)
    datum_entry.grid(row=1, column=1, padx=10, pady=5)

    foglalas_button = tk.Button(root, text="Foglalás", command=foglalas)
    foglalas_button.grid(row=2, column=0, padx=10, pady=5)

    lemondas_button = tk.Button(root, text="Lemondás", command=lemond)
    lemondas_button.grid(row=2, column=1, padx=10, pady=5)

    listaz_button = tk.Button(root, text="Foglalások listázása", command=listaz)
    listaz_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    root.mainloop()

foglalas_felulet()
