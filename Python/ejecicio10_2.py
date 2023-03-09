from tkinter import *

master = Tk()

listbox = Listbox(master)
for item in ["Manuel", "Carlos", "Juan", "Virtu", "Jean", "Laura", "Ana", "Lorena"]:
    listbox.insert(END, item)
listbox.pack()

label = Label(master, text="Lista de nombres de personas que se esta mostrando")
label.pack()

master.mainloop()