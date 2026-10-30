import math


def hitung_persegi(sisi):
    luas = sisi * sisi
    keliling = 4 * sisi

    return (
        f"Bangun: Persegi\n"
        f"Luas: {luas}\n"
        f"Keliling: {keliling}"
    )


def hitung_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)

    return (
        f"Bangun: Persegi Panjang\n"
        f"Luas: {luas}\n"
        f"Keliling: {keliling}"
    )


def hitung_segitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi

    return (
        f"Bangun: Segitiga\n"
        f"Luas: {luas}"
    )


def hitung_lingkaran(jari_jari):
    luas = math.pi * jari_jari ** 2
    keliling = 2 * math.pi * jari_jari

    return (
        f"Bangun: Lingkaran\n"
        f"Luas: {luas:.2f}\n"
        f"Keliling: {keliling:.2f}"
    )


def hitung_kubus(sisi):
    volume = sisi ** 3

    return (
        f"Bangun: Kubus\n"
        f"Volume: {volume}"
    )


def hitung_balok(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi

    return (
        f"Bangun: Balok\n"
        f"Volume: {volume}"
    )