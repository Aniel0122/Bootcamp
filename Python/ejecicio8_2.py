import pickle

class Vehiculo:
    def __init__(self, color, puertas):
        self.color = color
        self.puertas = puertas
    
    def __str__(self):
        return f"{self.color} {self.puertas}"

corsa = Vehiculo("dorado", "5")
print(corsa)

with open("vehiculo_ob", "wb") as file:
    pickle.dump(corsa, file)

with open("vehiculo_ob", "rb") as file:
    nuevo_corsa = pickle.load(file)

print(nuevo_corsa)