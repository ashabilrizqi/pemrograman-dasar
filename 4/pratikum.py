angka = -1

while angka <= 0:
    try:
        angka = int(input("masukkan angka positif: "))
        if angka <= 0:
            print("input tidak valid. masukkan angka lebih besar dari 0")
    except ValueError:
        print("itu bukan angka valid")
        angka = -1

print(f"terima kasih! angka anda adalah {angka}")
