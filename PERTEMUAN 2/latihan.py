Olahraga = ("Voly", "Senam", "Badminton", "Lompat", "Basket", "Futsal")

Olahraga_list = list(Olahraga)
Olahraga_list.append("Tenis")
print("update list = ", Olahraga_list)
del Olahraga_list[3]
print("hapus list = ", Olahraga_list)
Olahraga_list[5] = "Sepak Bola"
print("update = ", Olahraga_list)
Olahraga_tuple = tuple(Olahraga_list)