belanja = [
    {"buah":"Apel", "harga":5000*10},
    {"buah":"jeruk", "harga":3000*5},
    {"buah":"mangga", "harga":7000*7},
    {"buah":"Pisang", "harga":2000*20},
    {"buah":"Semangka", "harga":15000*1},
    ]

total_belanjaan = 0 
for item in belanja:
    total_belanjaan += item["harga"]

print("Total Belanja : ", total_belanjaan)