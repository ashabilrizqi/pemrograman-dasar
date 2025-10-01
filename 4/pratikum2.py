pilihan = 0

while pilihan not in [1, 2, 3]:
    try:
        print("\nmenu:")
        print("1. lihat profile")
        print("2. ubah setting")
        print("3. keluar")
        pilihan = int(input("silahkan pilih (1-3): "))
    except ValueError:
        print("masukkan angka yang valid!")
        pilihan = 0
        
print(f"anda memilih opsi nomor {pilihan}")
