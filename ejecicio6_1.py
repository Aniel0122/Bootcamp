class vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class Coche(vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

coche1 = Coche("azul", 4, 5, 180, 200)
print(f"Coche 1: color {coche1.color}, {coche1.ruedas} ruedas, {coche1.puertas} puertas, velocidad {coche1.velocidad} km/h, cilindrada {coche1.cilindrada} cc.")

coche1 = Coche("Rojo", 4, 5, 120, 100)
print("Coche 2: color " + coche1.color + ", " + str(coche1.ruedas) + " ruedas, " + str(coche1.puertas) + " puertas, velocidad " + str(coche1.velocidad) + " km/h, cilindrada " + str(coche1.cilindrada) + " cc.")

