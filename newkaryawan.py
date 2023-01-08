from tkinter import *
import tkinter.font
from tkinter import ttk
import calendar

window = Tk()
window.title("Gaji Karyawan")
window.geometry("300x600")


class karyawan():
    """Data dan proses karyawan"""
    nama_perusahaan = "Fight United"
    gaji = 60000000

    def _init_(self, nama, pendidikan, golongan):
        """Menghitung pendapatan karyawan"""
        self.nama = nama
        self.pendidikan = pendidikan
        self.golongan = golongan

    def gol(self):
        self.golongan["value"] = ["Golongan 1",
                                    "Golongan 2",
                                    "Golongan 3"]
        

changefont = tkinter.font.Font(size = 20)
jdl = Label(window,text="FIGHT UNITED",font =changefont)
jdl.place(x=60,y=10)

nama = Label(window,text="Nama Karyawan")
pend = Label(window,text="Pendidikan")
gol = Label(window,text="Golongan")
gaji = Label(window,text="Gaji perbulan")


e1 = Entry(window,width=40)
e2 = Entry(window)
e3 = Entry(window)
e4 = Entry(window,width = 20)


nama.place(x=20, y=50)
pend.place(x=20, y=90)
gol.place(x=20, y=130)
gaji.place(x=20, y=170)

e1.place(x=20, y=70)
e2.place()
e3.place()
e4.place(x=20, y=190)


r = StringVar()

r.set("SMA")

rb = Radiobutton(window,text="SMA",variable=r,value="SMA").place(x=20,y=110)
rb2 = Radiobutton(window,text="D3",variable=r,value="D3").place(x=80,y=110)
rb3 = Radiobutton(window,text="S1",variable=r,value="S1").place(x=140,y=110)

gol= ttk.Combobox(window,
                           values=["Golongan 1",
                                    "Golongan 2",
                                        "Golongan 3"])
gol.grid(pady=150, padx=20)

def bulan():
        z = int(spin1.get())
        a = int(spin2.get())

        cal = calendar.month(a,z)

        txt.delete(0.0,END)
        txt.insert(INSERT,cal)

spin1 = Spinbox(window,values=(1,2,3,4,5,6,7,8,9,10,11,12),width=4)
spin1.place(x=20, y=300)

spin2 = Spinbox(window,from_=1999,to_=2100,width=4)
spin2.place(x=20, y=320)

btn = Button(window, text="Show",command=bulan).place(x=80, y=300)

txt = Text(window,width=23,height=8)
txt.place(x=20,y=350)

#mencari hari
def hari():
    j = int(e5.get())
    k = int(e6.get())
    
    day = calendar.weekday(k,j,1)
    weekDay = calendar.day_name[day]
    dy = weekDay
    
    pp.insert(INSERT,dy)

bln = Label(window,text="Bulan")
thn = Label(window,text="Tahun")

e5 = Entry(window,width=20)
e6 = Entry(window,width=20)

bln.place(x=20, y=210)
thn.place(x=20, y=250)

e5.place(x=20, y=230)
e6.place(x=20, y=270)

ss = Button(window, text="Hari",command=hari).place(x=90, y=540)

pp = Entry(window,width = 20)
pp.place(x=20,y=500)


window.mainloop()