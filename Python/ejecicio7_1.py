
# Se importa el módulo creado
from ejecicio7_1_1 import * 

a, b, c, d = (10, 10, 10, 10)

print( "{} + {} = {}".format(a, b, sumadores(a, b) ) )

print( "{} - {} = {}".format(b, d, restadores(b, d) ) )

print( "{} * {} = {}".format(b, b, multiplicarcion(b, b) ) ) 

print( "{} / {} = {}".format(a, c, division(a, c) ) )