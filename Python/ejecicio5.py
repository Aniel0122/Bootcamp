
def anyobisiesto():
  anio: int = int(input("Introduce un año y para verificar si si es bisiesto:  "))

  if(anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)):
     print("El año ha sido veridicada el,",anio, "es bisiesto")
  else:
      print("Ha sido verificado. El año",anio ,  "no es bisiesto")

print(anyobisiesto())