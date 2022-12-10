import datakaryawan

while True:
    nama = str(input("Masukkan nama anda: "))
    golongan = (input("Golongan berapa: "))
    if golongan == "1":
        print ("gaji anda:",datakaryawan.gol_satu())
    elif golongan == "2":
        print("gaji anda:",datakaryawan.gol_dua())
    else:
       print("gaji anda:",datakaryawan.gol_tiga())

    pendidikan = (input("Pendidikan terakhir [SMA/D1/D3/S1]: "))
    if pendidikan == "SMA":
        print("tunjangan pendidikan anda: ",datakaryawan.pendidikan_sma())
    elif pendidikan == "D1":
        print ("tunjangan pendidikan anda: ",datakaryawan.pendidikan_d1())
    elif pendidikan == "D3":
        print("tunjangan pendidikan anda: ",datakaryawan.pendidikan_d3())
    else:
        print("tunjangan pendidikan anda: ",datakaryawan.pendidikan_s1())

    jamkerja = int(input("Jam kerja yang dipilih: "))
    if jamkerja >= 8:
        print("tunjangan anda sebesar: ",datakaryawan.jamkerja_lbhdelapan(jamkerja))
        break
    else:
        print("tunjangan anda sebesar: ",datakaryawan.jamkerja_krgdelapan(jamkerja))
        break