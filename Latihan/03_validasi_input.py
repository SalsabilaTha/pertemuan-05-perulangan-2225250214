# Input: menerima nilai ujian dari 0 sampai 100
# Proses: memeriksa apakah nilai berada di luar rentang 0 sampai 100
# Output: menampilkan nilai yang sudah valid

nilai = float(input("Nilai 0-100: "))

while nilai < 0 or nilai > 100:
    print("Nilai tidak valid.")
    nilai = float(input("Nilai 0-100: "))

print(f"Nilai diterima: {nilai}")