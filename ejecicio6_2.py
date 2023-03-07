class alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre 
        self.nota = nota

    def imprimir_datos(self):
        print(f"Nombre del alumno: {self.nombre}")
        print(f"Nota: {self.nota}")

    def resultado(self):
         if self.nota >= 75:
             print(f"El alumno {self.nombre} ha aprogrado todas con exito")

         else:
             print(f"El alumno {self.nombre} lo sentimos ha supendido")

# Ejemplo de uso
alumno1 = alumno("Juan", 89)
alumno1.imprimir_datos()
alumno1.resultado()

alumno2 = alumno("María", 70)
alumno2.imprimir_datos()
alumno2.resultado()
# inicializamos la clase


