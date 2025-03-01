from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Button(frm, text="Rosa", command=root.destroy).grid(column=1, row=0)
ttk.Button(frm, text="Azul", command=root.destroy).grid(column=1, row=0)
ttk.Button(frm, text="Verde", command=root.destroy).grid(column=1, row=0)
ttk.Button(frm, text="Amarelo", command=root.destroy).grid(column=1, row=0)
root.mainloop()