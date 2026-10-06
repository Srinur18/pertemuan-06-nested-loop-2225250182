print("Jumlah Per Baris\n")

for i in range(1, 5):
    total_baris = 0

    print(f"Baris {i}:")

    for j in range(1, 4):
        hasil = i * j
        total_baris += hasil

        print(hasil, end=" ")

    print(f"= {total_baris}")