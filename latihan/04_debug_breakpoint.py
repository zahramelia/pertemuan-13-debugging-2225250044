def hitung_total(daftar_nilai):
    total = 0

    for nilai in daftar_nilai:
        total = total + nilai

    return total


nilai_mahasiswa = [80, 60, 90, 70]
hasil = hitung_total(nilai_mahasiswa)

print("Total nilai:", hasil)
print("Rata-rata:", hasil / len(nilai_mahasiswa))