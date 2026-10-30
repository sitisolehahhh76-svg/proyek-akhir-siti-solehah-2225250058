from analisis import (
    hitung_persegi,
    hitung_persegi_panjang,
    hitung_segitiga,
    hitung_lingkaran,
    hitung_kubus,
    hitung_balok
)

from data_io import simpan_riwayat, baca_riwayat
from utilitas import tampilkan_menu, input_positif


def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            sisi = input_positif("Masukkan sisi: ")
            hasil = hitung_persegi(sisi)

        elif pilihan == "2":
            p = input_positif("Masukkan panjang: ")
            l = input_positif("Masukkan lebar: ")
            hasil = hitung_persegi_panjang(p, l)

        elif pilihan == "3":
            alas = input_positif("Masukkan alas: ")
            tinggi = input_positif("Masukkan tinggi: ")
            hasil = hitung_segitiga(alas, tinggi)

        elif pilihan == "4":
            r = input_positif("Masukkan jari-jari: ")
            hasil = hitung_lingkaran(r)

        elif pilihan == "5":
            sisi = input_positif("Masukkan sisi: ")
            hasil = hitung_kubus(sisi)

        elif pilihan == "6":
            p = input_positif("Masukkan panjang: ")
            l = input_positif("Masukkan lebar: ")
            t = input_positif("Masukkan tinggi: ")
            hasil = hitung_balok(p, l, t)

        elif pilihan == "7":
            print("\n=== RIWAYAT PERHITUNGAN ===")
            print(baca_riwayat())
            continue

        elif pilihan == "0":
            print("Terima kasih telah menggunakan program!")
            break

        else:
            print("Pilihan tidak tersedia!")
            continue

        print("\nHasil Perhitungan:")
        print(hasil)

        simpan_riwayat(hasil)
        print("Riwayat berhasil disimpan.")


if __name__ == "__main__":
    main()