import calendar

# Mencetak kalender 1 tahun

print("The Calendar of Year 2023 is : ")
print(calendar.calendar(2023))

#Data Karyawan
Staff = {'Vivi' : 'Staff', 'Ari' : 'Staff', 'Kiki' : 'Staff', 'Dimas' : 'Staff'}
OB = {'Cakra' : 'OB', 'Agung' : 'OB'}


d = calendar.Calendar()

key = list(Staff.keys())
keyOB = list(OB.keys())


#Fungsi Mencetak Jadwal Kerja Karyawan di Bulan Tertentu Berdasarkan Nama Pekerja
def jadwalStaff():
    print("------- Mencari Jadwal Staff pada Bulan Tertentu --------")
    a = input("Masukkan Nama Karyawan : ")
    b = input("Masukkan Kode Bulan (1-12) : ")
    f = d.monthdays2calendar(2022, int(b))

    if a == 'Vivi' :
        print("Karyawan", a, "Pada bulan", b, "memililiki jadwal kerja", "\n", f[0])
    elif a == 'Ari':
        print("Karyawan", a, "Pada bulan", b, "memililiki jadwal kerja", "\n", f[1])
    elif a == 'Kiki' :
        print("Karyawan", a, "Pada bulan", b, "memililiki jadwal kerja", "\n", f[2])
    elif a == 'Dimas':
        print("Karyawan", a, "Pada bulan", b, "memililiki jadwal kerja", "\n", f[3])
    elif a != key:
        print("Maaf, nama karyawan tidak terdaftar")
    else:
        print("Maaf input salah")


#Fungsi Mencetak Jadwal Kerja Karyawan di Bulan Tertentu Berdasarkan Nama Pekerja

def jadwalOB():
    print("------- Mencari Jadwal OB pada Bulan Tertentu --------")
    a = input("Masukkan Nama OB : ")
    b = input("Masukkan Kode Bulan (1-12) : ")
    f = d.monthdays2calendar(2022, int(b))

    if a == 'Cakra' :
        print("Nama Karyawan :", a, "Pada bulan", b, "memiliki jadwal kerja", "\n", f[0], "sampai", f[2])
    elif a == 'Agung':
        print("Nama Karyawan :", a, "Pada bulan", b, "memiliki jadwal kerja", "\n", f[3], "sampai", f[5])    
    elif a != keyOB:
        print("Maaf, nama karyawan tidak terdaftar")
    else:
        print("Maaf input salah")

"""Misal :
Jadwal Karyawan berdasarkan Hari :
Senin - Rabu :Vivi, Ari, Cakra
Kamis - Sabtu:Kiki, Dimas, Agung"""

def cekPekerja():
    print("------- Mencari Jadwal Seluruh Karyawan pada Hari Tertentu --------")
    mm = int(input("Masukkan Kode Bulan (1-12) : "))
    dd = int(input("Masukkan tanggal : "))

    cekHari = calendar.weekday(2022, mm, dd)
    print("Jadwal Karyawan yang bekerja pada ", dd, "-", mm, "-", "2022 adalah : " , "\n",  )

    if 0 <= cekHari <= 2 :
       
        print('''
        Staff    : Vivi dan Ari
        OB       : Cakra   
        
        ''')
        
    elif 3< cekHari <= 5 :
        print('''
        Staff    : Kiki dan Dimas
        OB       : Agung
        
        ''')

    else:
        print("Maaf input Anda salah")

jadwalStaff()
print()
jadwalOB()
print()
    





