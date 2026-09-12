# Sistem Pendataan Donor dan Stok Darah PMI

stok_darah = [
    ("D01", "DIANA", "A", 2),
    ("D02", "AUREL", "B", 3),
    ("D03", "LILY" , "O", 2),
    ("D04", "DIALY", "B", 1),

]


def tampilkan_stok():
    print("---------------------------------------------------")
    print("              === DAFTAR STOK DARAH ===            ")
    print("---------------------------------------------------")

    if len(stok_darah) == 0:
        print("STOK DARAH SEDANG KOSONG.")
    else:
        for item in stok_darah:
            print(
                "ID:", item[0],
                "| Nama:", item[1],
                "| Gol.darah:", item[2],
                "| Kantong Darah:", item[3]
            )


while True:
    print()
    print("==================================================")
    print("     SISTEM PENDATAAN DONOR DAN STOK DARAH PMI   ")
    print("==================================================")
    print("MENU :")
    print("1. Lihat Semua Stok Darah")
    print("2. Tambah Data Stok Baru")
    print("3. Ubah Data Stok Darah")
    print("4. Hapus Data Stok Darah")
    print("5. Keluar")

    pilihan = input("PILIH MENU (1-5): ")

    if pilihan == "1":
        tampilkan_stok()

    elif pilihan == "2":
        print("___________________________________________________")
        print("         === TAMBAH DATA DONOR BARU ===           ")
        print("___________________________________________________")

        while True:
            id_donor = input("Masukkan ID Pendonor: ").strip()
            if id_donor == "":
                print("ID tidak boleh kosong.")
            elif any(item[0] == id_donor for item in stok_darah):
                print("ID sudah digunakan. Silakan gunakan ID lain.")
            else:
                break

        while True:
            nama = input("Nama Pendonor: ").strip()
            if nama == "":
                print("Nama tidak boleh kosong.")
            else:
                break

        while True:
            gol_darah = input("Golongan Darah (A/B/AB/O): ").strip().upper()
            if gol_darah in ("A", "B", "AB", "O"):
                break
            print("Golongan darah tidak valid. Pilih A, B, AB, atau O.")

        while True:
            jumlah_kantong = input("Jumlah Kantong Darah: ").strip()
            if jumlah_kantong.isdigit() and int(jumlah_kantong) > 0:
                jumlah_kantong = int(jumlah_kantong)
                break
            print("Jumlah kantong harus berupa angka lebih dari 0.")

        nstok_darah = (id_donor, nama, gol_darah, jumlah_kantong)
        stok_darah.append(nstok_darah)
        print(">>> DATA BERHASIL DITAMBAHKAN! <<<")

    elif pilihan == "3":
        print("___________________________________________________")
        print("              === UBAH DATA STOK DARAH ===         ")
        print("___________________________________________________")

        id_cari = input("Masukkan ID pendonor: ").strip()
        ditemukan = False

        for i in range(len(stok_darah)):
            if stok_darah[i][0] == id_cari:
                ditemukan = True
                print("Data ditemukan.")
                print("Nama:", stok_darah[i][1])
                print("Golongan Darah:", stok_darah[i][2])
                print("Stok Saat Ini:", stok_darah[i][3])

                while True:
                    jumlah_baru = input("Jumlah Kantong Darah Baru: ").strip()
                    if jumlah_baru.isdigit() and int(jumlah_baru) > 0:
                        jumlah_baru = int(jumlah_baru)
                        break
                    print("Jumlah kantong harus berupa angka lebih dari 0.")

                data_lama = stok_darah[i]
                stok_darah[i] = (
                    data_lama[0],
                    data_lama[1],
                    data_lama[2],
                    jumlah_baru
                )
                print(">>> STOK BERHASIL DIPERBARUI! <<<")
                break

        if not ditemukan:
            print("ID tidak ditemukan.")

    elif pilihan == "4":
        print("___________________________________________________")
        print("             === HAPUS DATA STOK DARAH ===         ")
        print("___________________________________________________")

        hapus_data = input("Masukkan ID pendonor yang ingin dihapus: ").strip()
        ditemukan = False

        for i in range(len(stok_darah)):
            if stok_darah[i][0] == hapus_data:
                ditemukan = True
                konfirmasi = input("Yakin ingin menghapus data ini? (ya/tidak): ").strip().lower()

                if konfirmasi == "ya":
                    stok_darah.pop(i)
                    print(">>> DATA BERHASIL DIHAPUS. <<<")
                else:
                    print("Penghapusan dibatalkan.")
                break

        if not ditemukan:
            print("ID tidak ditemukan.")

    elif pilihan == "5":
        print("PROGRAM SELESAI DONOR DARAH, TERIMA KASIH!")
        break

    else:
        print("Pilihan menu tidak valid. Silakan pilih 1-5.")