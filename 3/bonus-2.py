print("==== Program Hitung Bonus Karyawan ====")
nama_karyawan = input("masukkan nama karyawan: ")
lama_bekerja = int(input("masukkan lama bekerja (tahun): "))
performa = int(input("masukkan performa (0-100%): "))

status_bonus = ""
besar_bonus = 0
kategori = ""
alasan_tidak_dapat = ""

if lama_bekerja < 5:
    kategori = "junior"
elif lama_bekerja >= 5 and lama_bekerja <= 10:
    kategori = "senior"
else:
    kategori = "veteran"

if lama_bekerja >= 2 and performa >= 70:
    status_bonus = "memenuhi syarat"
    besar_bonus = (lama_bekerja * 500000) + (performa * 10000)
else:
    status_bonus = "tidak memenuhi syarat"
    besar_bonus = 0
    if lama_bekerja < 2:
        alasan_tidak_dapat = " (lama bekerja kurang dari 2 tahun)"
    if performa < 70:
        if alasan_tidak_dapat != "":
            alasan_tidak_dapat += " dan performa di bawah 70%"
        else:
            alasan_tidak_dapat = " (performa di bawah 70%)"

print("\n==== Laporan Bonus Karyawan ====")
print(f"nama karyawan : {nama_karyawan}")
print(f"lama bekerja : {lama_bekerja} ({kategori})")
print(f"performa : {performa}%")

if status_bonus == "memenuhi syarat":
    print(f"status bonus: {status_bonus}")
    print(f"besar bonus: Rp {besar_bonus}")
else:
    print(f"status bonus: {status_bonus}{alasan_tidak_dapat}")
    print(f"besar bonus: Rp {besar_bonus}")
print("=================")
