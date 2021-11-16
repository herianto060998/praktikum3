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
- program akan membaca apakah A > B dan B > A <p>
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

pseudocode<p>
- import random memanggil file random.<p>
- n = int(input("Masukan nilai N : ")) input variabel n, tipe data integer.<p>
- for c in range(n) : looping for index c dengan jumlah perulangan sebanyak n.<p>
- b = random.uniform(.0,.5) variabel a berisikan angka acak dari 0.0 sampai 0.5.<p>
- print("Data ke : ",a,"==>",b) print data ke : a = index looping b = angka random.<p>

penjelasan<p>
- Ketikan Program import random<p>
import random memanggil file secara acak.<p>
- ketikan program n = int(input("Masukan nilai N : "))<p>
n = int(input("Masukan nilai N : ")) input variabel n, tipe data integer.<p>
- Program ketikan a=0<p>
- ketikan program untuk c dalam range(n) :<p>
for c in range(n) : looping for index c dengan jumlah perulangan sebanyak n.<p>
- ketikan program a+=1<p>
a+=1, setiap perulangan nilai akan bertambah 1<p>
- ketikan program b = random.uniform(.0,.5)<p>
b = random.uniform(.0,.5) variabel yang berisikan angka acak dari 0.0 sampai 0.5.<p>
- ketikan program print("Data ke : ",a,"==>",b)<p>
print("Data ke : ",a,"==>",b) print data ke : a = perulangan indeks b = angka acak sesuai <p>

# LABPY02
## LATIHAN 1 
### Membuat program menentukan nilai akhir

berikut ini adalah programnya <p>
![gambar11](ssgambar/ss11.png.png)

berikut ini adalah program saat running<p>
![gambar12](ssgambar/ss12.png.png)

penjelasan :<p>
- program ini adalah untuk menentukan nilai akhir dari mahasiswa dengan sistem perhitungan nilai akhir dengan sistem akhir=(int(tugas) * .2) + (int(uts) * .4) + (int(uas) * .4)<p>
- dan akan menampilkan lulus atau tidak lulus dengan sistem,  keterangan = ("TIDAK LULUS", "LULUS")[akhir > 60.0] <p>
- sistem dari sebuah perhitungan ialah menggunakan nilai dari UTS,UAS dan TUGAS yang sudah diinputkan dan jika nilai tersebut diatas dari perhitungan  nilai akhir mahasiswa akan dinyatakan LULUS tetapi jika tidak maka mahasiswa dinyatakan TIDAK LULUS <p>
 
## LATIHAN 2
### Membuat program menampilkan status gaji karyawan.

berikut ini adalah programnya<p>
![gambar13](ssgambar/ss13.png.png)

berikut ini adalah program saat running <p>
![gambar14](ssgambar/ss14.png.png)

penjelasan :<p>
- masukkan nilai inputan dari gaji <p>
- masukkan inputan apakah sudah berkeluarga dengan mengisi (Y/T) proses ini menggunakan sistem . berkeluarga = (False, True)[input("Sudah berkeluarga? (Y/T)") == "Y"]<p>
- masukkan inputtan apakah sudah memiliki rumah dengan mengisi (Y/T) proses ini menggunakan sistem .punya_rumah = (False, True)[input("Punya rumah? (Y/T)") == "Y"]<p>


## LATIHAN 3
### penggunaan kondisi OR program membandingkan 3 input bilangan, apabila penjumlahan 2 bilangan hasilnya sama dengan bilangan lainnya, maka cetak pernyataan “BENAR”

berikut ini adalah programnya <p>
![gambar15](ssgambar/ss15.png.png)

berikut ini adalah program saat running 
![gambar16](ssgambar/ss16.png.png)

penjelasan <p>
- variabel deklarasi menggunakan A,B,C 
- untuk dapat memasukkan nilai dari inputan menggunakan int contoh
a = int(input("Masukkan bilangan A: "))<p>
b = int(input("Masukkan bilangan B: "))<p>
c = int(input("Masukkan bilangan C: "))<p>
- program dari sistem penjumlahan yang digunakan yaitu if a+b == c or b+c == a or c+a == b:
- masukkan nilai inputan dari A dan B dan inputan C adalah hasil penjumlahan dari A dan B jika nilai inputan dari C tidak sesuai dengan penjumlahan A dan B maka sistem akan menampilkan tulisan SALAH tetapi jika nilai inputan C sesuai dengan hasil dari penjumlahan A dan B sistem akan menampilkan tulisan BENAR<p> 

## PROGRAM 2
### Buat repository dengan nama labspy02
### Buat program sederhana dengan input tiga buah bilangan, dari ketiga bilangan tersebut tampilkan bilangan terbesarnya. Gunakan statement if.
### Uraikan langkah atau algoritmanya pada file README.md, sertakan juga flowchart dan screenshot hasil eksekusi program. Tampilkan 3 kondisi inputan data.
### Commit dan push pada repository
### submit url repository pada classroom.

berikut ini adalah programnya <p>
![gambar17](ssgambar/ss17.png.png)

berikut ini adalah program saat running <p>
![gambar18](ssgambar/ss18.png.png)

berikut ini flowchart dari program tersebut<p>
![gambar19](ssgambar/ss19.png.png)

pseudocode:<p>
- start<p>
- gunakaan inisial a,b,c sebagai intenjer.<p>
- baca A<p>
- baca B<p>
- baca C<p>
- jika A > B dan A < C:<p>
- cetak "bilangan terbesar dari 3 inputan ", A<p>
- elif B > A dan B > C:<p>
- cetak "bilangan terbesar dari 3 inputan",B<p>
- else<p>
- cetak "bilangan terbesar dari 3 inputan", C<p>
- cetak " nilai terbesar yang diinputkan "<p>
- berhenti<p>

penjelasan:<p>
- untuk mencari bilangan terbesar dari 3 bilangan algoritmanya yang dimasukkan akan membandingkan terlebih dahulu apakah A > B.<p>
- jika A > B,maka ada 2 kadidat bilangan terbesar,yaitu A dan C sehingga perlu dilakukan pengujian yang lebih besar dari A dan C dengan membandingkan nilai B dan C. jika nilai B ternyata lebih besar dari C, maka bilangan terbesar adalah A.nilai terbesar adalah C jika ternyata C lebih besar dari A.<p>
- .jika kondisi A > B tidak terpenuhui(atau B <=A),maka 2 kadidat bilangan terbesar adalah B dan C.jika nilai C ternyata lebih kecil dari A,maka B adalah nilai terbesar,sedangkan jika C yang lebih besar dari B ,maka yang terbesar adalah C.<p>

# LABPY03
## LATIHAN 1 
### Tampilkan n bilangan acak yang lebih kecil dari 0.5.
### nilai n diisi pada saat runtime
### anda bisa menggunakan kombinasi while dan for untuk menyelesaikannya
### gunakan fungsi random() yang dapat diimport terlebih dahulu

berikut ini adalah programnya <p>
![gambar8](ssgambar/ss8.png.png)

berikut ini adalah program saat running<p>
![gambar9](ssgambar/ss9.png.png)

berikut ini adalah flowchart dari program tersebut<p>
![gambar10](ssgambar/ss10.png.png)

peseudocode <p>
- import random memanggil file random.<p>
- n = int(input("Masukan nilai N : ")) input variabel n, tipe data integer.<p>
- for c in range(n) : looping for index c dengan jumlah perulangan sebanyak n.<p>
- b = random.uniform(.0,.5) variabel a berisikan angka acak dari 0.0 sampai 0.5.<p>
- print("Data ke : ",a,"==>",b) print data ke : a = index looping b = angka random .<p>

penjelasan<p>
- Ketikan Program import random<p>
import random memanggil file secara acak.<p>
- ketikan program n = int(input("Masukan nilai N : "))<p>
n = int(input("Masukan nilai N : ")) input variabel n, tipe data integer.<p>
- Program ketikan a=0<p>
- ketikan program untuk c dalam range(n) :<p>
for c in range(n) : looping for index c dengan jumlah perulangan sebanyak n.<p>
- ketikan program a+=1<p>
a+=1, setiap perulangan nilai akan bertambah 1<p>
- ketikan program b = random.uniform(.0,.5)<p>
b = random.uniform(.0,.5) variabel yang berisikan angka acak dari 0.0 sampai 0.5.<p>
- ketikan program print("Data ke : ",a,"==>",b)<p>
print("Data ke : ",a,"==>",b) print data ke : a = perulangan indeks b = angka acak sesuai ><p>

## LATIHAN 2
### Buat program untuk menampilkan bilangan terbesar dari n buah data yang diinputkan. Masukkan angka 0 untuk berhenti.

berikut ini adalah programnya <p>
![gambar20](ssgambar/ss20.png.png)

berikut ini adalah program saat running<p>
![gambar21](ssgambar/ss21.png.png)

berikut ini flowchart dari program<p>
![gambar22](ssgambar/ss22.png.png)

pseudocode<p>
- maks=0 variabel maks diisi 0.<p>
- while True : perulangan while dengan syarat True.<p>
- if max < a: max = suatu proses jika untuk mencari nilai terbesar.<p>
- a = int(input('Masukan bilangan = ')) input nilai a dengan tipe data integer.<p>
- if a==0 : break jika inputan diisi angka 0 maka break alias berhenti looping.<p>
- print('Bilangan terbesarnya adalah = ',max) print nilai terbesar, variabel max<p>

penjelasan<p>
- Ketikan Program maks= 0<p>
max= 0 kode max disini untuk menentukan nilai max nya dalah 0<p>
- Ketikan Program saat benar :<p>
while true: Untuk perulangan hingga waktu yang tidak ditentukan atau selamanya<p>
- Ketikan Program a=int(input("Masukan Bilangan :"))<p>
a=int(input("Masukan Bilangan :")) a untuk menginput tipe data interger ( bilangan bulat )<p>
Program ketikan jika max < a<p>
- Ketikan Program max=a<p>
if max < a max=a jika max kurang dari a maka max = a<p>
- Program ketikan jika a==0 :<p>
- Ketikan Program istirahat<p>
if a==0: break jika a= 0 maka akan berhenti dengan syarat break yang terpenuhi<p>
- Ketikan Program print("Bilangan Tebesarnya Adalah :", max)<p>
print("Bilangan Tebesarnya Adalah :", max)*Bilangan Tebesar Adalah : Nilai maxiumnya<p>

## PROGRAM 1
### Buat repository baru labpy03
### Masukkan latihan1.py dan latihan2.py ke dalam repository.
### Buat program sederhana dengan perulangan: program1.py Seorang pengusaha menginvestasikan uangnya untuk memulai usahanya dengan modal awal 100 juta, pada bulan pertama dan kedua belum mendapatkan laba. pada bulan ketiga baru mulai mendapatkan laba sebesar 1% dan pada bulan ke 5, pendapatan meningkat 5%, selanjutnya pada bulan ke 8 mengalami penurunan keuntungan sebesar 2%, sehingga laba menjadi 3%. Hitung total keuntungan selama 8 bulan berjalan usahanya.
### buat file README.md, yang berisi penjelasan alur algoritma program latihan1.py, latihan2.py, dan program1.py beserta screenshot hasilnya.
### kemudian commit dan push ke repository (github)
### kirim url repository ke classroom.

berikut ini adalah programnya <p>
![gambar23](ssgambar/ss23.png.png)

berikut ini adalah program saat running<p>
![gambar24](ssgambar/ss24.png.png)

berikut ini flowchart dari program<p>
![gambar25](ssgambar/ss25.png.png)

pseudocode<p>
- x=100000000 modal 100.000.000, variabel x.<p>
- sum=0 variabel untuk menjumlah total laba.<p>
- y=0 variabel untuk masa bulan.<p>
- lb = [int(0), int(0), int(a) * .1, int(a) * .1, int(a) * .5, int(a) * .5, int(a) * .5, int(a) * .2] variabel untuk jumlah laba perbulan, dipisahkan dengan koma dan tipe data integer.<p>
- for i in lb : looping for index i dengan mengambil data dari lb.<p>
- sum=sum+i rumus untuk menghitung total laba perbulan.<p>
- y+=1 masa bulan, tiap looping menambah 1.<p>
- print('Laba Bulan Ke-', y ,'Sebesar :',y) print : y = ambil masa bulan, i = ambil dari data yang ada di dalam lb.<p>
- print('TOTAL LABA YANG DI DAPAT ADALAH :',sum) print total laba.<p>

penjelasan<p>
- program ketikan<p>
 x=100000000 modal 100.000.000, variabel x.<p>
- Ketikan jumlah program=0<p>
sum=0 kode sum disini untuk menentukan jumlah total laba<p>
- program kapan<p>
y=0 y= untuk variabel masa bulan<p>
- ketikan program lb = [int(0), int(0), int(x) * .1, int(x) * .1, int(x) * .5, int(x) * .5, int(x )* .5, int(x) * .2]<p>
lb = [int(0), int(0), int(x) * .1, int(x) * .1, int(x) * .5, int(x) * .5, int(x )* .5, int(x) * .2] Untuk Mendeklarasikan presentase laba tiap bulan dan di kali dengan x atau data inputan modal investasi yaitu 100000000<p>
- ketikan program print("Modal Awal Seorang Pengusaha :',x")<p>
print(" Modal Awal Seorang Pengusaha :',x") menyaksikan kalimat *Modal Awal : dan data yang berisi di x yaitu 100000000<p>
- ketikan program untuk i in lb :<p>
for i in lb : looping for index i dengan mengambil data dari lb.<p>
- ketikan program sum=sum+i<p>
sum=sum+i rumus untuk menghitung total laba perbulan.<p>
- kapann program y+1<p>
 y+=1, masa bulan tiap perulangan menambah 1.<p>
- print('Laba Bulan Ke-', y ,'Sebesar :',i)<p>
print('Laba Bulan Ke-', y ,'Sebesar :',i) print : y = ambil masa bulan, i = ambil dari data yang ada di dalam lb.<p>
- print('JUMLAH LABA YANG DI DAPAT ADALAH :',jumlah)<p>
 print('TOTAL LABA YANG DI DAPAT ADALAH :',jumlah) print total laba.<p>



