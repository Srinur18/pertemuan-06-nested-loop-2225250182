while True:
    try:
        n = int(input("Masukkan nilai n: "))

        if n > 0:
            break

        print("Input harus lebih dari 0.")

    except ValueError:
        print("Masukkan angka yang valid.")

count = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i + j <= n:
            count += 1

print("Banyak pasangan =", count)