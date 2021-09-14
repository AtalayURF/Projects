
from tkinter import *

master = Tk()
master.geometry("900x900")
canvas = Canvas(master)
canvas.pack()

frame_ust_a = Frame(master, bg='#2b63ff')
frame_ust_a.place(relx= 0.1, rely=0.1, relwidth=0.7, relheight=0.05)

frame_ust = Frame(master, bg='#5ea7eb')
frame_ust.place(relx= 0.1, rely=0.16, relwidth=0.7, relheight=0.05)

frame_ust_b = Frame(master, bg='#5ea7eb')
frame_ust_b.place(relx= 0.1, rely=0.22, relwidth=0.7, relheight=0.05)

frame_alt = Frame(master, bg='#5ea7eb')
frame_alt.place(relx= 0.1, rely=0.28, relwidth=0.7, relheight=0.05)

frame_alt_b = Frame(master, bg='#5ea7eb')
frame_alt_b.place(relx= 0.1, rely=0.34, relwidth=0.7, relheight=0.05)

frame_alt_sol = Frame(master, bg='#5ea7eb')
frame_alt_sol.place(relx= 0.1, rely=0.40, relwidth=0.34, relheight=0.05)

frame_alt_sag = Frame(master, bg='#5ea7eb')
frame_alt_sag.place(relx= 0.46, rely=0.40, relwidth=0.34, relheight=0.05)

### Sol Cam Tarafı ###

frame_sol_ba = Frame(master, bg='#5ea7eb')
frame_sol_ba.place(relx= 0.1, rely=0.46, relwidth=0.17, relheight=0.05)

frame_sol_a1 = Frame(master, bg='#5ea7eb')
frame_sol_a1.place(relx= 0.1, rely=0.51, relwidth=0.17, relheight=0.05)

frame_sol_a2 = Frame(master, bg='#5ea7eb')
frame_sol_a2.place(relx= 0.1, rely=0.56, relwidth=0.17, relheight=0.05)

frame_sol_a3 = Frame(master, bg='#5ea7eb')
frame_sol_a3.place(relx= 0.1, rely=0.61, relwidth=0.17, relheight=0.05)

frame_sol_a4 = Frame(master, bg='#5ea7eb')
frame_sol_a4.place(relx= 0.1, rely=0.66, relwidth=0.17, relheight=0.05)

frame_sol_a5 = Frame(master, bg='#5ea7eb')
frame_sol_a5.place(relx= 0.1, rely=0.71, relwidth=0.17, relheight=0.05)

frame_sol_a6 = Frame(master, bg='#5ea7eb')
frame_sol_a6.place(relx= 0.1, rely=0.76, relwidth=0.17, relheight=0.05)

frame_sol_a7 = Frame(master, bg='#5ea7eb')
frame_sol_a7.place(relx= 0.1, rely=0.81, relwidth=0.17, relheight=0.05)

### Sol Cam Tarafı ###

frame_sol_bb = Frame(master, bg='#5ea7eb')
frame_sol_bb.place(relx= 0.27, rely=0.46, relwidth=0.17, relheight=0.05)

frame_sol_b1 = Frame(master, bg='#5ea7eb')
frame_sol_b1.place(relx= 0.27, rely=0.51, relwidth=0.17, relheight=0.05)

frame_sol_b2 = Frame(master, bg='#5ea7eb')
frame_sol_b2.place(relx= 0.27, rely=0.56, relwidth=0.17, relheight=0.05)

frame_sol_b3 = Frame(master, bg='#5ea7eb')
frame_sol_b3.place(relx= 0.27, rely=0.61, relwidth=0.17, relheight=0.05)

frame_sol_b4 = Frame(master, bg='#5ea7eb')
frame_sol_b4.place(relx= 0.27, rely=0.66, relwidth=0.17, relheight=0.05)

frame_sol_b5 = Frame(master, bg='#5ea7eb')
frame_sol_b5.place(relx= 0.27, rely=0.71, relwidth=0.17, relheight=0.05)

frame_sol_b6 = Frame(master, bg='#5ea7eb')
frame_sol_b6.place(relx= 0.27, rely=0.76, relwidth=0.17, relheight=0.05)

frame_sol_b7 = Frame(master, bg='#5ea7eb')
frame_sol_b7.place(relx= 0.27, rely=0.81, relwidth=0.17, relheight=0.05)

### Sağ Koridor Tarafı ###

frame_sag_bc = Frame(master, bg='#5ea7eb')
frame_sag_bc.place(relx= 0.46, rely=0.46, relwidth=0.17, relheight=0.05)

frame_sag_c1 = Frame(master, bg='#5ea7eb')
frame_sag_c1.place(relx= 0.46, rely=0.51, relwidth=0.17, relheight=0.05)

frame_sag_c2 = Frame(master, bg='#5ea7eb')
frame_sag_c2.place(relx= 0.46, rely=0.56, relwidth=0.17, relheight=0.05)

frame_sag_c3 = Frame(master, bg='#5ea7eb')
frame_sag_c3.place(relx= 0.46, rely=0.61, relwidth=0.17, relheight=0.05)

frame_sag_c4 = Frame(master, bg='#5ea7eb')
frame_sag_c4.place(relx= 0.46, rely=0.66, relwidth=0.17, relheight=0.05)

frame_sag_c5 = Frame(master, bg='#5ea7eb')
frame_sag_c5.place(relx= 0.46, rely=0.71, relwidth=0.17, relheight=0.05)

frame_sag_c6 = Frame(master, bg='#5ea7eb')
frame_sag_c6.place(relx= 0.46, rely=0.76, relwidth=0.17, relheight=0.05)

frame_sag_c7 = Frame(master, bg='#5ea7eb')
frame_sag_c7.place(relx= 0.46, rely=0.81, relwidth=0.17, relheight=0.05)

### Sağ Cam Tarafı ###

frame_sag_bd = Frame(master, bg='#5ea7eb')
frame_sag_bd.place(relx= 0.63, rely=0.46, relwidth=0.17, relheight=0.05)

frame_sag_d1 = Frame(master, bg='#5ea7eb')
frame_sag_d1.place(relx= 0.63, rely=0.51, relwidth=0.17, relheight=0.05)

frame_sag_d2 = Frame(master, bg='#5ea7eb')
frame_sag_d2.place(relx= 0.63, rely=0.56, relwidth=0.17, relheight=0.05)

frame_sag_d3 = Frame(master, bg='#5ea7eb')
frame_sag_d3.place(relx= 0.63, rely=0.61, relwidth=0.17, relheight=0.05)

frame_sag_d4 = Frame(master, bg='#5ea7eb')
frame_sag_d4.place(relx= 0.63, rely=0.66, relwidth=0.17, relheight=0.05)

frame_sag_d5 = Frame(master, bg='#5ea7eb')
frame_sag_d5.place(relx= 0.63, rely=0.71, relwidth=0.17, relheight=0.05)

frame_sag_d6 = Frame(master, bg='#5ea7eb')
frame_sag_d6.place(relx= 0.63, rely=0.76, relwidth=0.17, relheight=0.05)

frame_sag_d7 = Frame(master, bg='#5ea7eb')
frame_sag_d7.place(relx= 0.63, rely=0.81, relwidth=0.17, relheight=0.05)

proje = Label(frame_ust_a, bg='#c4d0f2', text= " -- UYGULAMA ADI -- ", font="Calibri 10 bold")
proje.pack(padx=10, pady=10)

koltuk_tipi_etiket = Label(frame_ust, bg='#92c4f0', text = "Mercedes-Benz Otobüs Tipi", font="Verdana 10 bold")
koltuk_tipi_etiket.pack(padx=10, pady=10, side=LEFT)

koltuk_tipi_opsiyon = StringVar(frame_ust)
koltuk_tipi_opsiyon.set("\t")

koltuk_tipi_acilir_menu = OptionMenu(
    frame_ust,
    koltuk_tipi_opsiyon,
    "MB-12R",
    "MB-15R",
    "MB-17R",
    "MB-19R")
koltuk_tipi_acilir_menu.pack(padx=10, pady=10, side=RIGHT)

kapi_tipi_opsiyon = StringVar(frame_ust)
kapi_tipi_opsiyon.set("\t")

kapi_tipi_etiket = Label(frame_ust_b, bg='#92c4f0', text = "Orta Kapı Boyutu", font="Verdana 10 bold")
kapi_tipi_etiket.pack(padx=10, pady=10, side=LEFT)

kapi_tipi_acilir_menu = OptionMenu(
    frame_ust_b,
    kapi_tipi_opsiyon,
    "Dar-Kapı",
    "Geniş-Kapı")
kapi_tipi_acilir_menu.pack(padx=10, pady=10, side=RIGHT)

sol = Label(frame_alt, text="Sol Koltuk Sayısı", bg='#92c4f0', font="Verdana 10 bold").pack(padx=10, pady=10, side=LEFT)

##Sol taraf = Sürücü Tarafı##
sol_koltuk = StringVar(frame_alt)
sol_koltuk.set("\t")

sol_koltuk_yazı = Text(frame_alt, height=1.4, width=13)
sol_koltuk = IntVar(frame_alt)
sol_koltuk_yazı.pack(padx=10, pady=10, side=RIGHT)

sag = Label(frame_alt_b, text="Sağ Koltuk Sayısı", bg='#92c4f0', font="Verdana 10 bold").pack(padx=10, pady=10, side=LEFT)

##Sağ taraf = Kapı Tarafı##
sag_koltuk = StringVar(frame_alt_b)
sag_koltuk.set("\t")

sag_koltuk_yaz = Text(frame_alt_b, height=1.4, width=13)
sag_koltuk = IntVar(frame_alt_b)
sag_koltuk_yaz.pack(padx=10, pady=10, side=RIGHT)

sol_baslık = Label(frame_alt_sol, text="Sürücü Tarafı Koltuk Mesafeleri", bg='#92c4f0', font="Verdana 10 bold").pack(padx=25, pady=11)
sag_baslık = Label(frame_alt_sag, text="Kapı Tarafı Koltuk Mesafeleri", bg='#92c4f0', font="Verdana 10 bold").pack(padx=23, pady=11)

### Sol Cam Tarafı ###
solb = Label(frame_sol_ba, text="B-A1", bg='#92c4f0', font="Verdana 10 bold").pack(padx=10, pady=5, side=LEFT)
ba_yaz = Text(frame_sol_ba, height=2, width=5)
ba = IntVar(frame_sol_ba)
ba_yaz.pack(padx=20, pady=10, side=LEFT)

sola1 = Label(frame_sol_a1, text="A1-A2", bg='#92c4f0', font="Verdana 10 bold").pack(padx=10, pady=5, side=LEFT)
a1_yaz = Text(frame_sol_a1, height=2, width=5)
a1 = IntVar(frame_sol_a1)
a1_yaz.pack(padx=10, pady=10, side=LEFT)

sola2 = Label(frame_sol_a2, text="A2-A3", bg='#92c4f0', font="Verdana 10 bold").pack(padx=10, pady=5, side=LEFT)
a2_yaz = Text(frame_sol_a2, height=2, width=5)
a2 = IntVar(frame_sol_a2)
a2_yaz.pack(padx=10, pady=10, side=LEFT)

sola3 = Label(frame_sol_a3, text="A3-A4", bg='#92c4f0', font="Verdana 10 bold").pack(padx=10, pady=5, side=LEFT)
a3_yaz = Text(frame_sol_a3, height=2, width=5)
a3 = IntVar(frame_sol_a3)
a3_yaz.pack(padx=10, pady=10, side=LEFT)

sola4 = Label(frame_sol_a4, text="A4-A5", bg='#92c4f0', font="Verdana 10 bold").pack(padx=10, pady=5, side=LEFT)
a4_yaz = Text(frame_sol_a4, height=2, width=5)
a4 = IntVar(frame_sol_a4)
a4_yaz.pack(padx=10, pady=10, side=LEFT)

sola5 = Label(frame_sol_a5, text="A5-A6", bg='#92c4f0', font="Verdana 10 bold").pack(padx=10, pady=5, side=LEFT)
a5_yaz = Text(frame_sol_a5, height=2, width=5)
a5 = IntVar(frame_sol_a5)
a5_yaz.pack(padx=10, pady=10, side=LEFT)

sola6 = Label(frame_sol_a6, text="A6-A7", bg='#92c4f0', font="Verdana 10 bold").pack(padx=10, pady=5, side=LEFT)
a6_yaz = Text(frame_sol_a6, height=2, width=5)
a6 = IntVar(frame_sol_a6)
a6_yaz.pack(padx=10, pady=10, side=LEFT)

sola7 = Label(frame_sol_a7, text="A7-A8", bg='#92c4f0', font="Verdana 10 bold").pack(padx=10, pady=5, side=LEFT)
a7_yaz = Text(frame_sol_a7, height=2, width=5)
a7 = IntVar(frame_sol_a7)
a7_yaz.pack(padx=10, pady=10, side=LEFT)

### Sol Koridor Tarafı ###

solb = Label(frame_sol_bb, text="A8-A9", bg='#92c4f0', font="Verdana 10 bold").pack(padx=10, pady=5, side=LEFT)
bb_yaz = Text(frame_sol_bb, height=2, width=5)
bb = IntVar(frame_sol_bb)
bb_yaz.pack(padx=10, pady=10, side=RIGHT)

solb1 = Label(frame_sol_b1, text="A9-A10", bg='#92c4f0', font="Verdana 10 bold").pack(padx=10, pady=5, side=LEFT)
b1_yaz = Text(frame_sol_b1, height=2, width=5)
b1 = IntVar(frame_sol_b1)
b1_yaz.pack(padx=10, pady=10, side=RIGHT)

solb2 = Label(frame_sol_b2, text="A10-A11", bg='#92c4f0', font="Verdana 10 bold").pack(padx=10, pady=5, side=LEFT)
b2_yaz = Text(frame_sol_b2, height=2, width=5)
b2 = IntVar(frame_sol_b2)
b2_yaz.pack(padx=10, pady=10, side=LEFT)

solb3 = Label(frame_sol_b3, text="A11-A12", bg='#92c4f0', font="Verdana 10 bold").pack(padx=10, pady=5, side=LEFT)
b3_yaz = Text(frame_sol_b3, height=2, width=5)
b3 = IntVar(frame_sol_b3)
b3_yaz.pack(padx=10, pady=10, side=LEFT)

solb4 = Label(frame_sol_b4, text="A12-A13", bg='#92c4f0', font="Verdana 10 bold").pack(padx=10, pady=5, side=LEFT)
b4_yaz = Text(frame_sol_b4, height=2, width=5)
b4 = IntVar(frame_sol_b4)
b4_yaz.pack(padx=10, pady=10, side=LEFT)

solb5 = Label(frame_sol_b5, text="A13-A14", bg='#92c4f0', font="Verdana 10 bold").pack(padx=10, pady=5, side=LEFT)
b5_yaz = Text(frame_sol_b5, height=2, width=5)
b5 = IntVar(frame_sol_b5)
b5_yaz.pack(padx=10, pady=10, side=LEFT)

solb6 = Label(frame_sol_b6, text="A14-A15", bg='#92c4f0', font="Verdana 10 bold").pack(padx=10, pady=5, side=LEFT)
b6_yaz = Text(frame_sol_b6, height=2, width=5)
b6 = IntVar(frame_sol_b6)
b6_yaz.pack(padx=10, pady=10, side=LEFT)

solb7 = Label(frame_sol_b7, text="A15-A16", bg='#92c4f0', font="Verdana 10 bold").pack(padx=10, pady=5, side=LEFT)
b7_yaz = Text(frame_sol_b7, height=2, width=5)
b7 = IntVar(frame_sol_b7)
b7_yaz.pack(padx=10, pady=10, side=LEFT)

### Sağ Koridor Tarafı ###

sagbc = Label(frame_sag_bc, text="B-D1", bg='#92c4f0', font="Verdana 10 bold").pack(padx=10, pady=5, side=LEFT)
bc_yaz = Text(frame_sag_bc, height=2, width=5)
bc = IntVar(frame_sag_bc)
bc_yaz.pack(padx=20, pady=10, side=LEFT)

sagc1 = Label(frame_sag_c1, text="D1-D2", bg='#92c4f0', font="Verdana 10 bold").pack(padx=10, pady=5, side=LEFT)
c1_yaz = Text(frame_sag_c1, height=2, width=5)
c1 = IntVar(frame_sag_c1)
c1_yaz.pack(padx=10, pady=10, side=LEFT)

sagc2 = Label(frame_sag_c2, text="D2-D3", bg='#92c4f0', font="Verdana 10 bold").pack(padx=10, pady=5, side=LEFT)
c2_yaz = Text(frame_sag_c2, height=2, width=5)
c2 = IntVar(frame_sag_c2)
c2_yaz.pack(padx=10, pady=10, side=LEFT)

sagc3 = Label(frame_sag_c3, text="D3-D4", bg='#92c4f0', font="Verdana 10 bold").pack(padx=10, pady=5, side=LEFT)
c3_yaz = Text(frame_sag_c3, height=2, width=5)
c3 = IntVar(frame_sag_c3)
c3_yaz.pack(padx=10, pady=10, side=LEFT)

sagc4 = Label(frame_sag_c4, text="D4-D5", bg='#92c4f0', font="Verdana 10 bold").pack(padx=10, pady=5, side=LEFT)
c4_yaz = Text(frame_sag_c4, height=2, width=5)
c4 = IntVar(frame_sag_c4)
c4_yaz.pack(padx=10, pady=10, side=LEFT)

sagc5 = Label(frame_sag_c5, text="D5-D6", bg='#92c4f0', font="Verdana 10 bold").pack(padx=10, pady=5, side=LEFT)
c5_yaz = Text(frame_sag_c5, height=2, width=5)
c5 = IntVar(frame_sag_c5)
c5_yaz.pack(padx=10, pady=10, side=LEFT)

sagc6 = Label(frame_sag_c6, text="D6-D7", bg='#92c4f0', font="Verdana 10 bold").pack(padx=10, pady=5, side=LEFT)
c6_yaz = Text(frame_sag_c6, height=2, width=5)
c6 = IntVar(frame_sag_c6)
c6_yaz.pack(padx=10, pady=10, side=LEFT)

sagc7 = Label(frame_sag_c7, text="D7-D8", bg='#92c4f0', font="Verdana 10 bold").pack(padx=10, pady=5, side=LEFT)
c7_yaz = Text(frame_sag_c7, height=2, width=5)
c7 = IntVar(frame_sag_c7)
c7_yaz.pack(padx=10, pady=10, side=LEFT)

### Sağ Cam Tarafı ###

sagbd = Label(frame_sag_bd, text="D8-D9", bg='#92c4f0', font="Verdana 10 bold").pack(padx=10, pady=5, side=LEFT)
bd_yaz = Text(frame_sag_bd, height=2, width=5)
bd = IntVar(frame_sag_bd)
bd_yaz.pack(padx=10, pady=10, side=RIGHT)

sagd1 = Label(frame_sag_d1, text="D9-D10", bg='#92c4f0', font="Verdana 10 bold").pack(padx=10, pady=5, side=LEFT)
d1_yaz = Text(frame_sag_d1, height=2, width=5)
d1 = IntVar(frame_sag_d1)
d1_yaz.pack(padx=10, pady=10, side=RIGHT)

sagd2 = Label(frame_sag_d2, text="D10-D11", bg='#92c4f0', font="Verdana 10 bold").pack(padx=10, pady=5, side=LEFT)
d2_yaz = Text(frame_sag_d2, height=2, width=5)
d2 = IntVar(frame_sag_d2)
d2_yaz.pack(padx=10, pady=10, side=LEFT)

sagd3 = Label(frame_sag_d3, text="D11-D12", bg='#92c4f0', font="Verdana 10 bold").pack(padx=10, pady=5, side=LEFT)
d3_yaz = Text(frame_sag_d3, height=2, width=5)
d3 = IntVar(frame_sag_d3)
d3_yaz.pack(padx=10, pady=10, side=LEFT)

sagd4 = Label(frame_sag_d4, text="D12-D13", bg='#92c4f0', font="Verdana 10 bold").pack(padx=10, pady=5, side=LEFT)
d4_yaz = Text(frame_sag_d4, height=2, width=5)
d4 = IntVar(frame_sag_d4)
d4_yaz.pack(padx=10, pady=10, side=LEFT)

sagd5 = Label(frame_sag_d5, text="D13-D14", bg='#92c4f0', font="Verdana 10 bold").pack(padx=10, pady=5, side=LEFT)
d5_yaz = Text(frame_sag_d5, height=2, width=5)
d5 = IntVar(frame_sag_d5)
d5_yaz.pack(padx=10, pady=10, side=LEFT)

sagd6 = Label(frame_sag_d6, text="D14-D15", bg='#92c4f0', font="Verdana 10 bold").pack(padx=10, pady=5, side=LEFT)
d6_yaz = Text(frame_sag_d6, height=2, width=5)
d6 = IntVar(frame_sag_d6)
d6_yaz.pack(padx=10, pady=10, side=LEFT)

sagd7 = Label(frame_sag_d7, text="D15-D16", bg='#92c4f0', font="Verdana 10 bold").pack(padx=10, pady=5, side=LEFT)
d7_yaz = Text(frame_sag_d7, height=2, width=5)
d7 = IntVar(frame_sag_d7)
d7_yaz.pack(padx=10, pady=10, side=LEFT)


