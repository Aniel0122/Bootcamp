def ej2(lista):
    resultado = [x for x in lista if x % 2 != 0]
    print(resultado)
    resultado = sum(resultado)
    print(resultado)

lista = list(range(50))

ej2(lista)
