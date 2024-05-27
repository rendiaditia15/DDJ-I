import tkinter as tk
from tkinter import messagebox

class Produk:
    def __init__(self, nama, harga):  
        self.nama = nama
        self.harga = harga

class KeranjangBelanja:
    def __init__(self):  
        self.items = []

    def tambah_produk(self, produk, jumlah):
        self.items.append((produk, jumlah))

    def hapus_produk(self, index):
        del self.items[index]

    def hapus_semua_produk(self):  
        self.items.clear()

    def hitung_total(self):
        total = sum(produk.harga * jumlah for produk, jumlah in self.items)
        return total

class AplikasiECommerce:
    def __init__(self, master):  
        self.master = master
        self.master.title("RV.Store")
        self.master.configure(bg="#f0f0f0")
        self.font = ("Arial", 12)
        self.keranjang = KeranjangBelanja()
        self.daftar_produk = [
            Produk("Jaket Bomber On The Road", 150000),
            Produk("Jaket Bomber X-Urban", 200000),
            Produk("Jaket Smith", 300000),
            Produk("Celana Oblong", 180000),
            Produk("Celana Ripped", 200000),
            Produk("Celana Katun", 250000),
            Produk("Celana Pendek", 300000),
        ]
        self.label_produk = tk.Label(master, text="Daftar Produk:", bg="#f0f0f0", font=self.font)
        self.label_produk.grid(row=0, column=0)
        self.label_jumlah = tk.Label(master, text="Jumlah:", bg="#f0f0f0", font=self.font)
        self.label_jumlah.grid(row=0, column=1)
        self.listbox_produk = []
        self.entry_jumlah = []
        for i, produk in enumerate(self.daftar_produk):
            label_produk = tk.Label(master, text=f"{produk.nama} - Rp {produk.harga}", bg="#f0f0f0", font=self.font)
            label_produk.grid(row=i+1, column=0)
            entry_jumlah = tk.Entry(master, width=10, font=self.font)
            entry_jumlah.grid(row=i+1, column=1)
            self.listbox_produk.append(label_produk)
            self.entry_jumlah.append(entry_jumlah)
        self.button_tambah = tk.Button(master, text="Tambah ke Keranjang", command=self.tambah_ke_keranjang, font=self.font)
        self.button_tambah.grid(row=len(self.daftar_produk)+1, column=0, columnspan=2, pady=5)
        self.label_keranjang = tk.Label(master, text="Keranjang Belanja:", bg="#f0f0f0", font=self.font)
        self.label_keranjang.grid(row=0, column=2)
        self.listbox_keranjang = tk.Listbox(master, width=40, height=10, font=self.font)
        self.listbox_keranjang.grid(row=1, column=2, rowspan=len(self.daftar_produk)+1)
        self.label_total = tk.Label(master, text="Total Belanja:", bg="#f0f0f0", font=self.font)
        self.label_total.grid(row=len(self.daftar_produk)+2, column=1, sticky=tk.E)
        self.label_total_nilai = tk.Label(master, text="Rp 0", bg="#f0f0f0", font=self.font)
        self.label_total_nilai.grid(row=len(self.daftar_produk)+2, column=2, sticky=tk.W)
        self.label_alamat = tk.Label(master, text="Alamat Pengiriman:", bg="#f0f0f0", font=self.font)
        self.label_alamat.grid(row=len(self.daftar_produk)+3, column=0)
        self.entry_alamat = tk.Entry(master, width=40, font=self.font)
        self.entry_alamat.grid(row=len(self.daftar_produk)+4, column=0, columnspan=2, pady=5)
        self.label_uang_pembeli = tk.Label(master, text="Uang Pembeli:", bg="#f0f0f0", font=self.font)
        self.label_uang_pembeli.grid(row=len(self.daftar_produk)+5, column=0)
        self.entry_uang_pembeli = tk.Entry(master, width=20, font=self.font)
        self.entry_uang_pembeli.grid(row=len(self.daftar_produk)+5, column=1)
        self.button_checkout = tk.Button(master, text="Checkout", command=self.checkout, font=self.font)
        self.button_checkout.grid(row=len(self.daftar_produk)+7, columnspan=2, pady=10)
        self.listbox_keranjang.bind("<Double-Button-1>", self.hapus_produk_dari_keranjang)

    def tambah_ke_keranjang(self):
        for i, entry_jumlah in enumerate(self.entry_jumlah):
            jumlah = entry_jumlah.get()
            if jumlah.isdigit() and int(jumlah) > 0:
                produk = self.daftar_produk[i]
                self.keranjang.tambah_produk(produk, int(jumlah))
                self.listbox_keranjang.insert(tk.END, f"{produk.nama} - {jumlah} x Rp {produk.harga}")
        total = self.keranjang.hitung_total()
        self.label_total_nilai.config(text=f"Rp {total}")

    def checkout(self):
        alamat = self.entry_alamat.get()
        uang_pembeli = self.entry_uang_pembeli.get()
        if not alamat:
            messagebox.showwarning("Peringatan", "Masukkan alamat pengiriman terlebih dahulu.")
            return
        if not uang_pembeli.isdigit() or int(uang_pembeli) <= 0:
            messagebox.showwarning("Peringatan", "Masukkan uang pembeli yang valid.")
            return
        total = self.keranjang.hitung_total()
        uang_pembeli = int(uang_pembeli)
        if total > 0:
            kembali = uang_pembeli - total
            if kembali >= 0:
                detail_belanja = ""
                for produk, jumlah in self.keranjang.items:
                    detail_belanja += f"{produk.nama} - {jumlah} x Rp {produk.harga}\n"
                messagebox.showinfo("Checkout", f"Alamat Pengiriman: {alamat}\n\nDetail Belanja:\n{detail_belanja}\nTotal belanja Anda: Rp {total}\nUang Pembeli: Rp {uang_pembeli}\nKembali: Rp {kembali}\nTerima kasih telah berbelanja!")
                self.keranjang.hapus_semua_produk()
                self.listbox_keranjang.delete(0, tk.END)
                self.label_total_nilai.config(text="Rp 0")
                self.entry_alamat.delete(0, tk.END)
                self.entry_uang_pembeli.delete(0, tk.END)
                self.label_kembali_nilai.config(text="Rp 0")
            else:
                messagebox.showwarning("Peringatan", "Uang pembeli tidak mencukupi.")
        else:
            messagebox.showwarning("Peringatan", "Keranjang belanja Anda kosong. Tambahkan produk terlebih dahulu.")

    def hapus_produk_dari_keranjang(self, event):
        index = self.listbox_keranjang.curselection()
        if index:
            self.keranjang.hapus_produk(index[0])
            self.listbox_keranjang.delete(index)

def main():
    root = tk.Tk()
    app = AplikasiECommerce(root)
    root.mainloop()

if __name__ == "__main__":
    main()