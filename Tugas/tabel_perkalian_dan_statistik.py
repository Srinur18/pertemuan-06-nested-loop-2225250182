print("=== TABEL PERKALIAN DAN STATISTIK ===")

while True:
    try:
        n = int(input("Masukkan nilai n: "))

        if n > 0:
            break

        print("n harus lebih dari 0.")

    except ValueError:
        print("Masukkan angka yang valid.")

total_semua = 0
count_genap = 0

print("\nTabel Perkalian:\n")

for i in range(1, n + 1):

    total_baris = 0

    for j in range(1, n + 1):

        hasil = i * j

        print(f"{hasil:4}", end="")

        total_baris += hasil
        total_semua += hasil

        if hasil % 2 == 0:
            count_genap += 1

    print(f" | Jumlah Baris = {total_baris}")

print("\nStatistik")
print("Total seluruh hasil =", total_semua)
print("Banyak hasil genap =", count_genap)