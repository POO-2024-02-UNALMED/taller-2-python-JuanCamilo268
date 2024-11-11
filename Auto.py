from Asiento import Asiento
from Motor import Motor
class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        cantidad = 0
        for i in self.asientos:
            if i != None:
                cantidad += 1
        return cantidad
    
    def verificarIntegridad(self):
        verificar = "Auto original"
        if self.registro != self.motor.registro:
            verificar = "Las piezas no son originales"
            return verificar
        else:
            for i in self.asientos:
                if i != None:
                    if self.registro != i.registro:
                        verificar = "Las piezas no son originales"
                        return verificar
        return verificar
