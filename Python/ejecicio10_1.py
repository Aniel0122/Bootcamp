from tkinter import *

def seleccionar_opcion(opcion):
    # La función que se ejecuta cuando se selecciona una opción
    monitor.config(text=opcion)

aniel = Tk()
aniel.title("Seleccionar opción")

# Creamos una variable StringVar para almacenar la opción seleccionada
opcion = StringVar()

# Creamos una lista de opciones
opciones = ["Naranja", "Uba", "Platanos", "Maiz"]

# Creamos un grupo de botones de radio y agregamos las opciones
for opcion_actual in opciones:
    Radiobutton(aniel, text=opcion_actual, variable=opcion, value=opcion_actual,
                command=lambda opcion_actual=opcion_actual: seleccionar_opcion(opcion_actual)).pack(anchor=W)

# Creamos una etiqueta para mostrar la opción seleccionada
monitor = Label(aniel)
monitor.pack()

# Creamos un botón para reiniciar la selección
Button(aniel, text="Reiniciar", command=lambda: opcion.set(None)).pack()

aniel.mainloop()