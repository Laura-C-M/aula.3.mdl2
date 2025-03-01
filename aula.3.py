from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("1000x300")

frm = ttk.Frame(root, padding=10)
frm.grid()

def change_color(color, color_name):
    root.config(bg=color)
    label.config(text=color_name)
label = Label(root, text="", font=("Times", 16))
label.grid(column=0, row=2, columnspan=3, pady=10)

button1 = ttk.Button(frm, text="Rosa", command=lambda: change_color("#FFC0CB", "Rosa"))
button1.grid(column=1, row=0, padx=10, pady=10, ipadx=20, ipady=20)

button2 = ttk.Button(frm, text="Lilás", command=lambda: change_color("#CB66FE", "Lilás"))
button2.grid(column=1, row=1, padx=10, pady=10, ipadx=20, ipady=20)

button3 = ttk.Button(frm, text="Azul", command=lambda: change_color("#8EE4FE", "Azul"))
button3.grid(column=2, row=0, padx=10, pady=10, ipadx=20, ipady=20)

button4 = ttk.Button(frm, text="Verde", command=lambda: change_color("#8EFEA1", "Verde"))
button4.grid(column=2, row=1, padx=10, pady=10, ipadx=20, ipady=20)

button5 = ttk.Button(frm, text="Vermelho", command=lambda: change_color("#FF4848", "Vermelho"))
button5.grid(column=3, row=0, padx=10, pady=10, ipadx=20, ipady=20)

button6 = ttk.Button(frm, text="Laranja", command=lambda: change_color("#FF9148", "Laranja"))
button6.grid(column=3, row=1, padx=10, pady=10, ipadx=20, ipady=20)

button7 = ttk.Button(frm, text="Amarelo", command=lambda: change_color("#FFEC5B", "Amarelo"))
button7.grid(column=4, row=0, padx=10, pady=10, ipadx=20, ipady=20)

button8 = ttk.Button(frm, text="Azul Escuro", command=lambda: change_color("#01034E", "Azul Escuro"))
button8.grid(column=4, row=1, padx=10, pady=10, ipadx=20, ipady=20)

button9 = ttk.Button(frm, text="Bordo", command=lambda: change_color("#5A0202", "Bordo"))
button9.grid(column=5, row=0, padx=10, pady=10, ipadx=20, ipady=20)

button10 = ttk.Button(frm, text="Roxo", command=lambda: change_color("#320030", "Roxo"))
button10.grid(column=5, row=1, padx=10, pady=10, ipadx=20, ipady=20)
