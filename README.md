# TUGAS LAB 2 
## LAB 2 - 1 
### Program sederhada dengan input 2 buah bilangan, kemudian tentukan bilangan terbesar dari kedua bilangan.

berikut ini adalah tampilan programnya <p>
![gambar1](ssgambar/ss1.png.png)

berikut adalah saat program runnning <p>
![gambar2](ssgambar/ss2.png.png)

berikut adalah flowchart dari program tersebut<p>
![gambar3](ssgambar/ss3.png.png)

pseudocode:<p>
- A dan B sebagai variabel int dari inputan<p>
- masukkan nilai dari A dan B <p>
- program akan membaca apakah A > B dan B > A 
- sistem akan menampilkan nilai terbesar dari antara variabel A atau B jika A > B atau B > A<p> 

penjelasan:<p>
- variabel pendeklerasiaan untuk sistem penginputan saat running <p>
A=int(input("Masukkan nilai A : "))<p>
B=int(input("Masukkan nilai B : "))<p>
- untuk mencari bilangan terbesar dari 2 bilangan algoritmanya yang dimasukkan akan membandingkan terlebih dahulu apakah A > B dan B < A<p>
- jika A > B maka sistem akan menampilkan nilai dari A <p>
- tetapi jika nilai B > A maka sistem akan menampilkan nilai dari B <p>


## LAB 2 - 2
### program untuk mengurutkan data berdasarkan input sejumlah data (minimal 3 variable input atau lebih),kemudian tampilkan hasilnya secara berurutan mulai dari data terkecil.

berikut ini adalah tampilan dari programnya <p>
![gambar4](ssgambar/ss4.png.png)

berikut ini adalah tampilan dari programnya<p>
![gambar5](ssgambar/ss5.png.png)

penjelasan :<p>

- A,B,C,D sebagai variabel dari sebuah inputan 
- untuk memasukkan nilai dari sebuah inputan kita menggunakan int dan input contoh :<p>
A=int(input("bilangan ke-1:"))<p>
B=int(input("bilangan ke-2:"))<p>
C=int(input("bilangan ke-3:"))<p>
D=int(input("bilangan ke-4:"))<p>
- masukkan nilai dari A,B,C,D <p>
- luas = [ A, B, C, D,] adalah sebuah perintah bahwa pemisah dari hasil inputan adalah koma  
- untuk membuat agar hasil dari inputan berurutan mulai dari data terkecil menggunakan sorted

# TUGAS LAB 3
## Lab 3 - 1
### Buat program dengan perulangan bertingkat (nested) for.
berikut ini adalah programnya <p>
![gambar6](ssgambar/ss6.png.png)

berikut adalah saat program running<p>
![gambar7](ssgambar/ss7.png.png)

penjelasan:<p>
- Variabel Pendeklarasian<p>
baris = 10<p>
kolom = baris <p>
- untuk perulangan baris dan kolom menggunakan nested for <p>
for bar in range(baris):<p>
    for col in range(kolom):<p>
        tab = bar+col<p>
- untuk menampilkan hasil dari perulangan <p>
1.agar terlihat rapi menggunakan format string rata ke kanan sebanyak 6 karakter<p>
2.agar tidak membuat baris baru mengunakan end=''(baris)<p>
3.penggunaan print () untuk membuat baris baru kolom <p>
print("{0:>6}".format(tab), end='')<p>
    print()<p>

## Lab 3 - 2
### Tampilkan n bilangan acak yang lebih kecil dari 0.5.
### nilai n diisi pada saat runtime
### anda bisa menggunakan kombinasi while dan for untuk menyelesaikannya

berikut ini adalah programnya<p>
![gambar8](ssgambar/ss8.png.png)

berikut ini adalah program saat running<p>
![gambar9](ssgambar/ss9.png.png)

berikut ini flowchart dari program tersebut<p>
![gambar10](ssgambar/ss10.png.png)

penjelasan<p>
- menggunakan  modul import random untuk membuat bilangan acak<p>
- Untuk menentukan jumlah input yang diinginkan dan konversi ke dalam bilangan bulat (integer) yang dimasukan ke variabel(n), n = int(input("masukkan nilai;"))<p>
- untuk membuat urutan dari inputan tersebut mengunakan a=0 ,a+=1 yang menandakan urutan tersebut dimulai dari 1 dan ditambah 1 <p>
- untuk membuat rentang retret yang diinputkan oleh variabel (n) ,for c in range (n): <p>
- Untuk menampilkan urutan data sesuai jumlah inputan dengan hasil di bawah 0.5<p>
    a+= 1<p>
   b = random.uniform(.0,.5)<p>
   print('data ke:', a, '==>', b)<p>




