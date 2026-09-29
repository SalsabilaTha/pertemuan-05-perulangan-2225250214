# Pertemuan 05 Perulangan

Nama: Salsabila Thahira  
NIM: 2225250214  
Kelas: 3B

## Tujuan 
Pada Pertemuan 05 ini, saya mempelajari penggunaan perulangan for dan while dalam Python. Perulangan digunakan untuk menjalankan proses yang sama secara berulang sesuai dengan jumlah iterasi atau kondisi tertentu.

Selain itu, saya juga mempelajari penggunaan validasi input, seleksi if di dalam perulangan, akumulasi, serta cara melakukan pengujian dan tracing pada program.

## Cara Menjalankan 
Pastikan Python sudah terpasang dan terminal berada di dalam folder utama project.

Untuk menjalankan latihan:

python latihan/01_tabel_perkalian.py
python latihan/02_jumlah_bilangan.py
python latihan/03_validasi_input.py
python latihan/04_hitung_genap.py

Untuk menjalankan program kuis:

python kuis/kuis2_deret_aritmetika.py

## Algortima Kuis 2
Program Kuis 2 digunakan untuk menampilkan deret aritmetika dan menghitung jumlah seluruh sukunya.

Langkah-langkah algoritmanya:

1. Memasukkan nilai suku pertama a.
2. Memasukkan nilai beda d.
3. Memasukkan banyak suku n.
4. Memeriksa nilai n menggunakan while.
5. Jika n kurang dari atau sama dengan 0, program meminta input n kembali.
6. Jika n sudah positif, variabel total diatur menjadi 0.
7. Menggunakan for untuk mengulang proses sebanyak n kali.
8. Menghitung nilai setiap suku dengan a + i * d.
9. Menambahkan setiap suku ke dalam total.
10. Menampilkan nomor dan nilai setiap suku.
11. Setelah perulangan selesai, program menampilkan jumlah seluruh suku.

## Hasil Pengujian 
<table> <tr> <th>No</th> <th>Masukan</th> <th>Keluaran yang Diharapkan</th> <th>Keluaran Aktual</th> <th>Status</th> </tr>

<tr> <td>1</td> <td>a = 2, d = 3, n = 5</td> <td>Suku: 2.00, 5.00, 8.00, 11.00, 14.00<br>Jumlah = 40.00</td> <td>Suku: 2.00, 5.00, 8.00, 11.00, 14.00<br>Jumlah = 40.00</td> <td>Berhasil</td> </tr>

<tr> <td>2</td> <td>a = 10, d = -2, n = 4</td> <td>Suku: 10.00, 8.00, 6.00, 4.00<br>Jumlah = 28.00</td> <td>Suku: 10.00, 8.00, 6.00, 4.00<br>Jumlah = 28.00</td> <td>Berhasil</td> </tr>

<tr> <td>3</td> <td>a = 1.5, d = 0.5, n = 3</td> <td>Suku: 1.50, 2.00, 2.50<br>Jumlah = 6.00</td> <td>Suku: 1.50, 2.00, 2.50<br>Jumlah = 6.00</td> <td>Berhasil</td> </tr>

<tr> <td>4</td> <td>a = 2, d = 3, n = 0</td> <td>Program menolak n dan meminta input kembali</td> <td>Program menampilkan pesan bahwa n harus positif dan meminta input kembali</td> <td>Berhasil</td> </tr>

</table>

## Refleksi 
Pada pertemuan ini saya memahami bahwa for dan while digunakan untuk kebutuhan perulangan yang berbeda. for lebih mudah digunakan ketika jumlah perulangan sudah diketahui, sedangkan while digunakan ketika perulangan bergantung pada suatu kondisi.

Saya juga memahami bahwa variabel seperti total harus diinisialisasi sebelum perulangan agar hasil sebelumnya tidak terus direset. Selain itu, pada while harus ada perubahan pada variabel yang digunakan sebagai kondisi supaya perulangan dapat berhenti dan tidak menjadi infinite loop.

Dari Kuis 2, saya belajar menggabungkan while untuk validasi input dan for untuk memproses deret aritmetika. Dengan melakukan beberapa test case, saya dapat memastikan bahwa jumlah suku dan hasil penjumlahan sudah sesuai.