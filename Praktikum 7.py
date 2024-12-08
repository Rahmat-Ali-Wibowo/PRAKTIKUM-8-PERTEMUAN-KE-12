class DaftarNilaiMahasiswa:
    def __init__(self):
        self.data_mahasiswa = {}

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

    def tampilkan(self):
        if self.data_mahasiswa:
            print("\nDaftar Data Mahasiswa:")
            for nama, nilai in self.data_mahasiswa.items():
                print(f"Nama: {nama}, Tugas: {nilai['tugas']}, UTS: {nilai['uts']}, UAS: {nilai['uas']}, Nilai Akhir: {nilai['nilai_akhir']:.2f}")
        else:
            print("Tidak ada data mahasiswa.")

    def hapus(self, nama):
        if nama in self.data_mahasiswa:
            del self.data_mahasiswa[nama]
            print(f"Data untuk {nama} telah dihapus.")
        else:
            print(f"Data untuk {nama} tidak ditemukan.")

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

# Jalankan menu
menu()
