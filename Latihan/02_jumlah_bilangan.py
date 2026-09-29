# Input: menerima bilangan bulat n
# Proses: menjumlahkan bilangan dari 1 sampai n
# Output: menampilkan hasil penjumlahan

n = int(input("n: "))

total = 0

for i in range(1, n + 1):
    total += i

print(f"Jumlah = {total}")