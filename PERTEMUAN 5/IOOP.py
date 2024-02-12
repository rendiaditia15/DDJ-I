print("\nLOOPING IN PYTHON")
print("-----------------\n")
a = 0
b = float(input("Masukan angka anda : "))
while a < b: # a < b adalah syarat
    print(a)
    a += 1 # Increment

print("\nPenggunaan Break pada Loping")
print("----------------------------\n")
a = 0
b = float(input("Masukan angka anda : "))    
while a < b: # a < b adalah syarat
    print(a)
    if a == 5: # Seleksi Kondisi
        break # Break Point
    a += 1 # Increment   

print("\nPenngunaan Continue pada Looping")
print("--------------------------------\n")
a = 0
b = float(input("Masukan angka anda : "))     
while a < b: # a > b adalah syarat
    a += 1 #Increment
    if a == 5: # Seleksi Kondisi
        continue # Continue Point
    print(a)