
# Pertemuan 13 - Debugging, Tracing, dan Testing

## Identitas Mahasiswa
- Nama: Zahra Amelia
- NIM: 2225250044
- Mata Kuliah: Algoritma dan Pemrograman
- Pertemuan: 13

## Deskripsi
Proyek ini dibuat untuk mempelajari debugging, tracing, dan testing pada program Python. Kegiatan meliputi menelusuri alur program, menguji beberapa kondisi, menemukan kesalahan, memperbaiki kode, dan melakukan pengujian ulang.

## Struktur Folder
- `latihan/` : latihan tracing dan testing.
- `kasus/` : contoh kasus kesalahan program.
- `praktik/` : program praktik debugging.

## Hasil Latihan
1. `01_trace_loop.py` digunakan untuk menelusuri perulangan. Hasilnya adalah 24.
2. `02_trace_fungsi.py` digunakan untuk menguji fungsi perhitungan diskon. Hasilnya adalah 180000.0.
3. `03_test_case.py` digunakan untuk menguji batas kelulusan nilai.
4. `04_debug_breakpoint.py` digunakan untuk mengamati proses perhitungan total dan rata-rata nilai.

## Laporan Bug

### Bug 1: Batas Kelulusan
- Masalah: Nilai 60 menghasilkan status Tidak lulus.
- Penyebab: Kondisi menggunakan `nilai > 60`.
- Perbaikan: Kondisi diubah menjadi `nilai >= 60`.
- Hasil pengujian ulang: Nilai 60 menghasilkan status Lulus.

### Bug 2: Perhitungan Rata-rata
- Masalah: Rata-rata dihitung dengan membagi jumlah nilai dengan angka 5.
- Penyebab: Jumlah data tidak digunakan sebagai pembagi.
- Perbaikan: Menggunakan `len(nilai)` sebagai pembagi dan menangani daftar kosong.
- Hasil pengujian ulang: Rata-rata `[80, 60, 90, 70]` adalah 75.0.

### Bug 3: Nilai Tertinggi
- Masalah: Program menghasilkan nilai tertinggi 0.
- Penyebab: Kondisi perbandingan menggunakan `x < tertinggi`.
- Perbaikan: Nilai awal diambil dari data pertama dan perbandingan diubah menjadi `x > tertinggi`.
- Hasil pengujian ulang: Nilai tertinggi adalah 90.

## Test Case

| ID | Pengujian | Hasil yang Diharapkan |
|---|---|---|
| T1 | Rata-rata `[80, 60, 90, 70]` | 75.0 |
| T2 | Rata-rata `[100, 80]` | 90.0 |
| T3 | Status nilai 60 | Lulus |
| T4 | Status nilai 59 | Tidak lulus |
| T5 | Nilai tertinggi `[80, 60, 90, 70]` | 90 |

## Kesimpulan
Debugging membantu menemukan dan memperbaiki kesalahan pada program. Tracing membantu memahami alur eksekusi program, sedangkan testing digunakan untuk memeriksa apakah hasil program sesuai dengan yang diharapkan. Pengujian ulang dilakukan setelah perbaikan untuk memastikan bug telah teratasi.
