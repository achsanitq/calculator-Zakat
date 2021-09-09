from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Zakat Yuk")
window.geometry("400x450")
window.iconbitmap("icon.ico")

f_home = Frame(window, bg="light green")
f_zakfit = Frame(window, bg="light grey")
f_zakmal = Frame(window, bg="light yellow")
f_zaksil = Frame(window, bg="light blue")

def swap(frame):
    frame.tkraise()

for frame in (f_home,f_zakfit,f_zakmal,f_zaksil):
    frame.place(x=0, y=0, width=400, height=450)

def hitung_zakfit():
    n_hrgbrs = hrgbrs.get()
    n_jumorg = jumorg.get()
    n_jumzaku = int(n_hrgbrs) * 3 * int(n_jumorg)
    n_jumzakb = int(n_jumorg) * 3
    jumzaku.set("Rp. "+ str(n_jumzaku))
    jumzakb.set(str(n_jumzakb)+ " kg")

def hitung_zakmal():
    n_hrgrmas = hargaemas.get()
    n_tabungan =tabungan.get()
    n_prop = properti.get()
    jumlah_harta = int(n_tabungan) + int(n_prop)
    nisab = 85 * int(n_hrgrmas)
    jumzak = float(jumlah_harta) * 2.5/100

    if(jumlah_harta >= nisab):
        total.set("Rp. " + str(jumzak))
    else:
        total.set("anda tidak wajib membayar zakat")

def hitung_zaksil():
    n_gaji = gaji.get()
    n_kebutuhan = kebutuhan.get()
    n_bonus = bonus.get()
    n_hrgberas = harga.get()
    n_gaji_brsh = float(n_gaji) + float(n_bonus) - float(n_kebutuhan)
    nishab = 653 * float(n_hrgberas)
    n_zakat = float(n_gaji_brsh) * 2.5/100

    if(n_gaji_brsh >= nishab ):
        hasil.set("Rp. "+ str(n_zakat))
    else:
        hasil.set("anda tidak wajib membayar zakat")

def rumfit():
    rumus = "Kadar Zakat = jumlah jiwa * 3 Kg \nTotal Zakat = kadar zakat * harga beras"
    messagebox.showinfo("Rumus Zakat Fitrah", rumus)

def rummal():
    rumus = """    Jumlah Harta = Uang cash, tabungan + barang berharga
    Nishab = 85 gr * harga emas
    Jumlah Harta > Nishab (Wajib Berzakat)
    Jumlah Harta < Nishab (Tidak Wajib Berzakat)
    Total Zakat = Jumlah Harta * 2.5%
    """
    messagebox.showinfo("Rumus Zakat Maal", rumus)

def rumsil():
    rumus = """    Gaji Bersih = gaji + bonus - kebutuhan
    Nishab = 653 Kg * harga beras
    Gaji Brsih > Nishab (Wajib Berzakat)
    Gaji Bersih < Nishab (Tidak Wajib Berzakat)
    Total Zakat = gaji bersih * 2.5%
    """
    messagebox.showinfo("Rumus Zakat Penghasilan", rumus)


#isi frame home
lbl_jenis = Label(f_home, text="Selamat Datang \nsilahkan pilih jenis zakat anda", font="verdana 14", bg="light green", fg="navy").place(x=52,y=50)

pho_zakfit = PhotoImage(file="fitrah.png")
pho_zakmal = PhotoImage(file="maal.png")
pho_zaksil = PhotoImage(file="hasil.png")

btn_zakfit = Button(f_home, image=pho_zakfit, text="zakat fitrah",compound=TOP,height=100,width=100, bg="white", command = lambda:swap(f_zakfit)).place(x=25, y=200)
btn_zakmal = Button(f_home, image=pho_zakmal, text="zakat maal",compound=TOP,height=100,width=100, bg="white", command = lambda:swap(f_zakmal)).place(x=145, y=200)
btn_zaksil = Button(f_home, image=pho_zaksil,text="zakat penghasilan", compound=TOP,height=100,width=100, bg="white", command = lambda:swap(f_zaksil)).place(x=265, y=200)

#isi frame zakfit
logo_zakfit = PhotoImage(file="logofit.png")
lbl_logofit = Label(f_zakfit, image=logo_zakfit, bg="light grey", bd=0).place(x=175, y=20)

lbl_zakfit = Label(f_zakfit, text="Zakat Fitrah", bg="light grey", fg="navy", font="helvatica 12").place(x=150,y=65)
lbl_hrgbrs = Label(f_zakfit, text="Harga Beras / Kg ", bg="light grey" ).place(x=80,y=105)
lbl_jumorg = Label(f_zakfit, text="Jumlah Jiwa ", bg="light grey" ).place(x=80,y=155)
lbl_jumfitb = Label(f_zakfit, text="Jumlah Kadar Zakat (Kg)" , bg="light grey" ).place(x=80,y=205)
lbl_jumfitu = Label(f_zakfit, text="Total Zakat Yang Dikeluarkan (Rp)" , bg="light grey" ).place(x=80,y=255)

hrgbrs = StringVar()
jumorg = StringVar()
jumzaku = StringVar()
jumzakb = StringVar()

ent_hrgbrs = Entry(f_zakfit,textvariable=hrgbrs, width=40).place(x=80,y=130)
ent_jumorg = Entry(f_zakfit,textvariable=jumorg, width=40).place(x=80,y=180)
ent_jumzakb = Entry(f_zakfit, textvariable=jumzakb, width=40,state=DISABLED).place(x=80,y=230)
ent_jumzaku = Entry(f_zakfit, textvariable=jumzaku, width=40,state=DISABLED).place(x=80,y=280)

btn_rumfit = Button(f_zakfit, text="Rumus", bg="white", command=rumfit).place(x=215,y=310)
btn_hitfit = Button(f_zakfit, text="Hitung", bg="white", command=hitung_zakfit).place(x=275,y=310)
logo_back = PhotoImage(file="back.png")
btn_backfit = Button(f_zakfit, image=logo_back, bd=0,bg="light grey", command= lambda:swap(f_home)).place(x=20,y=400)

#isi frame zakmal
logo_zakmal = PhotoImage(file="logosil.png")
lbl_logomal = Label(f_zakmal, image=logo_zakmal, bg="light yellow", bd=0).place(x=175, y=20)

lbl_zakmal = Label(f_zakmal, text="Zakat Maal", bg="light yellow", fg="navy",font="helvatica 12").place(x=153,y=65)
lbl_hrgems = Label(f_zakmal, text="Harga Emas / Gram", bg="light yellow").place(x=80,y=105)
lbl_tabdep = Label(f_zakmal, text="Uang Cash, Tabungan, Deposito", bg="light yellow").place(x=80,y=155)
lbl_proken = Label(f_zakmal, text="Properti dan Barang Berharga (Rp)", bg="light yellow").place(x=80,y=205)
lbl_jummal = Label(f_zakmal, text="Total Zakat Yang Dikeluarkan ", bg="light yellow").place(x=80,y=255)

hargaemas = StringVar()
tabungan = StringVar()
properti = StringVar()
total = StringVar()

ent_hrgems = Entry(f_zakmal,textvariable=hargaemas, width=40).place(x=80,y=130)
ent_tabdep = Entry(f_zakmal,textvariable=tabungan, width=40).place(x=80,y=180)
ent_proken = Entry(f_zakmal,textvariable=properti, width=40).place(x=80,y=230)
ent_jummal = Entry(f_zakmal,textvariable=total, width=40,state=DISABLED).place(x=80,y=280)

btn_rummal = Button(f_zakmal, text="Rumus", bg="white", command=rummal).place(x=215,y=310)
btn_hitmal = Button(f_zakmal, text="Hitung", bg="white", command=hitung_zakmal).place(x=275,y=310)
btn_backmal = Button(f_zakmal, image=logo_back, bd=0,bg="light yellow", command= lambda:swap(f_home)).place(x=20,y=400)

#isi frane zaksil
logo_zaksil = PhotoImage(file="logomal.png")
lbl_logosil = Label(f_zaksil, image=logo_zaksil, bg="light blue", bd=0).place(x=175, y=20)

lbl_zaksil = Label(f_zaksil, text="Zakat Penghasilan", bg="light blue", fg="navy",font="helvatica 12").place(x=130,y=65)
lbl_penghasilan = Label(f_zaksil, text="Penghasilan Perbulan", bg="light blue").place(x=80,y=105)
lbl_kebutuhan = Label(f_zaksil, text="Kebutuhan Perbulan", bg="light blue").place(x=80,y=155)
lbl_bonus = Label(f_zaksil, text="Jumlah Bonus Perbulan", bg="light blue").place(x=80,y=205)
lbl_hrgberas = Label(f_zaksil, text="Harga Beras / Kg", bg="light blue").place(x=80,y=255)
lbl_jumsil = Label(f_zaksil, text="Total Zakat Yang Dikeluarkan", bg="light blue").place(x=80,y=305)

gaji = StringVar()
kebutuhan = StringVar()
bonus = StringVar()
hasil = StringVar()
harga = StringVar()

ent_penghasilan = Entry(f_zaksil,textvariable=gaji, width=40).place(x=80,y=130)
ent_kebutuhan = Entry(f_zaksil,textvariable=kebutuhan, width=40).place(x=80,y=180)
ent_bonus = Entry(f_zaksil,textvariable=bonus, width=40).place(x=80,y=230)
ent_hrgberas = Entry(f_zaksil,textvariable=harga, width=40).place(x=80,y=280)
ent_jumsil = Entry(f_zaksil,textvariable=hasil, width=40,state=DISABLED).place(x=80,y=325)

btn_rumsil = Button(f_zaksil, text="Rumus", bg="white", command=rumsil).place(x=215,y=355)
btn_hitsil = Button(f_zaksil, text="Hitung", bg="white", command=hitung_zaksil).place(x=275,y=355)
btn_backsil = Button(f_zaksil, image=logo_back, bd=0,bg="light blue", command= lambda:swap(f_home)).place(x=20,y=400)

swap(f_home)
window.mainloop()