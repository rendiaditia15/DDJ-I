belanja = [
    {"produk":"baju", "jumlah":20},
    {"produk":"celana", "jumlah":15},
    {"produk":"sepatu", "jumlah":20},
    {"produk":"tas", "jumlah":10},
    ]

total_belanjaan = 0
for item in belanja:
    total_belanjaan += item["jumlah"]

print("Total Belanjaan : ", total_belanjaan)
