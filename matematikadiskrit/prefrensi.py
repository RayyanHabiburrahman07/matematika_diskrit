python = {"Ani", "Budi", "Citra"}
java = {"Budi", "Deni"}
sql = {"Ani", "Budi", "Eka"}
semua_mahasiswa = {"Ani", "Budi", "Citra", "Eka", "Fajar"}

python_saja = python - (java | sql)
python_dan_java = python & java
minimal_satu = python | java | sql
tidak_menyukai_ketiganya = semua_mahasiswa - (python | java | sql)

print("Python saja :", python_saja)
print("Python dan Java :", python_dan_java)
print("Mininmal satu:", minimal_satu)
print("Tidak Menyukai Ketiganya:", tidak_menyukai_ketiganya)