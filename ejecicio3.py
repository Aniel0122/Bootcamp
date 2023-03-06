print ("------------Calcular la masa colpora-----------------")

kg= float(input("Cual es su peso en kg: "))
mt= float(input("Cual es tu estatura en metros: "))

#r = kg / mt

r = round(float(kg)/float(mt)**2,2)
print("Su masa corporal es: " + str(r))

input ("Precione entre para salir")
