def tampilkan_menu():
    print("\n===== KALKULATOR GEOMETRI =====")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    print("5. Kubus")
    print("6. Balok")
    print("7. Lihat Riwayat")
    print("0. Keluar")


def input_positif(pesan):
    while True:
        try:
            nilai = float(input(pesan))

            if nilai > 0:
                return nilai

            print("Nilai harus lebih dari 0!")

        except ValueError:
            print("Input harus berupa angka!")