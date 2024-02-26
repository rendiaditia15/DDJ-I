nilai_siswa =[
    {"jumlah":85},
    {"jumlah":90},
    {"jumlah":78},
    {"jumlah":92},
    {"jumlah":88},
    ]

total_siswa=0
for item in nilai_siswa:
    total_siswa += item["jumlah"]
    
print("total siswa : ", total_siswa)

