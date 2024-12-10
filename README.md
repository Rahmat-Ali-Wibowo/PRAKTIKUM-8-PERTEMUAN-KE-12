# Program Mengelola Daftar Nilai Mahasiswa

## Deskripsi
Program ini memungkinkan pengguna untuk mengelola daftar nilai mahasiswa menggunakan class. Pengguna dapat menambah, mengubah, menghapus, dan menampilkan data mahasiswa. Nilai akhir dihitung berdasarkan komponen nilai tugas, UTS, dan UAS.

## Diagram Class

```plaintext
+-----------------------------------+
|           DaftarNilaiMahasiswa    |
+-----------------------------------+
| - data_mahasiswa: dict            |
+-----------------------------------+
| + tambah(): void                  |
| + tampilkan(): void               |
| + hapus(nama: str): void          |
| + ubah(nama: str): void           |
+-----------------------------------+

## Flowchart

```plaintext
+------------------------------------------------------+
| Mulai                                                 |
+------------------------------------------------------+
          |
          v
+----------------------------+
| Inisialisasi class         |
| DaftarNilaiMahasiswa       |
+----------------------------+
          |
          v
+----------------------------+
| Tampilkan menu pilihan     |
| (Tambah, Tampilkan, Hapus, |
| Ubah, Keluar)              |
+----------------------------+
          |
          v
+----------------------------+
| Input pilihan pengguna     |
| (1/2/3/4/5)                |
+----------------------------+
          |
          v
+-----------------------------+
| Apakah pilihan '1'?         |
| (Tambah Data)               |
+-------------+---------------+
              |Tidak                       |Ya
              v                            v
+-------------+-------------+  +-----------+-----------+
| Lanjutkan ke pilihan lain |  | Input nama, tugas, UTS,|
| (2/3/4/5)                 |  | UAS                   |
+-------------+-------------+  +-----------------------+
                               | Hitung nilai akhir    |
                               | Tambah data ke list   |
                               +-----------------------+
                                         |
                                         v
+-----------------------------+ +-----------------------+
| Apakah pilihan '2'?         | | Apakah pilihan '3'?   |
| (Tampilkan Data)            | | (Hapus Data)          |
+-------------+---------------+ +-------------+---------+
              |Tidak                      |Ya
              v                           v
+-------------+-------------+  +----------+-----------+
| Lanjutkan ke pilihan lain |  | Input nama mahasiswa  |
| (3/4/5)                   |  | Jika ditemukan,       |
+-------------+-------------+  | hapus data            |
                               +-----------------------+
                                         |
                                         v
+-----------------------------+ +-----------------------+
| Apakah pilihan '4'?         | | Apakah pilihan '5'?   |
| (Ubah Data)                 | | (Keluar)              |
+-------------+---------------+ +-------------+---------+
              |Tidak                      |Ya
              v                           v
+-------------+-------------+  +-----------+-----------+
| Lanjutkan ke pilihan lain |  | Keluar dari program    |
| (5)                       |  +-----------------------+
+-------------+-------------+





#Deskripsi Program
Program ini menggunakan konsep OOP (Object-Oriented Programming) untuk mengelola data mahasiswa, termasuk menambah, menampilkan, menghapus, dan mengubah data. Program ini menggunakan kelas DaftarNilaiMahasiswa untuk menyimpan dan mengelola informasi mahasiswa.

#Struktur Program
Definisi Kelas DaftarNilaiMahasiswa:

-python
class DaftarNilaiMahasiswa:
    def __init__(self):
        self.data_mahasiswa = {}
Kelas ini memiliki konstruktor __init__ yang menginisialisasi dictionary data_mahasiswa untuk menyimpan data mahasiswa.

#Fungsi tambah(): Fungsi ini digunakan untuk menambah data mahasiswa baru. Pengguna diminta memasukkan nama, nilai tugas, nilai UTS, dan nilai UAS. Nilai akhir dihitung berdasarkan bobot tertentu dan data mahasiswa disimpan dalam dictionary.

-python
def tambah(self):
    nama = input("Masukkan nama mahasiswa: ")
    tugas = float(input("Masukkan nilai tugas: "))
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))
    
    nilai_akhir = 0.3 * tugas + 0.35 * uts + 0.35 * uas
    self.data_mahasiswa[nama] = {
        'tugas': tugas,
        'uts': uts,
        'uas': uas,
        'nilai_akhir': nilai_akhir
    }
    print(f"Data untuk {nama} telah ditambahkan.")

#Fungsi tampilkan(): Fungsi ini digunakan untuk menampilkan semua data mahasiswa yang ada. Jika tidak ada data, maka akan menampilkan pesan bahwa tidak ada data mahasiswa.

-python
def tampilkan(self):
    if self.data_mahasiswa:
        print("\nDaftar Data Mahasiswa:")
        for nama, nilai in self.data_mahasiswa.items():
            print(f"Nama: {nama}, Tugas: {nilai['tugas']}, UTS: {nilai['uts']}, UAS: {nilai['uas']}, Nilai Akhir: {nilai['nilai_akhir']:.2f}")
    else:
        print("Tidak ada data mahasiswa.")

#Fungsi hapus(nama): Fungsi ini digunakan untuk menghapus data mahasiswa berdasarkan nama. Jika nama yang dimasukkan tidak ditemukan, maka akan menampilkan pesan bahwa data tidak ditemukan.

-python
def hapus(self, nama):
    if nama in self.data_mahasiswa:
        del self.data_mahasiswa[nama]
        print(f"Data untuk {nama} telah dihapus.")
    else:
        print(f"Data untuk {nama} tidak ditemukan.")

#Fungsi ubah(nama): Fungsi ini digunakan untuk mengubah data mahasiswa yang sudah ada. Pengguna diminta memasukkan nilai tugas, nilai UTS, dan nilai UAS baru. Nilai akhir dihitung ulang dan data diperbarui dalam dictionary.

-python
def ubah(self, nama):
    if nama in self.data_mahasiswa:
        tugas = float(input("Masukkan nilai tugas baru: "))
        uts = float(input("Masukkan nilai UTS baru: "))
        uas = float(input("Masukkan nilai UAS baru: "))
        
        nilai_akhir = 0.3 * tugas + 0.35 * uts + 0.35 * uas
        self.data_mahasiswa[nama] = {
            'tugas': tugas,
            'uts': uts,
            'uas': uas,
            'nilai_akhir': nilai_akhir
        }
        print(f"Data untuk {nama} telah diperbarui.")
    else:
        print(f"Data untuk {nama} tidak ditemukan.")

#Fungsi menu(): Fungsi ini digunakan untuk menampilkan menu pilihan kepada pengguna. Pengguna dapat memilih untuk menambah data, menampilkan data, menghapus data, mengubah data, atau keluar dari program. Fungsi ini menggunakan loop while untuk terus menampilkan menu sampai pengguna memilih untuk keluar.

-python
def menu():
    daftar_nilai = DaftarNilaiMahasiswa()
    
    while True:
        print("\nMenu Pilihan:")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        print("4. Ubah Data")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/4/5): ")
        
        if pilihan == '1':
            daftar_nilai.tambah()
        elif pilihan == '2':
            daftar_nilai.tampilkan()
        elif pilihan == '3':
            nama = input("Masukkan nama mahasiswa yang datanya akan dihapus: ")
            daftar_nilai.hapus(nama)
        elif pilihan == '4':
            nama = input("Masukkan nama mahasiswa yang datanya akan diubah: ")
            daftar_nilai.ubah(nama)
        elif pilihan == '5':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

#Menjalankan Menu:

-python
menu()
Panggilan fungsi menu() untuk menjalankan program dan menampilkan menu pilihan kepada pengguna.
