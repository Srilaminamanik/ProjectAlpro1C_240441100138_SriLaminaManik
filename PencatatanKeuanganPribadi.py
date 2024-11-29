import datetime

transaksi = []
kategori_valid = {"Uang saku", "Pengeluaran"}

def login():
    print("=== Login ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username == "RIRI DAN CHELSY" and password == "12345":
        print("Login berhasil. Selamat datang!")
        return True
    else:
        print("Username atau password salah. Silakan coba lagi.")
        return False

# 1. Menambah transaksi
def tambah_transaksi(jenis, jumlah, nama_barang=None):
    total_Uang_saku = sum(jumlah for jenis_trans, jumlah, _, _ in transaksi if jenis_trans == "Uang saku")
    total_pengeluaran = sum(jumlah for jenis_trans, jumlah, _, _ in transaksi if jenis_trans == "Pengeluaran")
    
    if jenis not in kategori_valid:
        print("Kategori tidak valid. Pilih kategori yang benar.")
        return

    if jenis == "Pengeluaran" and not nama_barang:
        print("Nama barang harus diisi untuk kategori Pengeluaran.")
        return

    # Memeriksa apakah pengeluaran akan melebihi total uang saku
    if jenis == "Pengeluaran" and (total_pengeluaran + jumlah > total_Uang_saku):
        print("Transaksi gagal! Pengeluaran melebihi total uang saku.")
        return

    # Input tanggal transaksi
    tanggal = input("Masukkan tanggal transaksi (format: YYYY-MM-DD): ")
    try:
        datetime.datetime.strptime(tanggal, "%Y-%m-%d")
    except ValueError:
        print("Tanggal tidak valid. Gunakan format YYYY-MM-DD.")
        return

    # 2. Tambahkan transaksi jika valid
    transaksi.append((jenis, jumlah, nama_barang, tanggal))
    
    if jenis == "Uang saku":
        print(f"Transaksi {jenis} sebesar Rp{jumlah} telah ditambahkan pada {tanggal}.")
    elif nama_barang:
        print(f"Transaksi {jenis} sebesar Rp{jumlah} untuk {nama_barang} telah ditambahkan pada {tanggal}.")
    else:
        print(f"Transaksi {jenis} sebesar Rp{jumlah} telah ditambahkan pada {tanggal}.")

    # Tampilkan sisa uang
    total_Uang_saku += jumlah if jenis == "Uang saku" else 0
    sisa_uang = total_Uang_saku - total_pengeluaran
    print(f"Sisa uang saat ini: Rp{sisa_uang}")

# 3. Menampilkan laporan keuangan
def tampilkan_laporan():
    total_Uang_saku = sum(jumlah for jenis, jumlah, _, _ in transaksi if jenis == "Uang saku")
    total_pengeluaran = sum(jumlah for jenis, jumlah, _, _ in transaksi if jenis == "Pengeluaran")
    uang = total_Uang_saku - total_pengeluaran

    print("\nLaporan pencatatan Keuangan pribadi:")
    print(f"Total Uang saku: Rp{total_Uang_saku}")
    print(f"Total Pengeluaran: Rp{total_pengeluaran}")
    print(f"Sisa Uang: Rp{uang}")

# 4. Menampilkan semua transaksi
def tampilkan_transaksi():
    print("\nDaftar Transaksi:")
    if not transaksi:
        print("Belum ada transaksi.")
        return
    for i, (jenis, jumlah, nama_barang, tanggal) in enumerate(transaksi, 1):
        if jenis == "Pengeluaran" and nama_barang:
            print(f"{i}. {tanggal} - {jenis}: Rp{jumlah} (Nama Barang: {nama_barang})")
        else:
            print(f"{i}. {tanggal} - {jenis}: Rp{jumlah}")

# 5. Mengupdate transaksi
def update_transaksi(index):
    if index < 1 or index > len(transaksi):
        print("Indeks tidak valid. Tidak ada transaksi yang ditemukan.")
        return
    
    jenis, jumlah, nama_barang, tanggal = transaksi[index - 1]
    
    # Tampilkan detail transaksi saat ini
    print(f"\nDetail Transaksi yang dipilih:")
    print(f"Tanggal: {tanggal}, Jenis: {jenis}, Jumlah: Rp{jumlah}, Nama Barang: {nama_barang or 'N/A'}")

    # Input baru untuk update
    new_tanggal = input("Masukkan tanggal baru (tekan Enter untuk tetap): ")
    
    new_nama_barang = input("Masukkan nama barang baru (tekan Enter untuk tetap): ")
    
    new_jumlah_str = input("Masukkan jumlah baru (tekan Enter untuk tetap): ")
    
    new_jumlah = None
    if new_jumlah_str != "":
        try:
            new_jumlah = int(new_jumlah_str)
        except ValueError:
            print("Input tidak valid. Jumlah harus berupa angka.")

    # Update nilai jika diisi
    updated_tanggal = new_tanggal if new_tanggal else tanggal
    updated_nama_barang = new_nama_barang if new_nama_barang else nama_barang
    updated_jumlah = new_jumlah if new_jumlah is not None else jumlah
    
    # Simpan perubahan ke dalam daftar transaksi
    transaksi[index - 1] = (jenis, updated_jumlah, updated_nama_barang, updated_tanggal)
    
    print("Transaksi berhasil diperbarui.")

# 6. Menghapus transaksi
def hapus_transaksi(index):
    if index < 1 or index > len(transaksi):
        print("Indeks tidak valid. Tidak ada transaksi yang ditemukan.")
        return
    
    # Konfirmasi sebelum menghapus
    confirm = input(f"Apakah Anda yakin ingin menghapus transaksi ke-{index}? (y/n): ")
    
    if confirm.lower() == 'y':
        del transaksi[index - 1]
        print("Transaksi berhasil dihapus.")

# Validasi input angka
def input_angka(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Input tidak valid. Masukkan angka!")

# Fungsi utama
def main():
    if not login():
        return

    while True:
        print("\n====Pencatatan Keuangan Pribadi====")
        print("1. Tambah Uang Saku")
        print("2. Tambah Pengeluaran")
        print("3. Lihat Laporan Keuangan")
        print("4. Lihat Semua Transaksi")
        print("5. Update Transaksi")
        print("6. Hapus Transaksi")
        print("7. Keluar")

        pilihan = input("Pilih menu (1-7): ")

        if pilihan == "1":
            jumlah = input_angka("Masukkan jumlah Uang saku: ")
            tambah_transaksi("Uang saku", jumlah)
        elif pilihan == "2":
            jumlah = input_angka("Masukkan jumlah pengeluaran: ")
            nama_barang = input("Masukkan nama barang: ")
            tambah_transaksi("Pengeluaran", jumlah, nama_barang)
        elif pilihan == "3":
            tampilkan_laporan()
        elif pilihan == "4":
            tampilkan_transaksi()
        elif pilihan == "5":
            tampilkan_transaksi()
            index = input_angka("Masukkan nomor transaksi yang ingin diupdate: ")
            update_transaksi(index)
        elif pilihan == "6":
            tampilkan_transaksi()
            index = input_angka("Masukkan nomor transaksi yang ingin dihapus: ")
            hapus_transaksi(index)
        elif pilihan == "7":
            print("Terima kasih telah menggunakan program pencatatan keuangan. Semoga tidak boros!")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")

if __name__ == "__main__":
    main()