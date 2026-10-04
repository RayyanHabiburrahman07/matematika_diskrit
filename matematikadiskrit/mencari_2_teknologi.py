python = {"Ani", "Budi", "Citra"}
java = {"Budi", "Deni"}
sql = {"Ani", "Deni", "Eka"}
javascript = {"Fajar", "Budi", "Eka"}
semua_mahasiswa = {"Ani", "Budi", "Citra", "Deni", "Eka", "Fajar"}

tepat_dua = ((python & java)|(python & sql)|(python & javascript)|(java & sql)|(java & javascript)|(sql & javascript))

print("Mahasiswa yang menyukai 2 teknologi : ", tepat_dua)