# Leer la entrada del usuario
items = input("Introduce países separados por comas:\n")

# Crear una lista de países a partir de la entrada del usuario
paises = [pais for pais in items.split(",")]

# Eliminar duplicados, ordenar y unir en una cadena separada por comas
paises_unicos_ordenados = sorted(list(set(paises)))
resultado = ",".join(paises_unicos_ordenados)

# Imprimir el resultado
print(resultado)