belanja = [
    {"buah":"semangka", "harga":12000},
    {"buah":"nanas", "harga":10000},
    {"buah":"pepaya", "harga":12000},
    ]

total_belanjaan = 0
for item in belanja:
    total_belanjaan += item["harga"]

print("Total Belanjaan : ", total_belanjaan)
