# Input: menerima suku pertama (a), beda (d), dan banyak suku (n)
# Proses: memvalidasi n agar merupakan bilangan bulat positif
# Proses: menghitung dan menjumlahkan setiap suku
# Output: menampilkan nomor dan nilai setiap suku
# Output: menampilkan jumlah seluruh suku

print("Deret Aritmetika")

a = float(input("Suku pertama a: "))
d = float(input("Beda d: "))

n = int(input("Banyak suku n: "))

while n <= 0:
    print("n harus bilangan bulat positif.")
    n = int(input("Banyak suku n: "))

total = 0

for i in range(n):
    suku = a + i * d
    total += suku
    print(f"Suku ke-{i + 1}: {suku:.2f}")

print(f"Jumlah = {total:.2f}")