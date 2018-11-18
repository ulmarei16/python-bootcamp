import tkinter

def licz_koszt():
    a = int(dystans_entry.get())
    b = float(spal_entry.get())
    c = float(cena_entry.get())
    wynik = (a/100)*b*c
    koszt.configure(text=str(wynik) + " PLN")

root = tkinter.Tk()

dystans_label = tkinter.Label(master=root,text="Dystans:")
#dystans_label.pack()
dystans_label.grid(row=0,column=0)
dystans_entry = tkinter.Entry(master=root)
#dystans_entry.pack()
dystans_entry.grid(row=0,column=1)

spal_label = tkinter.Label(master=root,text="Spalanie:")
#spal_label.pack()
spal_label.grid(row=1,column=0)
spal_entry = tkinter.Entry(master=root)
#spal_entry.pack()
spal_entry.grid(row=1,column=1)

cena_label = tkinter.Label(master=root,text="Cena paliwa:")
#cena_label.pack()
cena_label.grid(row=2,column=0)
cena_entry = tkinter.Entry(master=root)
#cena_entry.pack()
cena_entry.grid(row=2,column=1)

koszt_label = tkinter.Label(master=root,text="Wynik:")
#koszt_label.pack()
koszt_label.grid(row=4,column=0)
koszt = tkinter.Label(master=root,text="-")
#koszt.pack()
koszt.grid(row=4,column=1)

licz_koszt_button = tkinter.Button(master=root, text="Licz koszt", command=licz_koszt)
#licz_koszt_button.pack()
licz_koszt_button.grid(row=3,column=0)


root.title("Liczenie kosztu przejazdu")

root.mainloop()