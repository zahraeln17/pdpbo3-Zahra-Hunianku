from tkinter import *
from user import User
import tkinter as Tkinter

user = []
#create root window
root = Tkinter.Tk()
root.title("TP3 DPBO Zahra")
#root.geometry("500x500")

def about():
        top = Toplevel()

        d_frame = LabelFrame(top, padx = 10, pady = 15)
        d_frame.pack(padx = 10, pady = 15)

        d_summary = Label(d_frame, text = "Aplikasi Jasa Titip \n", anchor="w").grid(row=0, column=0, sticky="w")
        d_summary = Label(d_frame, text = "Membuka jastip untuk orang orang yang ingin beli barang atau makanan yang diinginkan \n", anchor="w").grid(row=1, column=0, sticky="w")
        d_summary = Label(d_frame, text = "by: Zahra Elgysha – 1908767", anchor="w").grid(row=2, column=0, sticky="w")

        d_exit = Button(d_frame, text="Exit", command=top.destroy)
        d_exit.grid(row=4, column=0)

def masukan():

        global root
        root.withdraw()

        top = Toplevel()
        top.title("Input")
        
        d_frame = LabelFrame(top, padx=10, pady=10)
        d_frame.pack(padx=10, pady=10)
        
        #input1
        label_a = Label(d_frame, text="Nama").grid(row=0, column=0, sticky="w")
        input1 = Entry(d_frame, width=25)
        input1.grid(row=0, column=1, padx=20, pady=10, sticky="w")

        #input2
        label_b = Label(d_frame, text="No HP").grid(row=1, column=0, sticky="w")
        input2 = Entry(d_frame, width=25)
        input2.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        #input3 Radiobutton
        label_c = Label(d_frame, text="Jenis").grid(row=2, column=0, sticky="w")
        rad_Frame = LabelFrame(d_frame, borderwidth=0)
        rad_Frame.grid(row=2, column=1, padx=20, sticky="w")

        jenis = StringVar(rad_Frame)
        radio1 = Radiobutton(rad_Frame, text="Food", variable=jenis, value= "Food")
        radio1.grid(row=0, column=0, sticky="w")

        radio2 = Radiobutton(rad_Frame, text="Fashion", variable=jenis, value= "Fashion")
        radio2.grid(row=0, column=1, sticky="w")

        #input4
        label_d = Label(d_frame, text="Pesanan").grid(row=3, column=0, sticky="w")
        input4 = Entry(d_frame, width=25)
        input4.grid(row=3, column=1, padx=20, pady=10, sticky="w")

        #input5
        options = ["1","2","3","4","5"]
        var_jml = StringVar(root)
        var_jml.set(options[0])
        label_e = Label(d_frame, text="Jumlah").grid(row=4, column=0, sticky="w")
        input5 = OptionMenu(d_frame, var_jml, *options)
        input5.grid(row=4, column=1, padx=20, pady=10, sticky="w")

        #input6 untuk check button
        label_f = Label(d_frame, text="Mode Pengiriman").grid(row=5, column=0, sticky="w")
        frame_cb= LabelFrame(d_frame, borderwidth=0)
        frame_cb.grid(row=5, column=1, padx=20, pady=10, sticky="w")

        mode = []
        Mode1 = IntVar()  
        Mode2 = IntVar()  
        Mode3 = IntVar()
        Mode4 = IntVar()

        CB1 = Checkbutton(frame_cb, text="JNE", variable=Mode1, height=2, width=10)
        CB1.grid(row=0, column=0, sticky="w", pady=0)

        CB2 = Checkbutton(frame_cb, text = "SiCepat", variable=Mode2, height=2, width=10)
        CB2.grid(row=0, column=1, sticky="w", pady=0)

        CB3 = Checkbutton(frame_cb, text = "J&T", variable=Mode3, height=2, width=10)
        CB3.grid(row=0, column=2, sticky="w", pady=0)

        CB4 = Checkbutton(frame_cb, text = "COD", variable=Mode4, height=2, width=10)
        CB4.grid(row=0, column=3, sticky="w", pady=0)

        mode.append(Mode1)
        mode.append(Mode2)
        mode.append(Mode3)
        mode.append(Mode4)

        #button frame
        frame_btn = LabelFrame(d_frame, borderwidth=0)
        frame_btn.grid(row = 10, columnspan = 2,column = 0, pady = 10)

        #button submit
        btn_submit = Button(frame_btn, text="Submit", anchor="s", command=lambda:[save_data(top, input1, input2, jenis, input4, var_jml, mode), top.withdraw()])
        btn_submit.grid(row=5, column=0, padx=10)

        #button cancel
        btn_cancel = Button(frame_btn, text="Back", anchor="s", command=lambda:[top.destroy(), root.deiconify()])
        btn_cancel.grid(row=5, column=1, padx=10)

def save_data(parent, nama, noHp, jenis, pesanan, jumlah, modee):
        top = Toplevel()
        
        nama = nama.get()
        noHp = noHp.get()
        jenis = jenis.get()
        pesanan = pesanan.get()
        jumlah = jumlah.get()
        mode = []
        if(modee[0].get()==1): mode.append("JNE")
        if(modee[1].get()==1): mode.append("SiCepat")
        if(modee[2].get()==1): mode.append("J&T")
        if(modee[3].get()==1): mode.append("COD")

        if(nama != '' and noHp != '' and jenis != '' and pesanan != '' and jumlah != ''):
                user.append(User(nama, noHp, jenis, pesanan, jumlah, mode))

                top.title("Ditambahkan")
                lbl = Label(top, text="Data Berhasil Ditambahkan!", fg="red")
                lbl.pack(padx=30, pady=15)

                btn_Oke = Button(top, text = "Oke", anchor="s", command=lambda:[top.destroy(), parent.deiconify()])
                btn_Oke.pack(padx=5, pady=5)
        else:
                top.title("Tidak bisa ditambahkan")
                lbl = Label(top, text="Isi semua data dengan benar!", fg="red")
                lbl.pack(padx=30, pady=15)

                btn_Oke = Button(top, text = "Oke", anchor="s", command=lambda:[top.destroy(), parent.deiconify()])
                btn_Oke.pack(padx=5, pady=5)

def semua_data():
        global root
        root.withdraw()

        top = Toplevel
        top.title("Semua Pesanan")
        frame_lbl = LabelFrame(top, borderwidth=0)
        frame_lbl.pack()

        #button cancel
        btn_cancel = Button(frame, text="Back", anchor="w", command=lambda:[top.destroy(), root.deiconify()])
        btn_cancel.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        #header title
        header = LabelFrame(frame_lbl)
        header.grid(row=0, column=0, columnspan=2)

        tbl_Frame = LabelFrame(frame)
        tbl_Frame.grid(row=1, column = 0, columnspan=2)
        #title
        a_title = Label(tbl_Frame, text="Nama", borderwidth=1, relief="solid", width=10, padx=5).grid(row=0, column=0)
        b_title = Label(tbl_Frame, text="No HP", borderwidth=1, relief="solid", width=10, padx=5).grid(row=0, column=1)
        c_title = Label(tbl_Frame, text="Jenis", borderwidth=1, relief="solid", width=10, padx=5).grid(row=0, column=2)
        d_title = Label(tbl_Frame, text="Pesanan", borderwidth=1, relief="solid", width=25, padx=5).grid(row=0, column=3)
        e_title = Label(tbl_Frame, text="Jumlah", borderwidth=1, relief="solid", width=5, padx=5).grid(row=0, column=4)
        f_title = Label(tbl_Frame, text="Mode", borderwidth=1, relief="solid", width=10, padx=5).grid(row=0, column=5)
        #menampilkan
        i=0
        for data in user:
                tampil_1 = Label(tbl_Frame, text=data.get_nama(), relief="solid", borderwidth=1, width=10, height=2, padx=5).grid(row=i+1, column=0)
                tampil_2 = Label(tbl_Frame, text=data.get_noHp(), relief="solid", borderwidth=1, width=10, height=2, padx=5).grid(row=i+1, column=1)
                tampil_3 = Label(tbl_Frame, text=data.get_jenis(), relief="solid", borderwidth=1, width=10, height=2, padx=5).grid(row=i+1, column=2)
                tampil_4 = Label(tbl_Frame, text=data.get_pesanan(), relief="solid", borderwidth=1, width=25, height=2, padx=5).grid(row=i+1, column=3)
                tampil_5 = Label(tbl_Frame, text=data.get_jumlah(), relief="solid", borderwidth=1, width=5, height=2, padx=5).grid(row=i+1, column=4)
                tampil_6 = Label(tbl_Frame, text=data.get_mode(), relief="solid", borderwidth=1, width=10, height=2, padx=5).grid(row=i+1, column=5)
        
def clear_data():
        top = Toplevel()
                
        clear_lbl = Label(top, text="Hapus semua data?")
        clear_lbl.pack(padx=20, pady=20)
        btn_frame = LabelFrame(top, borderwidth=0)
        btn_frame.pack(padx=20, pady=20)
        #untuk tombol yes
        yes_btn = Button(btn_frame, text = "Yes", fg="black", command=lambda:[top.destroy(),user.clear()])
        yes_btn.grid(row=0, column=0, padx=10)
        #untuk tombol no
        no_btn = Button(btn_frame, text = "No", fg="black", command = top.destroy)
        no_btn.grid(row=0, column=1,padx=10)

def exit():
        global root
        root.withdraw()

        top = Toplevel()
        exit_lbl = Label(top, text="Keluar dari aplikasi?")
        exit_lbl.pack(padx=20, pady=20)
        btn_frame = LabelFrame(top, borderwidth=0)
        btn_frame.pack(padx=20, pady=20)
        #untuk tombol yes
        yes_btn = Button(btn_frame, text = "Yes", fg="black", command=lambda:[top.destroy(),user.clear()])
        yes_btn.grid(row=0, column=0, padx=10)
        #untuk tombol no
        no_btn = Button(btn_frame, text = "No", fg="black", command = top.destroy)
        no_btn.grid(row=0, column=1,padx=10)



#title
a_frame = Tkinter.LabelFrame(root, padx=10, pady=10, bg="pink")
a_frame.pack(padx=10, pady=10)
header1 = Label(a_frame, text="Jasa Titip Yuk!", bg="pink", font=("arial",25))
header1.pack()

header2 = Label(a_frame, text="Jastip fashion dan makanan yang kalian inginkan dengan fee 15000/item", bg="pink", font=(25))
header2.pack()

#button input
bg = Frame(root, padx=10, pady=10)
bg.pack(padx=10, pady=10)

input_btn = Button(bg, text="Input Data Jastip", command=masukan, width=20, font=(50))
input_btn.grid(row=0, column=0, pady=5)

#see all submissons
input_btn = Button(bg, text="See All Submissons", command=semua_data, width=20, font=(50))
input_btn.grid(row=1, column=0, pady=5)

#clear submissons
clear_btn = Button(bg, text="Clear Submissons", command=clear_data, width=20, font=(50))
clear_btn.grid(row=2, column=0, pady=5)

#ABOUT
about_btn = Button(bg, text="About", command=about, width=20, font=(50))
about_btn.grid(row=3, column=0, pady=5)

#EXIT
exit_btn = Button(bg, text="Exit", command=exit, width=5, font=(50))
exit_btn.grid(row=4, column=0, pady=5)


root.mainloop()