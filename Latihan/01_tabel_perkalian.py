# Input: menerima satu bilangan bulat n
# Proses: mengalikan n dengan angka 1 sampai 10
# Output: menampilkan hasil perkalian

n = int(input("Bilangan: "))

for i in range(1, 11):
    hasil = n * i
    print(f"{n} x {i} = {hasil}")