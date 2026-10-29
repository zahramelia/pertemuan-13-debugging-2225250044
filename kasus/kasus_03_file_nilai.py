
nama_file = "nilai.txt"

try:
    with open(nama_file, "r") as file:
        isi = file.read()
        print("Isi file nilai:")
        print(isi)
except FileNotFoundError:
    print("Error: File nilai.txt tidak ditemukan.")
