# domain: mahasiswa, kodomain: mata kuliah
mahasiswa   = {"ani","budi","citra","ulok"}
mata_kuliah = {"matdis", "algoritma","basis data","jaringan"}

# hubungan sebagai dictionary (setisp mahasiswa -> satu matkul)
pemetaan = {
    "ani" : "matdis",
    "budi": "algoritma",
    "citra": "matdis",
    "ulok" : "basis data",

}

# apakah ini sebuah fungsi?
# fungsi : setiap elemen domain dipetakan ke tepat satu elemen kodomain
adalah_fungsi = len(pemetaan) == len(mahasiswa) and \
                all(v in mata_kuliah for v in pemetaan.values())
print("Apakah merupakan fungsi?", adalah_fungsi)

# range (output yang benar benar dihasilkan)
range_fungsi = set(pemetaan.values())
print("range:", range_fungsi)
print("kodomain:",mata_kuliah)

# injektif: tidak ada dua mahasiswa -> matkul yang sama
values = list(pemetaan.values())
injektif = len(values) == len(set(values))
print("injektif (one to one)?", injektif)

# surjektif: range = kodomain
surjektif = range_fungsi == mata_kuliah
print("surjektif?", surjektif)

# bijektif
bijektif = injektif and surjektif
print("Bijektif?",bijektif)

# analisis
print("\n--- Analisis ---")
for mhs, mk in pemetaan.items():
    print(f"    {mhs:6} -> {mk}")
    