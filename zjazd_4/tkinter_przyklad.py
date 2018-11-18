#istnieje wiele gui dla pythona
import tkinter

def sumuj():
    a = float(a_entry.get()) #<-- .get szuka wsrod istniejacychv nazw w programie
    b = float(b_entry.get())
    wynik.configure(text=a+b)

root = tkinter.Tk() #<-- zaczyna program

a_label = tkinter.Label(master=root,text="Parametr a") #<--przypina element do czegoś 1.krok, tu do root, więc root jest elementem nadrzednym
a_label.pack() #<--przypina element do czegoś 2.krok
a_entry = tkinter.Entry(master=root)
a_entry.pack()

b_label = tkinter.Label(master=root,text="Parametr b") #<--przypina element do czegoś 1.krok, tu do root, więc root jest elementem nadrzednym
b_label.pack() #<--przypina element do czegoś 2.krok
b_entry = tkinter.Entry(master=root)
b_entry.pack()

wynik_label = tkinter.Label(master=root,text="Wynik:")
wynik_label.pack()
wynik = tkinter.Label(master=root,text="-")
wynik.pack()

licz_button = tkinter.Button(master=root, text="Policz", command=sumuj)
licz_button.pack()

root.title("Sumator")

root.mainloop() #<--konczy taki program